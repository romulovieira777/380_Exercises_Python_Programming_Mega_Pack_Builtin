"""
Exercise No. 05

The following text is given:

    text = "python programming - introduction"

Using the built-in collections module and the Counter class calculate the three most common characters in the given text.
Print the result as shown below.

Tip:
    #>>> help(Counter.most_common)

    Help on function most_common in module collections:

    most_common(self, n=None)
        List the n most common elements and their counts from the most
        common to the least.  If n is None, then list all element counts.

        #>>> Counter('abcdeabcdabcaba').most_common(3)
        [('a', 5), ('b', 4), ('c', 3)]

Expected result:

    [('o', 4), ('n', 4), ('t', 3)]
"""
from collections import Counter

text = "python programming - introduction"

counter = Counter(text)
print(counter.most_common(3))
