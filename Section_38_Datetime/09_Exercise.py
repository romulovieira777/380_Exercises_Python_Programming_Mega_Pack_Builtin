"""
Exercise No. 09

Using the built-in datetime module, calculate the exact time remaining until the end of the current year.

Expected result:
    'Until the end of the year: x'

The value of x will vary depending on the time taken to complete the exercise.

For example, for the date: 2020-07-21 07:39:39.188939 the return value should be:
    'Until the end of the year: 162 days, 16:20:20.811061'
"""
import datetime

# Solution I
today = datetime.datetime.today()
end_of_year = datetime.datetime(today.year, 12, 31, 23, 59, 59, 999999)
diff = end_of_year - today
print("Until the end of the year:", diff)


# Solution II
now = datetime.datetime.now()
end_of_year = datetime.datetime(now.year + 1, 1, 1)
diff = end_of_year - now
print(f'Until the end of the year: {diff}')
