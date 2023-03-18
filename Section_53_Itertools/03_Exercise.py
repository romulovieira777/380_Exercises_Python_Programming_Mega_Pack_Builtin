"""
Exercise No. 03

Using the built-in itertools module and the cycle class create an iterator that allows you to iterate cyclically on the
following values -1, 0, 1. Then using a loop display the first 15 elements of the iterator to the console.

Tip:

    #>>> help(itertools.cycle)

    Help on class cycle in module itertools:

    class cycle(builtins.object)
     |  cycle(iterable, /)
     |
     |  Return elements from the iterable until it is exhausted. Then repeat the sequence indefinitely.

Expected result:

    -1
    0
    1
    -1
    0
    1
    -1
    0
    1
    -1
    0
    1
    -1
    0
    1
"""
import itertools

# Solution I
counter = itertools.cycle([-1, 0, 1])

for i in range(15):
    print(next(counter))


# Solution II
cycle = itertools.cycle([-1, 0, 1])

results = [next(cycle) for i in range(15)]

for result in results:
    print(result)
