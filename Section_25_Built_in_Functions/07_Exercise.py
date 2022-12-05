"""
Exercise No. 07

Count the number of ones in the binary representation of the number:

    number = 24

Print the result to the console.

Tip: Use the bin() built-in function.

Expected result:

    5
"""

# Solution I
number = 234
binary = bin(number)
binary = binary[2:]

print(binary.count('1'))


# Solution II
number = 234

print(bin(number).count('1'))
