"""
Exercise No. 02

Using the built-in datetime module, create time objects for the given hours:
    - 12:00:00
    - 6:00:00
    - 9:15:00

Then print these objects to the console.

Tip:
    #>>> help(datetime.time)

    Help on class time in module datetime:

    class time(builtins.object)
     |  time([hour[, minute[, second[, microsecond[, tzinfo]]]]]) --> a time object
     |
     |  All arguments are optional. tzinfo may be None, or an instance of
     |  a tzinfo subclass. The remaining arguments may be ints.

Expected result:
    12:00:00
    06:30:00
    09:15:00
"""
import datetime

time1 = datetime.time(12, 0, 0)
time2 = datetime.time(6, 30, 0)
time3 = datetime.time(9, 15, 0)

print(time1)
print(time2)
print(time3)
