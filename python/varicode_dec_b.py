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

import sys
import numpy
from gnuradio import gr

from varicode_table import VARICODE

class varicode_dec_b(gr.sync_block):
    """
    docstring for block varicode_dec_b
    """
    def __init__(self):
        gr.sync_block.__init__(self,
            name="varicode_dec_b",
            in_sig=[numpy.byte],
            out_sig=None)

        self.count = 0
        self.symbol = []

    def work(self, input_items, output_items):
        in0 = input_items[0]

        for bit in in0:
            if bit == 1:
                if self.count >= 2:
                    self.symbol = self.symbol[:(self.count * -1)]

                    try:
                        sys.stdout.write(chr(VARICODE.index(self.symbol)))
                        sys.stdout.flush()
                    except ValueError:
                        pass

                    self.symbol = []

                self.count = 0
                self.symbol.append(bit)

            if bit == 0:
                if len(self.symbol) > 0:
                    self.count += 1
                    self.symbol.append(bit)

        # <+signal processing here+>
        return len(input_items[0])

