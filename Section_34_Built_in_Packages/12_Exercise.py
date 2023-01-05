"""
Exercise No. 12

Using the random built-in module set the random seed as follows:

    random.seed(15)

And shuffle (pseudo-randomly) items in the following list:

    items = ['python', 'java', 'sql', 'c++', 'c']

In response, print the list to the console.

Expected result:

    ['c++', 'c', 'sql', 'java', 'python']
"""
import random

items = ['python', 'java', 'sql', 'c++', 'c']

random.seed(15)
random.shuffle(items)
print(items)
