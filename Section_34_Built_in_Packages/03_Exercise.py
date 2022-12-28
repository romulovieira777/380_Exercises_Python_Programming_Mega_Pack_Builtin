"""
Exercise No. 03

Using the datetime built-in module, calculate the difference for dates (date 2 - date 1):

    - date 1: 2020-06-01
    - date 2: 2020-07-18

Print the result to the console as shown below.

Expected result:

    47 days, 0:00:00
"""
import datetime

# Solution I
date_1 = datetime.date(2020, 6, 1)
date_2 = datetime.date(2020, 7, 18)
print(date_2 - date_1)


# Solution II
date_1 = datetime.datetime(2020, 6, 1)
date_2 = datetime.datetime(2020, 7, 18)
diff = date_2 - date_1
print(diff)
