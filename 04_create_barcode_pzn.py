#!/usr/bin/env python3

# Python 3.9.5

# 04_create_barcode_pzn.py

# The Pharmacy Central Number (PZN) is a nationally standardized 
# identification code in Germany for pharmaceuticals, medical devices 
# and other products commonly sold in pharmacies.

# Dependencies
import barcode
from barcode.writer import ImageWriter
import os

# Change directory to specific output directory:
p = 'C:\\Users\\name\\output'
os.chdir(p)

identifier = '8906763'
BCODE = barcode.get_barcode_class('pzn')
my_pzn = BCODE(identifier, writer=ImageWriter())
file = my_pzn.save(identifier)

print(file) # Print file name, file will be saved as PNG
