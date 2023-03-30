"""
Exercise No. 29

The following list is given:

    data = [1, 5, 3, 4, 6, 9, 3]

Using the built-in itertools module and the groupby class, group the data (properly sort the data before grouping) into
even numbers (key 'even') and odd numbers (key 'odd').

In response, print the keys and the group of numbers assigned to the appropriate key as shown below.

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

    even -> [4, 6]
    odd -> [1, 5, 3, 9, 3]
"""
import itertools

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]

func = lambda x: 'even' if x % 2 == 0 else 'odd'
sorted_data = sorted(data, key=func)
grouped_data = itertools.groupby(sorted_data, key=func)

for key, group in grouped_data:
    print(f'{key} -> {list(group)}')
