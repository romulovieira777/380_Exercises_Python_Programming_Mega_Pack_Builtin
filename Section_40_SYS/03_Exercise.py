"""
Exercise No. 02

Do this exercise in the command line.

Using the sys built-in module create a script that prints all arguments passed to the console while calling the script(
each argument on a separate line).

Example:
    $ python example.py arg1 arg2 arg3
    arg1
    arg2
    arg3
"""
import sys

for arg in sys.argv:
    print(arg)
