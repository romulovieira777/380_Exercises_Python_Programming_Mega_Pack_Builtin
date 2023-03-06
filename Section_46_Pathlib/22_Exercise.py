"""
Exercise No. 22

The README.md file from the pandas library is given. Using the built-in pathlib module, load this file. Then display all
lines from the README.md file containing the header (the line beginning with '#') to the console.

Tip:

    # >>> help(pathlib.Path.open)

    Help on function open in module pathlib:

    open(self, mode='r', buffering=-1, encoding=None, errors=None, newline=None)
        Open the file pointed by this path and return a file object, as
        the built-in open() function does.

Expected result:

    # pandas: powerful Python data analysis toolkit
    ## What is it?
    ## Main Features
    ## Where to get it
    # conda
    # or PyPI
    ## Dependencies
    ## Installation from sources
    ## License
    ## Documentation
    ## Background
    ## Getting Help
    ## Discussion and Development
    ## Contributing to pandas [![Open Source Helpers](https://www.codetriage.com/pandas-dev/pandas/badges/users.svg)](https://www.codetriage.com/pandas-dev/pandas)
"""
from pathlib import Path

# Solution I
path = Path.cwd() / '../Files/README.md'

with path.open() as f:
    for line in f:
        if line.startswith('#'):
            print(line, end='')


# Solution II
path = Path.cwd() / '../Files/README.md'

with path.open('r') as file:
    headers = [line.strip() for line in file if line.startswith('#')]

print('\n'.join(headers))
