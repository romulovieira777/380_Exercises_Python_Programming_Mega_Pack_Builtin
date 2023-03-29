"""
Exercise No. 26

The following list is given:

    values = [(44, 7), (57, 6), (10, 3)]

Using the built-in itertools module and the starmap class create an iterator that allows iterating over the remainder
values of dividing the first value of each tuple by the second.

In response, print all elements of the results iterator to the console as shown below.

Tip:

    #>>> help(itertools.starmap)

    Help on class starmap in module itertools:

    class starmap(builtins.object)
        |  starmap(function, iterable, /)
        |
        |  Return an iterator whose values are returned from the function evaluated with an argument tuple taken from
           the given sequence.

Expected result:

    2
    3
    1
"""
import itertools

values = [(44, 7), (57, 6), (10, 3)]

for value in itertools.starmap(lambda x, y: x % y, values):
    print(value)
