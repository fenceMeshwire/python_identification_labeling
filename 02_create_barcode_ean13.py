#!/usr/bin/env python3

# Python 3.9.5

# 02_create_barcode_ean13.py

import barcode
from barcode.writer import ImageWriter
import os

# Change directory to specific output directory:
p = 'C:\\Users\\name\\output'
os.chdir(p)

# The identifier must have a length of 12 digits, 13 is the check digit:
# 1 2 3 4 5 6 7 8 9 10 11 12 (13)
#                
# Country code      (1-3)           
# Company number    (4-9)  
# Item number       (10-12)
# Check digit       (13)

identifier = '410525002200'   
BCODE = barcode.get_barcode_class('ean')
my_ean = BCODE(identifier, writer=ImageWriter())
file = my_ean.save(identifier)

print(file) # Print file name, file will be saved as PNG
