#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2014 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy
from gnuradio import gr
import pmt

from varicode_table import VARICODE

class varicode_enc_b(gr.sync_block):
    """
    docstring for block varicode_enc_b
    """
    def __init__(self):
        gr.sync_block.__init__(self,
            name="varicode_enc_b",
            in_sig=None,
            out_sig=[numpy.uint8])

        self.message_port_register_in(pmt.intern('in_port'))
        self.set_msg_handler(pmt.intern('in_port'),
                             self.handle_msg)

        self.transmitting = False
        self.tx_index = 0
        self.tx_data = []

    def handle_msg(self, msg):
        if self.transmitting:
            return

        msg = str(msg)

        # pre-amble
        self.tx_data = [0] * 16

        for char in msg:
            if ord(char) > len(VARICODE):
                continue

            self.tx_data += VARICODE[ord(char)]
            self.tx_data += [0, 0]

        # post-amble
        self.tx_data += [1] * 16

        # append a few more 1's to round up to 16
        remaining_bits = 8 - (len(self.tx_data) % 8)
        self.tx_data += [1] * remaining_bits
        self.transmitting = True

    def work(self, input_items, output_items):
        nout = 0

        if self.transmitting:
            out = output_items[0]
            
            while nout < len(out) and self.tx_index < len(self.tx_data):
                out[nout] = self.tx_data[self.tx_index]
                nout += 1
                self.tx_index += 1

            if self.tx_index == len(self.tx_data):
                try:
                    msg = self.msg_queue.get_nowait()
                    self.setup_next_msg(msg)
                except Queue.Empty:
                    self.transmitting = False
        else:
            self.stop()

        return nout

