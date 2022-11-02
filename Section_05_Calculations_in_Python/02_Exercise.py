"""
Exercise No. 02

Write a program that calculates the future value of 1000 USD with an annual interest rate of 3%, annual capitalization
and a 5-year investment period. Round the result to the nearest cent.

Tip: Use compound interest capitalization formula.

Print the result to the console as shown below.

Expected result:

    The future valueof the investment: 1159.27 USD
"""

# Solution I
fv = 1000 * (1 + 0.03) ** 5
print(f'The future value of the investment: {fv:.2f} USD')


# Solution II
pv = 1000
r = 0.03
n = 5
fv = pv * (1 + r) ** n

print(f'The future value of the investment: {fv:.2f} USD')
