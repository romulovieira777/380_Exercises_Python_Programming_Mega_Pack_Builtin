"""
Exercise No. 03

From the following text:

    string = '1 0 0 1 0 1'

Remove spaces using slicing. Then convert the result to decimal notation and print to the console as shown below.

Expected result:

    Number found: 37
"""

# Solution I
string = '1 0 0 1 0 1'
print('Number found: ' + str(int(string.replace(' ', ''), 2)))


# Solution II
string = '1 0 0 1 0 1'
binary = string[::2]
number = int(binary, 2)
print(f'Number found: {number}')
