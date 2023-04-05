"""
Exercise No. 05

Consider the compound capitalization model, where:

    - pv - is the present value of the investment
    - r - is rate (annual)
    - n - the number of years of investment
    - m - number of capitalization periods during the year (default 1)

A function fv() was implemented to calculate the future value of investment depending on the number of capitalization
periods during the year (m parameter default 1):

    def fv(pv, r, n, m=1):
        return round(pv * (1 + (r / m)) ** (n * m), 2)

Using the built-in functools module, the class partial and the fv() function create the function annual_acc_factor(),
which calculates the annual accumulation factor.

In response, print of the annual accumulation factor for the following cases:

    - 4% (annual) interest rate and annual capitalization
    - 4% (annual) interest rate and quarterly capitalization
    - 6% (annual) interest rate and monthly capitalization

Expected result:

    1.04
    1.04060401
    1.0616778118644983
"""
from functools import partial


def fv(rate, m, n, pv):
    return pv * (1 + (rate / m)) ** (n * m)


annual_acc_factor = partial(fv, n=1, pv=1)

print(annual_acc_factor(0.04, 1))
print(annual_acc_factor(0.04, 4))
print(annual_acc_factor(0.06, 12))
