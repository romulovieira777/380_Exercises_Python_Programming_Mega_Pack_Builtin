"""
Exercise No. 06

The quadratic equation is given with the following formula:

    x^2 + 5x + 4 = 0

Using Vieta's formulas calculate the sum and product of the roots of this quadratic equation. Print the result to the
console as shown below.

Expected result:

    x1 + x2 = -5.0
    x1x2 = 4.0
"""

# Solution I
x = 1
y = 5
z = 4

x1 = (-y + (y ** 2 - 4 * x * z) ** 0.5) / (2 * x)
x2 = (-y - (y ** 2 - 4 * x * z) ** 0.5) / (2 * x)

print(f'x1 + x2 = {x1 + x2}')
print(f'x1x2 = {x1 * x2}')


# Solution II
a = 1
b = 5
c = 4

sum = -b / a
product = c / a

print(f'x1 + x2 = {sum}\nx1x2 = {product}')
