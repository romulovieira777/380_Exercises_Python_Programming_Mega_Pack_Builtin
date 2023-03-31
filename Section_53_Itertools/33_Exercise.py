"""
Exercise No. 33

The following list is given:

    data = [
        {'user': '0032', 'level': 70},
        {'user': '0034', 'level': 74},
        {'user': '0233', 'level': 71},
        {'user': '0532', 'level': 70},
        {'user': '0634', 'level': 74},
        {'user': '0245', 'level': 70},
        {'user': '0235', 'level': 70},
        {'user': '0255', 'level': 71},
]

Using the built-in module itertools and the groupby class, group users by 'level' values.

In response, print the keys and user groups belonging to the appropriate key as shown below.

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

    70 -> [{'user': '0032', 'level': 70}, {'user': '0532', 'level': 70}, {'user': '0245', 'level': 70}, {'user': '0235', 'level': 70}]
    71 -> [{'user': '0233', 'level': 71}, {'user': '0255', 'level': 71}]
    74 -> [{'user': '0034', 'level': 74}, {'user': '0634', 'level': 74}]
"""
import itertools

data = [
    {'user': '0032', 'level': 70},
    {'user': '0034', 'level': 74},
    {'user': '0233', 'level': 71},
    {'user': '0532', 'level': 70},
    {'user': '0634', 'level': 74},
    {'user': '0245', 'level': 70},
    {'user': '0235', 'level': 70},
    {'user': '0255', 'level': 71},
]

func = lambda x: x['level']
sorted_data = sorted(data, key=func)
grouped_data = itertools.groupby(sorted_data, key=func)

for key, group in grouped_data:
    print(f'{key} -> {list(group)}')
