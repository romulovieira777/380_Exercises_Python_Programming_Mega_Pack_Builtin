"""
Exercise No. 02

Using the built-in itertools module and the cycle class create an iterator that allows you to return positive odd
numbers. Then using a loop display the first 5 elements of the iterator to the console.

Tip:

    #>>> help(itertools.count)

    Help on class count in module itertools:

    class count(builtins.object)
     |  count(start=0, step=1)
     |
     |  Return a count object whose .__next__() method returns consecutive values.

Expected result:

    1
    3
    5
    7
    9
"""
import itertools

# Solution I
counter = itertools.cycle([1, 3, 5, 7, 9])

for i in range(5):
    print(next(counter))


# Solution II
counter = itertools.count(start=1, step=2)

for i in counter:
    if i > 9:
        break
    print(i)
