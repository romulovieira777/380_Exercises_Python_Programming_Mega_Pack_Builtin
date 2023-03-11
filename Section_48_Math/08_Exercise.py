"""
Exercise No. 08

Consider the continuous capitalization model of interest. The future value in this model can be calculated as follows:

    fv = pv . e ** (r * n)

where:

    - FV - future value - the future value of investments
    - PV - present value - present value of the investment
    - e - Euler's number
    - r - interest rate (annual)
    - n - number of years

By transforming the above formula, we get:

    n = 1 / r * ln(fv / pv)

which allows you to determine the number of periods.

Using the built-in math module determine after how many years the amount invested in the model of continuous interest
capitalization at an annual interest rate of 4% will at least double its value. Round the result to full years and print
it to the console as shown below.

Tip:

    # >>> help(math.log)

    Help on built-in function log in module math:

    log(...)
        log(x[, base])

    Return the logarithm of x to the given base.
    If the base not specified, returns the natural logarithm (base e) of x.


    # >>> help(math.ceil)

    Help on built-in function ceil in module math:

    ceil(...)
        ceil(x)

        Return the ceiling of x as an Integral.
        This is the smallest integer >= x.

Expected result:

    n = 18
"""
import math

# Solution I
n = 1 / 0.04 * math.log(2)
n = math.ceil(n)

print(f"n = {n}")


# Solution II
pv = 1
fv = 2
r = 0.04

n = math.ceil((1 / r) * math.log(fv / pv))

print(f"n = {n}")
