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


import time
import numpy

from gnuradio import gr, gr_unittest, blocks
from varicode_enc_b import varicode_enc_b
import pmt


# Simple block to generate messages
class message_generator(gr.sync_block):
    def __init__(self, msg_list, msg_interval):
        gr.sync_block.__init__(
            self,
            name = "message generator",
            in_sig = [numpy.float32],
            out_sig = None
        )   

        self.msg_list = msg_list
        self.msg_interval = msg_interval
        self.msg_ctr = 0 
        self.message_port_register_out(pmt.intern('out_port'))


    def work(self, input_items, output_items):
        inLen = len(input_items[0])
        while self.msg_ctr < len(self.msg_list) and \
                (self.msg_ctr * self.msg_interval) < \
                (self.nitems_read(0) + inLen):
            self.message_port_pub(pmt.intern('out_port'),
                                  self.msg_list[self.msg_ctr])
            self.msg_ctr += 1
        return inLen

class qa_varicode_enc_b (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_t (self):
        count = 2
        interval = 1000
        msg_list = [pmt.string_to_symbol('hello')] * count
        src_data = [1.0] * (count * interval)

        src = blocks.vector_source_f(src_data, False)
        msg_gen = message_generator(msg_list, interval)
        msg_cons = varicode_enc_b()

        dest = blocks.vector_sink_b()

        self.tb.connect(src, msg_gen)
        self.tb.connect(msg_cons, dest)

        self.tb.msg_connect(msg_gen, 'out_port', msg_cons, 'in_port')

        self.tb.run()

        print "Msg Ctr:", msg_gen.msg_ctr
        while msg_gen.msg_ctr < count:
            print "Msg Ctr:", msg_gen.msg_ctr
            time.sleep(0.5)
        print "Msg Ctr:", msg_gen.msg_ctr

        self.tb.stop()
        self.tb.wait()

        print 'Output Data:', dest.data()

if __name__ == '__main__':
    gr_unittest.run(qa_varicode_enc_b, "qa_varicode_enc_b.xml")
