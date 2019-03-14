#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""
files_rename - Rename files in the directory using regex
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Rename all the files in the given directory (default to the current directory)
  matching the regular expression from_regex by to_regex.
 
Usage: files_rename.py from_regex to_regex [dir|.]
Eg. Rename '.txt' to '.bak' in the current directory:
$ ./files_rename.py '\.txt' '.bak'
 
Eg. Rename files ending with '.txt' to '.bak' in directory '/temp'
$ ./files_rename.py '\.txt$' '.bak' '/temp'
 
Eg. Rename 0 to 9 with _0 to _9 via back reference in the current directory:
$ ./files_rename.py '([0-9])' '_\1'
"""
import sys   # Using sys.argv, sys.exit()
import os    # Using os.chdir(), os.listdir(), os.path.isfile(), os.rename()
import re    # Using re.sub()
 
if not(3 <= len(sys.argv) <= 4):  # logical operators are 'and', 'or', 'not'
    print('Usage: ./files_rename.py from_regex to_regex [dir|.]')
    sys.exit(1)    # Return a non-zero value to indicate abnormal termination
 
# Change directory if given
if len(sys.argv) == 4:
   dir = sys.argv[3]
   os.chdir(dir)     # change current working directory
 
count = 0  # count of files renamed
for oldFilename in os.listdir():      # list current directory, non-recursive
    if os.path.isfile(oldFilename):   # file only (not directory)
        newFilename = re.sub(sys.argv[1], sys.argv[2], oldFilename)
        if oldFilename != newFilename:
            count += 1  # Update count
            os.rename(oldFilename, newFilename)
            print(oldFilename, '->', newFilename)  # Print results

print("Number of files renamed:", count)