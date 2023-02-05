"""
Exercise No. 04

The text is a follows:
    text = "python programming - introduction"

Using the built-in collections module and the Counter class find the distribution of characters in the given text
(create a Counter object). Print the result to the console.

Tip:
    #>>> help(Counter)

    Help on class Counter in module collections:

    class Counter(builtins.dict)
     |  Dict subclass for counting hashable items.  Sometimes called a bag
     |  or multiset.  Elements are stored as dictionary keys and their counts
     |  are stored as dictionary values.

Expected result:
    Counter({'o': 4, 'n': 4, 't': 3, ' ': 3, 'r': 3, 'i': 3, 'p': 2, 'g': 2, 'm': 2, 'y': 1, 'h': 1, 'a': 1, '-': 1,
             'd': 1, 'u': 1, 'c': 1})
"""
from collections import Counter

text = "python programming - introduction"

counter = Counter(text)
print(counter)
