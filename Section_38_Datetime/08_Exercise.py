"""
Exercise No. 08

using the built-in datetime module, calculate the number of days until the end of the current year.

Expected result:
    'Number of days until the end of the year: x'

The value of x will vary depending in the time taken to complete the exercise.
"""
import datetime

# Solution I
today = datetime.date.today()
end_of_year = datetime.date(today.year, 12, 31)
diff = end_of_year - today
print("Number of days until the end of the year:", diff.days)


# Solution II
today = datetime.date.today()
end_of_year = datetime.date(today.year, 12, 31)
diff = (end_of_year - today).days
print(f"Number of days until the end of the year: {diff}")
