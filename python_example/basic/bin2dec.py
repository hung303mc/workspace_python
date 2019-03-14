#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
bin2dec - binary to decimal conversion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Prompt user for a binary string, and print its decimal equivalent
 
Usage: bin2dec.py
"""
def validate(binStr:str) -> bool:
    """Check if the given str is a binary string (containing '0' and '1' only)"""
    for ch in binStr:
        if not(ch == '0' or ch == '1'): return False
 
    return True
 
def convert(binStr:str) -> int:
    """Convert the binary string into its equivalent decimal"""
    dec = 0  # Accumulate from each bit
 
    # Process each bit from the left (most significant digit)
    for bitIdx in range(len(binStr)):  # bitIdx = 0, 1, 2, ..., len()-1
        bit = binStr[bitIdx]
        if bit == '1':
            dec += 2 ** (len(binStr) - 1 - bitIdx)  # ** for power
 
    return dec
 
def main():
    """The main function"""
    # Prompt and read binary string
    binStr = input('Enter a binary string: ')
    if not validate(binStr):
        print('error: invalid binary string "{}"'.format(binStr))
    else:
        print('The decimal equivalent for binary "{}" is: {}'.format(binStr, convert(binStr)))
        # Using built-in function int(str, radix)
        print('The decimal equivalent for binary "{}" using built-in function is: {}'.format(binStr, int(binStr, 2)))
 
# Run the main function
if __name__ == '__main__':
    main()