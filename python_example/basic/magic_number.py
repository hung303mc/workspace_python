#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
magic_number - Check if the given number contains a magic digit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Prompt user for a number, and check if the number contains a magic digit.
 
Usage: magic_number.py
"""
def isMagic(number:int, magicDigit:int = 8) -> bool:
    """Check if the given number contains the digit magicDigit.
    Arguments:
    number - positive int only
    magicDigit - single-digit int (default is 8)
    """
    while number > 0:
        # extract and drop each digit
        if number % 10 == magicDigit:
            return True     # break loop
        else:
            number //= 10   # integer division
 
    return False
 
def isMagicStr(numberStr:str, magicDigit:str = '8') -> bool:
    """Check if the given number string contains the magicDigit
    Arguments:
    numberStr - a numeric str
    magicDigit - a single-digit str (default is '8')
    """
    return magicDigit in numberStr  # Use built-in sequence operator 'in'
 
def main():
    """The main function"""
    # Prompt and read input string as int
    numberIn = int(input('Enter a number: '))
 
    # Use isMagic()
    if isMagic(numberIn):
        print('{} is a magic number'.format(numberIn))
    else:
        print('{} is NOT a magic number'.format(numberIn))
 
    # Use isMagicStr()
    if isMagicStr(str(numberIn), '9'):
        print('{} is a magic number'.format(numberIn))
    else:
        print('{} is NOT a magic number'.format(numberIn))
 
# Run the main function
if __name__ == '__main__':
    main()