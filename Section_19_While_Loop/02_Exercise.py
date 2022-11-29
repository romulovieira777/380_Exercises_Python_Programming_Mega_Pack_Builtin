"""
Exercise No. 02

Using the while loop, calculate how many years you have to wait for the return on the investiment described below to at
least double your money (we only take into account full periods).

Description:

    n = number of periods (in years)
    pv - present value
    r - interest rate (annual)
    fv - future value

Ivestment paramenters:

    pv = 1000
    r = 0.04

Print result to the console as shown below.

Expected result:

    Future value: 2025.82 USD. Number of periods: 18 years
"""
n = 1
pv = 1000
r = 0.04
fv = pv * (1 + r)

while fv < 2 * pv:
    fv = fv * (1 + r)
    n += 1
print(f'Future value: {fv:.2f} USD. Number of periods: {n} years')
