#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2014 Tim Kuester
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

VARICODE = [
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 1, 1, 0, 1, 1, 0, 1, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 1, 1],
    [1, 1, 0, 1, 0, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 1],  
    [1, 1, 1, 0, 1],     
    [1, 1, 0, 1, 1, 0, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1],     
    [1, 1, 0, 1, 1, 1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 1, 1, 1],
    [1, 1, 0, 1, 0, 1, 1, 0, 1, 1],
    [1, 1, 0, 1, 1, 0, 1, 0, 1, 1],
    [1, 1, 0, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 1, 0, 1, 0, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 1, 0, 1, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 0, 1, 1, 0, 1, 1, 1],
    [1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
    [1],         
    [1, 1, 1, 1, 1, 1, 1, 1, 1], 
    [1, 0, 1, 0, 1, 1, 1, 1, 1], 
    [1, 1, 1, 1, 1, 0, 1, 0, 1], 
    [1, 1, 1, 0, 1, 1, 0, 1, 1], 
    [1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1], 
    [1, 1, 1, 1, 1, 0, 1, 1],  
    [1, 1, 1, 1, 0, 1, 1, 1],  
    [1, 0, 1, 1, 0, 1, 1, 1, 1], 
    [1, 1, 1, 0, 1, 1, 1, 1, 1], 
    [1, 1, 1, 0, 1, 0, 1],   
    [1, 1, 0, 1, 0, 1],    
    [1, 0, 1, 0, 1, 1, 1],   
    [1, 1, 0, 1, 0, 1, 1, 1, 1], 
    [1, 0, 1, 1, 0, 1, 1, 1],  
    [1, 0, 1, 1, 1, 1, 0, 1],  
    [1, 1, 1, 0, 1, 1, 0, 1],  
    [1, 1, 1, 1, 1, 1, 1, 1],  
    [1, 0, 1, 1, 1, 0, 1, 1, 1], 
    [1, 0, 1, 0, 1, 1, 0, 1, 1], 
    [1, 0, 1, 1, 0, 1, 0, 1, 1], 
    [1, 1, 0, 1, 0, 1, 1, 0, 1], 
    [1, 1, 0, 1, 0, 1, 0, 1, 1], 
    [1, 1, 0, 1, 1, 0, 1, 1, 1], 
    [1, 1, 1, 1, 0, 1, 0, 1],  
    [1, 1, 0, 1, 1, 1, 1, 0, 1], 
    [1, 1, 1, 1, 0, 1, 1, 0, 1], 
    [1, 0, 1, 0, 1, 0, 1],   
    [1, 1, 1, 0, 1, 0, 1, 1, 1], 
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 0, 1],   
    [1, 1, 1, 0, 1, 0, 1, 1],  
    [1, 0, 1, 0, 1, 1, 0, 1],  
    [1, 0, 1, 1, 0, 1, 0, 1],  
    [1, 1, 1, 0, 1, 1, 1],   
    [1, 1, 0, 1, 1, 0, 1, 1],  
    [1, 1, 1, 1, 1, 1, 0, 1],  
    [1, 0, 1, 0, 1, 0, 1, 0, 1], 
    [1, 1, 1, 1, 1, 1, 1],   
    [1, 1, 1, 1, 1, 1, 1, 0, 1], 
    [1, 0, 1, 1, 1, 1, 1, 0, 1], 
    [1, 1, 0, 1, 0, 1, 1, 1],  
    [1, 0, 1, 1, 1, 0, 1, 1],  
    [1, 1, 0, 1, 1, 1, 0, 1],  
    [1, 0, 1, 0, 1, 0, 1, 1],  
    [1, 1, 0, 1, 0, 1, 0, 1],  
    [1, 1, 1, 0, 1, 1, 1, 0, 1], 
    [1, 0, 1, 0, 1, 1, 1, 1],  
    [1, 1, 0, 1, 1, 1, 1],   
    [1, 1, 0, 1, 1, 0, 1],   
    [1, 0, 1, 0, 1, 0, 1, 1, 1], 
    [1, 1, 0, 1, 1, 0, 1, 0, 1], 
    [1, 0, 1, 0, 1, 1, 1, 0, 1], 
    [1, 0, 1, 1, 1, 0, 1, 0, 1], 
    [1, 0, 1, 1, 1, 1, 0, 1, 1], 
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 1], 
    [1, 1, 1, 1, 0, 1, 1, 1, 1], 
    [1, 1, 1, 1, 1, 1, 0, 1, 1], 
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 1, 1, 0, 1], 
    [1, 0, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 0, 1, 1],      
    [1, 0, 1, 1, 1, 1, 1],   
    [1, 0, 1, 1, 1, 1],    
    [1, 0, 1, 1, 0, 1],    
    [1, 1],        
    [1, 1, 1, 1, 0, 1],    
    [1, 0, 1, 1, 0, 1, 1],   
    [1, 0, 1, 0, 1, 1],    
    [1, 1, 0, 1],      
    [1, 1, 1, 1, 0, 1, 0, 1, 1], 
    [1, 0, 1, 1, 1, 1, 1, 1],  
    [1, 1, 0, 1, 1],     
    [1, 1, 1, 0, 1, 1],    
    [1, 1, 1, 1],      
    [1, 1, 1],       
    [1, 1, 1, 1, 1, 1],    
    [1, 1, 0, 1, 1, 1, 1, 1, 1], 
    [1, 0, 1, 0, 1],     
    [1, 0, 1, 1, 1],     
    [1, 0, 1],       
    [1, 1, 0, 1, 1, 1],    
    [1, 1, 1, 1, 0, 1, 1],   
    [1, 1, 0, 1, 0, 1, 1],   
    [1, 1, 0, 1, 1, 1, 1, 1],  
    [1, 0, 1, 1, 1, 0, 1],   
    [1, 1, 1, 0, 1, 0, 1, 0, 1], 
    [1, 0, 1, 0, 1, 1, 0, 1, 1, 1],
    [1, 1, 0, 1, 1, 1, 0, 1, 1], 
    [1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

class varicode_enc_bb(gr.basic_block):
    """
    Encodes an 8-bit byte (ie: characters) into a serial stream of
    bits mapping to the variable length code from the PSK31 spec,
    and attaches the two bit separator (00).

    For example: 't' (0x74) maps to varicode 101. This block will
    output the following five bytes (representative of bits):
    [1, 0, 1, 0, 0]. To ensure interoperability between GNU Radio
    and other PSK31 software, the bits are inverted (so they actually
    come out as [0, 1, 0, 1, 1].

    If you are using GNU Radio's "PSK Mod" block (3.7.3), you should
    use a bit->byte packer, with K=8.

    http://www.arrl.org/psk31-spec
    """
    def __init__(self):
        gr.basic_block.__init__(self,
            name="varicode_enc_bb",
            in_sig=[numpy.byte],
            out_sig=[numpy.byte])

    def forecast(self, noutput_items, ninput_items_required):
        #setup size of input_items[i] for work call
        for i in range(len(ninput_items_required)):
            ninput_items_required[i] = 1

    def general_work(self, input_items, output_items):
        consumed = 0
        out_idx = 0

        for i, val in enumerate(input_items[0]):
            val = numpy.uint8(val)
            code = VARICODE[val]

            if (out_idx + len(code) + 2) > len(output_items[0]):
                break

            consumed += 1

            for bit in code:
                if bit == 1:
                    output_items[0][out_idx] = 0
                else:
                    output_items[0][out_idx] = 1
                out_idx += 1

            output_items[0][out_idx] = 1
            output_items[0][out_idx + 1] = 1
            out_idx += 2

        self.consume(0, consumed)

        return out_idx
