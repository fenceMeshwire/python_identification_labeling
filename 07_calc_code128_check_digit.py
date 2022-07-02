#!/usr/bin/env python3

# Python 3.9.5

# 07_calc_code128_check_digit.py

def calculate_check_digit(identifier, level='B'):
    """Code 128 is divided into three different character sets, referred to as Level A, Level B and Level C."""
    """The level of the barcode representation is indicated with the start character"""

    code128_level_A:dict = {
        '\s': 0, '!': 1, '"': 2, '#': 3, '$': 4, '%': 5, '&': 6, "'": 7, '(': 8, ')': 9, 
        '*': 10, '+': 11, ',': 12, '-': 13, '.': 14, '/': 15, '0': 16, '1': 17, '2': 18, '3': 19,
        '4': 20, '5': 21, '6': 22, '7': 23, '8': 24, '9': 25, ':': 26, ';': 27, '<' : 28, '=': 29,
        '>': 30, '?': 31, '@': 32, 'A': 33, 'B': 34, 'C': 35, 'D': 36, 'E': 37, 'F': 38, 'G': 39,
        'H': 40, 'I': 41, 'J': 42, 'K': 43, 'L': 44, 'M': 45, 'N': 46, 'O': 47, 'P': 48, 'Q': 49,
        'R': 50, 'S': 51, 'T': 52, 'U': 53, 'V': 54, 'W': 55, 'X': 56, 'Y': 57, 'Z': 58, '[': 59, 
        '\\': 60, ']': 61, '?': 62, '-': 63, 'NUL': 64, 'SOH': 65, 'STX': 66, 'ETX': 67, 'EOT': 68, 'ENQ': 69,
        'ACK': 70, 'BEL': 71, 'BS': 72, 'HT': 73, 'LF': 74, 'VT': 75, 'FF': 76, 'CR': 77, 'SO': 78, 'SI': 79, 
        'DLE': 80, 'DC1': 81, 'DC2': 82, 'DC3': 83, 'DC4': 84, 'NAK': 85, 'SYN': 86, 'ETB': 87, 'CAN': 88, 'EM': 89, 
        'SUB': 90, 'ESC': 91, 'FS': 92, 'GS': 93, 'RS': 94, 'US': 95, 'FNC3 ': 96, 'FNC 2': 97, 'Shift B': 98, 'Code C': 99,
        'Code B': 100, 'FNC 4': 101, 'FNC 1': 102, 'Start Code A': 103, 'Start Code B': 104, 'Start Code C': 105, 'Stop': 106
        }

    code128_level_B:dict = {
        '\s': 0, '!': 1, '"': 2, '#': 3, '$': 4, '%': 5, '&': 6, "'": 7, '(': 8, ')': 9, 
        '*': 10, '+': 11, ',': 12, '-': 13, '.': 14, '/': 15, '0': 16, '1': 17, '2': 18, '3': 19,
        '4': 20, '5': 21, '6': 22, '7': 23, '8': 24, '9': 25, ':': 26, ';': 27, '<' : 28, '=': 29,
        '>': 30, '?': 31, '@': 32, 'A': 33, 'B': 34, 'C': 35, 'D': 36, 'E': 37, 'F': 38, 'G': 39,
        'H': 40, 'I': 41, 'J': 42, 'K': 43, 'L': 44, 'M': 45, 'N': 46, 'O': 47, 'P': 48, 'Q': 49,
        'R': 50, 'S': 51, 'T': 52, 'U': 53, 'V': 54, 'W': 55, 'X': 56, 'Y': 57, 'Z': 58, '[': 59, 
        '\\': 60, ']': 61, '?': 62, '-': 63, '`': 64, 'a': 65, 'b': 66, 'c': 67, 'd': 68, 'e': 69,
        'f': 70, 'g': 71, 'h': 72, 'i': 73, 'j': 74, 'k': 75, 'l': 76, 'm': 77, 'n': 78, 'o': 79, 
        'p': 80, 'q': 81, 'r': 82, 's': 83, 't': 84, 'u': 85, 'v': 86, 'w': 87, 'x': 88, 'y': 89, 
        'z': 90, '{': 91, '|': 92, '}': 93, '?': 94, 'DEL': 95, 'FNC 3': 96, 'FNC 2': 97, 'SHIFT A': 98, 'Code C': 99,
        'FNC 4': 100, 'CODE A': 101, 'FNC 1': 102, 'Start Code A': 103, 'Start Code B': 104, 'Start Code C': 105, 'Stop': 106
        }

    code128_level_C:dict = {
        '00': 0,  '01': 1,  '02': 2,  '03': 3,  '04': 4,  '05': 5,  '06': 6,  '07': 7,  '08': 8,  '09': 9, 
        '10': 10, '11': 11, '12': 12, '13': 13, '14': 14, '15': 15, '16': 16, '17': 17, '18': 18, '19': 19,
        '20': 20, '21': 21, '22': 22, '23': 23, '24': 24, '25': 25, '26': 26, '27': 27, '28': 28, '29': 29,
        '30': 30, '31': 31, '32': 32, '33': 33, '34': 34, '35': 35, '36': 36, '37': 37, '38': 38, '39': 39,
        '40': 40, '41': 41, '42': 42, '43': 43, '44': 44, '45': 45, '46': 46, 'O' : 47, 'P' : 48, 'Q' : 49,
        '50': 50, '51': 51, '52': 52, '53': 53, '54': 54, '55': 55, '56': 56, 'Y': 57, 'Z': 58, '[': 59, 
        '60': 60, '61': 61, '62': 62, '63': 63, '64': 64, '65': 65, '66': 66, 'c': 67, 'd': 68, 'e': 69,
        '70': 70, '71': 71, '72': 72, '73': 73, '74': 74, '75': 75, '76': 76, 'm': 77, 'n': 78, 'o': 79, 
        '80': 80, '81': 81, '82': 82, '83': 83, '84': 84, '85': 85, '86': 86, 'w': 87, 'x': 88, 'y': 89, 
        '90': 90, '91': 91, '92': 92, '93': 93, '94': 94, '95': 95, '96': 96, '97': 97, '98': 98, '99': 99, 
        'Code B': 100, 'CODE A': 101, 'FNC 1': 102, 'Start Code A': 103, 'Start Code B': 104, 'Start Code C': 105, 'Stop': 106
        }

    counter:int = 1
    total = 0
 
    for character in identifier:
        transformation = code128_level_B[character]
        subtotal = int(transformation) * counter
        total = total + subtotal
        counter += 1
    if level == 'B':
        total = 104 + total
    value = total % 103
    check_digit = list(code128_level_B.keys())[list(code128_level_B.values()).index(value)]
    
    return check_digit

if __name__ == '__main__':
    identifier = 'ProductABC'
    level = 'B' # The level is indicated with the start character of the barcode.
    check_digit = calculate_check_digit(identifier, level)
    print('Identifier:  ' + str(identifier))
    if check_digit == "l":
        print('Please check the level, the check digit equals the value 1.')
    else:
        print('Check digit: ' + str(check_digit))
