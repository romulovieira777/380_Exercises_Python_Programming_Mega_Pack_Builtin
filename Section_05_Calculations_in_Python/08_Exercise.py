"""
Exercise No. 08

Calculate the distance of two points A = (3, 2), B = (-1, -1) and print result to the console as shown below.

Expected result:

    The distance between two points A and B: 5.0
"""

# Solution I
a = (3, 2)
b = (-1, -1)
d = ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

print(f'The distance between points A and B: {d}')


# Solution II
a1 = 3
a2 = 2
b1 = -1
b2 = -1
distance = ((b1 - a1) ** 2 + (b2 - a2) ** 2) ** (1 / 2)

print(f'The distance between points A and B: {distance}')
