"""
Exercise No. 02

The following target list is given:
    target = ['yes', 'no', 'no', None, 'yes', 'yes', 'no', 'yes']

Using the built-in collections module create a Counter class object from the given list. Print the result to the console.

Tip:
    # >>> help(Counter)

    Help on class Counter in module collections:

    class Counter(builtins.dict)
     |  Dict subclass for counting hashable items.  Sometimes called a bag
     |  or multiset.  Elements are stored as dictionary keys and their counts
     |  are stored as dictionary values.

Expected result:
    Counter({'yes': 4, 'no': 3, None: 1})
"""
from collections import Counter

target = ['yes', 'no', 'no', None, 'yes', 'yes', 'no', 'yes']

counter = Counter(target)
print(counter)
