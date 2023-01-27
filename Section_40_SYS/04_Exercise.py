"""
Exercise No. 04

Do this exercise in the command line.

Using the built-in sys module create a script called example.py that calculates the sum of the first two arguments.

Example:
    $ python example.py 24 6
    30
"""
import sys

if len(sys.argv) > 2:
    result = int(sys.argv[1]) + int(sys.argv[2])
    print(result)
