"""
Exercise No. 03

Consider the compound annual capitalization model, where:

    - pv - is the present value of the investment
    - r - is rate (annual)
    - n - the number of years of investment

Implement a function called fv() that calculates the future value of investment rounded to two decimal places.

In response, print the future values of investment for the following cases:

    - pv=1000, r=0.04, n=1
    - pv=1000, r=0.04, n=2
    - pv=1000, r=0.03, n=5
    - pv=10000, r=0.09, n=10

Expected result:

    1040.0
    1081.6
    1159.27
    23673.64
"""


def fv(pv, r, n):
    return round(pv * (1 + r) ** n, 2)


print(fv(1000, 0.04, 1))
print(fv(1000, 0.04, 2))
print(fv(1000, 0.03, 5))
print(fv(10000, 0.09, 10))
