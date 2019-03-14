#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
wc - word count
~~~~~~~~~~~~~~~
Read a file given in the command-line argument and print the number of
  lines, words and characters - similar to UNIX's wc utility.
 
Usage: wc.py filename
"""
 
# Check if a filename is given in the command-line arguments using "sys" module
import sys              # Using sys.argv and sys.exit()
if len(sys.argv) != 2:  # Command-line arguments are kept in a list sys.argv
    print('Usage: ./wc.py filename')
    sys.exit(1)         # Return a non-zero value to indicate abnormal termination
 
# You do not need to declare the name and type of variables.
# Variables are created via the initial assignments.
num_words = num_lines = num_chars = 0  # chain assignment
 
# Get input file name from list sys.argv
# sys.argv[0] is the script name, sys.argv[1] is the filename.
with open(sys.argv[1]) as infile: # 'with-as' closes the file automatically
    for line in infile:           # Process each line (including newline) in a for-loop
        num_lines += 1            # No ++ operator in Python?!
        num_chars += len(line)
        line = line.strip()       # Remove leading and trailing whitespaces
        words = line.split()      # Split into a list using whitespace as delimiter
        num_words += len(words)
 
# Various ways of printing results
print('Number of Lines is', num_lines)                 # Items separated by blank
print('Number of Words is: {0:5d}'.format(num_words))  # new formatting style
print('Number of Characters is: %8.2f' % num_chars)    # old formatting style

# Invoke Unix utility 'wc' through shell command for comparison
from subprocess import call     # Python 3
call(['wc', sys.argv[1]])       # Command in a list

import os                       # Python 2
os.system('wc ' + sys.argv[1])  # Command is a str