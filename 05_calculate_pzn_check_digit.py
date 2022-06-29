#!/usr/bin/env python3

# Python 3.9.5

# 05_calc_pzn_check_digit.py

def calc_pzn_check_digit(identifier):
    counter:int = 1
    check_digit:int = 0
    subtotal:int = 0
    total:int = 0
    full_identifier:str = ""

    for digit in identifier:
        subtotal = int(digit) * (counter + 1)
        total = total + subtotal
        counter += 1
    check_digit = total % 11

    if check_digit == 10:
        check_digit = None
        full_identifier = identifier
    else:
        full_identifier = identifier + str(check_digit)
    return full_identifier, check_digit

if __name__ == '__main__':
    # The full identifier is often specified as follows: 08906763
    # Enter the data without the leading '0':
    identifier = '8906763'
    identifier = identifier[0:-1:1]
    full_identifier, check_digit = calc_pzn_check_digit(identifier)
    if not check_digit == None:
        print('PZN full identifier: ' + str(full_identifier))
        print('PZN check digit: ' + str(check_digit))
    else:
        print('The check digit cannot be calculated for this particular PZN.')
        print('This is part of the PZN combination rule.')
