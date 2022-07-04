#!/usr/bin/env python3

# Python 3.9.5

# VIN.py

# Algorithm for calculating the check digit of the vehicle identification number (VIN)
# according to USA/Federal 49 CFR 565

# VIN decipherment:
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
# WMI   |         |  | 
# (1-3) |         |  |
#       VDS (4-8) |  |
#                 |  |
#       check-digit  | model year (10th digit)
#                    VIS (9-17)

# model_year_code = {2005:5, 2006:6, 2007:7, 2008:8, 2009:9, 2010:"A", 2011:"B", \
#       2012:"C", 2013:"D", 2014:"E", 2015:"F", 2016:"G", 2017:"H", 2018:"J", \
#       2019:"K", 2020:"L", 2021:"M", 2022:"N", 2023:"P", 2024:"R", 2025:"S", 2026:"T", \
#       2027:"V", 2028:"W", 2029:"X", 2030:"Y", 2031:"1", 2032:"2", 2032:"3"}

def calculate_check_digit(vin):

  if len(vin) == 17:
    plausibility = True
  elif len(vin) < 17:
    plausibility = False
    return
  elif len(vin) > 17:
    plausibility = False
    return

  assigned_values = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8,"J":1, "K":2, \
    "L":3, "M":4, "N":5, "P":7, "R":9, "S":2, "T":3, "U":4, "V":5, "W":6, "X":7, "Y":8, "Z":9, \
      "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "0":0}

  weight_factors = {"1":8, "2":7, "3":6, "4":5, "5":4, "6":3, "7":2, "8":10, "10":9, "11":8, \
        "12":7, "13":6, "14":5, "15":4, "16":3, "17":2}

  check_digits = {"0.000":0, "0.091":1, "0.182":2, "0.273":3, "0.364":4, "0.455":5, "0.545":6, \
        "0.636":7, "0.727":8, "0.818":9, "0.909":"X"}

  position = 0
  total = 0
  
  for digit in vin:
    assigned_value = assigned_values.get(digit)
    position += 1
    if position == 9:
      continue # Check-Digit
    weight_factor = weight_factors.get(str(position))
    subtotal = int(assigned_value) * int(weight_factor)
    total = total + subtotal

  check_digit = total / 11
  check_digit = check_digit - int(check_digit)
  check_digit = "%.3f" % check_digit
  result = check_digits.get(check_digit)
  
  return result, plausibility

if __name__ == '__main__':

  vin = 'ABCDE123824F22231'
  nineth_digit = vin[8]
  result, plausibilty = calculate_check_digit(vin)

  if str(result) == str(nineth_digit) and plausibilty == True:
    print("Result: The check digit is correct.")
    print('WMI:\t\t\t', vin[0:3]) 
    print('VDS Code:\t\t', vin[3:7])
    print('VDS - Free Digit:\t',vin[7:8]) 
    print('Check Digit:\t\t',vin[8:9])
    print('Model Year:\t\t',vin[9:10])
    print('Plant Identifier:\t',vin[10:11])
    print('Running number:\t\t',vin[11:17])
  elif str(result) != str(nineth_digit) and plausibilty == True:
    print("Result: ERROR - The VIN is not correct.\nDEVIATION:")
    print("Nineth digit: \t\t" + str(nineth_digit))
    print("Calculated check digit: " + str(result))
  elif plausibilty == False:
    print('ERROR: \tThe current VIN has more or less than 17 digits. \
                  \nThe maximum number of digits is 17.')
