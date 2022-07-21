#!/usr/bin/env python3

# Python 3.9.5

# 08_qr_code.py

# QR-Code: QUICK RESPONSE CODE
# The QR-Code is encountered in a size from 21 x 21 to 177 x 177 fields (points). 
# Alternatively, 7089 digits or digits or 4296 alphanumeric characters can be encoded with it.
# An error correction allows a meaningful reconstruction of the QR code even if 
# up to 30% of the data area is destroyed.
# The QR code has squares distributed in three corners and nested within each other, 
# which serve as search elements.

import os
import qrcode

path = 'C:\\Users\user\\QR-Code' # Change the working directory as needed.

qr_code = qrcode.QRCode(
    version=1,    # 1 to 42; controls the size of the QR-Code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # err_corr_percent = {'L': 7, 'M': 15, 'Q': 25, 'H': 30}
    box_size=15,
    border=6,
)
qr_code.add_data('https://github.com/')
qr_code.make(fit=True)

# String values:
img = qr_code.make_image(back_color="white", fill_color="black")
# RGB color tuples:
img = qr_code.make_image(back_color=(0, 0, 0), fill_color=(255, 255, 255))

# Save the image:
img.save("sample_qr_code.png")
