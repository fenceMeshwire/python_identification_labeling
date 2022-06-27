#!/usr/bin/env python3

# Python 3.9.5

# 03_calculate_ean13_check_digit.py

def calc_ean13_check_digit(identifier):
    odd_sum = 0
    even_sum = 0
    resulting_sum = 0
    reversed_identifier = identifier[::-1]
    counter = 1
    for number in reversed_identifier:
        if counter // 2 != 0:
            odd_sum = odd_sum + int(number) * 3
        if counter //2 == 0:
            even_sum = even_sum + int(number) * 1
        counter += 1
    resulting_sum = odd_sum + even_sum
    check_digit = resulting_sum % 10
    return identifier + str(check_digit), check_digit

if __name__ == '__main__':
    identifier:str = '410525002200' 
    full_identifier, check_digit = calc_ean13_check_digit(identifier)
    print('Full identifier:\t' + full_identifier)
    print('Check digit:\t' + check_digit)
