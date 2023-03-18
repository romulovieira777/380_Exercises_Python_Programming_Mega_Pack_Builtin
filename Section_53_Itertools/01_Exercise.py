"""
Exercise No. 01

Using the built-in itertools module and the count class create an iterator that allows you to return sucessive natural
numbers (start from zero). Then using a loop display the first 10 elements of the iterator to the console.

Tip:

    #>>> help(itertools.count)

    Help on class count in module itertools:

    class count(builtins.object)
     |  count(start=0, step=1)
     |
     |  Return a count object whose .__next__() method returns consecutive values.

Expected result:

    0
    1
    2
    3
    4
    5
    6
    7
    8
    9
"""
import itertools

# Solution I
counter = itertools.count()

for i in range(10):
    print(next(counter))


# Solution II
counter = itertools.count()

for i in counter:
    if i > 9:
        break
    print(i)
