"""
Exercise No. 02

Implement a generator called enum() that works just like the enumerate() built-in function.

For simplicity, the function gets an iterable object and returns a tuple (index, element).

Example:

    [IN]: list(enum(['TEN', 'CDR', 'BBT']))
    [OUT]: [(0, 'TEN'), (1, 'CDR'), (2, 'BBT')]

Note! All you have to do is define a generator.
"""


def enum(iterable):
    index = 0
    for element in iterable:
        yield index, element
        index += 1


print(list(enum(['TEN', 'CDR', 'BBT'])))
