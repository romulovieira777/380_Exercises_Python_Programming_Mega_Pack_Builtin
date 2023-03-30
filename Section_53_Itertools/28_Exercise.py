"""
Exercise No. 28

The following list is given:

    data = [1, 5, 3, 4, 6, 9, 3]

Using the built-in itertools module and the groupby class, try to group the data into even numbers (key 'even') and odd
numbers (key 'odd') without sorting the data first.

In response, print the keys and the group of numbers assigned to the appropriate key to the console as shown below.

Note that without sorting the grouping doesn't work as it should.

Tip:

    #>>> help(itertools.groupby)

    Help on class groupby in module itertools:

    class groupby(builtins.object)
        |  groupby(iterable, key=None)
        |
        |  make an iterator that returns consecutive keys and groups from the iterable
        |
        |  iterable
        |    Elements to divide into groups according to the key function.
        |  key
        |    A function for computing the group category for each element.
        |    If the key function is not specified or is None, the element itself
        |    is used for grouping.

Expected result:

    odd -> [1, 5, 3]
    even -> [4, 6]
    odd -> [9, 3]
"""
import itertools

data = [1, 5, 3, 4, 6, 9, 3]

for key, group in itertools.groupby(data, lambda x: 'odd' if x % 2 else 'even'):
    print(f'{key} -> {list(group)}')
