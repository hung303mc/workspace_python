#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
dec2hex - decimal hexadecimal to conversion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Prompt user for a decimal number, and print its hexadecimal equivalent
 
Usage: dec2hex.py
"""
hexStr = ''   # To be accumulated
hexChars = [  # Use this list as lookup table for converting 0-15 to 0-9A-F
    '0','1','2','3', '4','5','6','7', '8','9','A','B', 'C','D','E','F'];
 
# Prompt and read decimal number
dec = int(input('Enter a decimal number: '))  # positive int only
decSave = dec  # We will destroy dec
 
# Repeated modulus/division and get the hex digits in reverse order
while dec > 0:
    hexDigit = dec % 16;   # 0-15
    hexStr = hexChars[hexDigit] + hexStr;  # Append in front corresponds to reverse order
    dec = dec // 16;       # Integer division
 
print('The hex for decimal {} is: {}'.format(decSave, hexStr))   # Formatted output
# Using built-in function hex(decNumber)
print('The hex for decimal {} using built-in function is: {}'.format(decSave, hex(decSave)))