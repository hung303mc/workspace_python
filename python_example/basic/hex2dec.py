#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
hex2dec - hexadecimal to decimal conversion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Prompt user for a hex string, and print its decimal equivalent
This example illustrates for-loop with index, nested-if, string operations and dictionary.
 
Usage: hex2dec.py
"""
import sys   # Using sys.exit()
 
dec = 0   # Accumulating from each hex digit
dictHex2Dec = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}  # lookup table for hex to dec
 
# Prompt and read hex string
hexStr = input('Enter a hex string: ')
 
# Process each hex digit from the left (most significant digit)
for hexDigitIdx in range(len(hexStr)):  # hexDigitIdx = 0, 1, 2, ..., len()-1
    hexDigit = hexStr[hexDigitIdx]      # Extract each 1-character string
    hexExpFactor = 16 ** (len(hexStr) - 1 - hexDigitIdx)  # ** for power or exponent
    if '1' <= hexDigit <= '9':   # Python supports chain comparison
       dec += int(hexDigit) * hexExpFactor
    elif hexDigit == '0':
       pass   # Need a dummy statement for do nothing
    elif 'A' <= hexDigit <= 'F':
       dec += (ord(hexDigit) - ord('A') + 10) * hexExpFactor  # ord() returns the Unicode number
    elif 'a' <= hexDigit <= 'f':
       dec += dictHex2Dec[hexDigit] * hexExpFactor  # Look up from dictionary
    else:
       print('error: invalid hex string')
       sys.exit(1)   # Return a non-zero value to indicate abnormal termination
 
print('The decimal equivalent for hex "{}" is: {}'.format(hexStr, dec))   # Formatted output
# Using built-in function int(str, radix)
print('The decimal equivalent for hex "{}" using built-in function is: {}'.format(hexStr, int(hexStr, 16)))