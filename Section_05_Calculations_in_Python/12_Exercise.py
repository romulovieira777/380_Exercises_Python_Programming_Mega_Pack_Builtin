"""
Exercise No. 12

Calculate the standard deviation of the following set of data: 10, 11, 9.

Print the result to the console as shown below.

Expected result:

    The standard deviation: 0.82
"""

# Solution I
a = 10
b = 11
c = 9
n = 3
mean = (a + b + c) / n
variance = ((a - mean) ** 2 + (b - mean) ** 2 + (c - mean) ** 2) / n

std = variance ** 0.5

print(f'The standard deviation: {std:.2f}')


# Solution II
x1, x2, x3 = 10, 11, 9
mean = (x1 + x2 + x3) / 3
var = ((x1 - mean) ** 2 + (x2 - mean) ** 2 + (x3 - mean) ** 2) / 3
std = var ** 0.5

print(f'The standard deviation: {std:.2f}')
