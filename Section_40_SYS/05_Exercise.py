"""
Exercise No. 05

Do this exercise in the command line.

Using the built-in sys module create a script called calculate.py, which calculates the arithmetic mean (round the
result to four decimal places) of the arguments passed. In case the user doesn't provide any argument, the script
returns the following information:
    'No values were given'

Examples:
    $ python calculate.py 5 9 4
    Average: 6.0000

    $ python calculate.py
    No values were given
"""
import sys

# Solution I
if len(sys.argv) > 1:
    result = sum([int(arg) for arg in sys.argv[1:]]) / len(sys.argv[1:])
    print(f'Average: {result:.4f}')
else:
    print('No values were given')


# Solution II
if len(sys.argv) > 1:
    values = [int(value) for value in sys.argv[1:]]
    result = sum(values) / len(values)
    print(f'Average: {result:.4f}')
else:
    print('No values were given.')
