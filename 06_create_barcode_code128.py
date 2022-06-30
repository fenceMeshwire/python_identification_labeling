#!/usr/bin/env python3

# Python 3.9.5

# 06_create_barcode_code128.py

# Code128 is fully described in the international standard ISO/IEC 15417.

# Dependencies
import barcode
from barcode.writer import ImageWriter
import os

# Change directory to specific output directory:
p = 'C:\\Users\\name\\output'
os.chdir(p)

identifier = 'Label_Code128'   
BCODE = barcode.get_barcode_class('code128')
my_code128 = BCODE(identifier, writer=ImageWriter())
file = my_code128.save(identifier)

print(file) # Print file name, file will be saved as PNG
