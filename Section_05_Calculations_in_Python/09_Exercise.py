"""
Exercise No. 09

Find the roots of the quadratic equation:

    x^2 + 5x + 4 = 0

Print the result to the console as shown below.

Expected result:

    x1 = -4.0
    x2 = -1.0
"""

# Solution I
x1 = (-5 + (5 ** 2 - 4 * 1 * 4) ** 0.5) / (2 * 1)
x2 = (-5 - (5 ** 2 - 4 * 1 * 4) ** 0.5) / (2 * 1)

print(f'x1 = {x2}\nx2 = {x1}')


# Solution II
a = 1
b = 5
c = 4

delta = b ** 2 - 4 * a * c
delta_sqrt = delta ** 0.5

x1 = (-b - delta_sqrt) / (2 * a)
x2 = (-b + delta_sqrt) / (2 * a)

print(f'x1 = {x1}\nx2 = {x2}')
