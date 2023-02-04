"""
Exercise No. 02

The results of voting in two groups are given in the form of dictionaries:
    poll_1 = {'yes': 140, 'no': 120, NOne: 12}
    poll_2 = {'yes': 113, 'no': 132, None: 9}

The dictionary keys mean respectively:
    - 'yes - vote for keys
    - 'no' - vote for no
    - 'None' - invalid vote

Using the built-in collections module create two objects of the Counter class from the given dictionaries.

Then combine these objects into one and print to the console.

Tip:
    # >>> help(Counter)

    Help on class Counter in module collections:

    class Counter(builtins.dict)
     |  Dict subclass for counting hashable items.  Sometimes called a bag
     |  or multiset.  Elements are stored as dictionary keys and their counts
     |  are stored as dictionary values.

Expected result:
    Counter({'yes': 253, 'no': 252, None: 21})
"""
from collections import Counter

poll_1 = {'yes': 140, 'no': 120, None: 12}
poll_2 = {'yes': 113, 'no': 132, None: 9}

counter_1 = Counter(poll_1)
counter_2 = Counter(poll_2)

counter_1.update(counter_2)
print(counter_1)
