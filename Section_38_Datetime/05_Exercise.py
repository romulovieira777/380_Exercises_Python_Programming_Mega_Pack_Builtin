"""
Exercise No. 05

Using the built-in datetime module, determine the exact time elapsed between the dates:
    - Jul 20 2020 11:30:00
    - 2021-02-20 10:25:00

Then print the result to the console.

Expected result:
    214 days, 22:55:00
"""
import datetime

# Solution I
datetime1 = datetime.datetime(2020, 7, 20, 11, 30, 0)
datetime2 = datetime.datetime(2021, 2, 20, 10, 25, 0)

diff = datetime2 - datetime1

print(diff)


# Solution II
d1 = datetime.datetime(2020, 7, 20, 11, 30, 0)
d2 = datetime.datetime(2021, 2, 20, 10, 25, 0)
print(d2 - d1)
