#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
htmlescape - Escape the given html file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Replace the HTML reserved characters by their corresponding HTML entities.
    " is replaced with &quot;
    & is replaced with &amp;
    < is replaced with &lt;
    > is replaced with &gt;
 
Usage: htmlescape.py infile outfile
"""
import sys   # Using sys.argv and sys.exit()
# Check if infile and outfile are given in the command-line arguments
if len(sys.argv) != 3:
    print('Usage: ./htmlescape.py infile outfile')
    sys.exit(1)  # Return a non-zero value to indicate abnormal termination
 
# The "with-as" closes the files automatically upon exit.
with open(sys.argv[1]) as infile, open(sys.argv[2], 'w') as outfile:
    for line in infile:       # Process each line (including newline)
        line = line.rstrip()  # strip trailing (right) white spaces
 
        # Encode HTML &, <, >, ".  The order of substitution is important!
        line = line.replace('&', '&amp;')  # Need to do first as the rest uses it
        line = line.replace('<', '&lt;')
        line = line.replace('>', '&gt;')
        line = line.replace('"', '&quot;')
        outfile.write('%s\n' % line)   # write() does not output newline