#!/usr/bin/env python3

# Python 3.9.5

# 01_create_barcode_code39.py
import barcode
from barcode.writer import ImageWriter
import os

# Change directory:
p = 'C:\\Users\\name\\output'
os.chdir(p)

identifier = 'ABCDE123524FG2231'
BCODE = barcode.get_barcode_class('code39')
my_code39 = BCODE(identifier, writer=ImageWriter())
file = my_code39.save(identifier)

print(file) # Print file name, file will be saved as PNG 
