"""
Exercise No. 11

Using the random built-in module set the random seed as follows:

    random.seed(12)

And select randomly (pseudo-randomly) an item from the list below:

    items = ['python', 'java', 'sql', 'c++', 'c']

Print the result to the console.

Expected result:

    c++
"""
import random

items = ['python', 'java', 'sql', 'c++', 'c']

# Solution I
random.seed(12)
print(random.choice(items))


# Solution II
random.seed(12)
choice = random.choice(items)
print(choice)
