"""
Exercise No. 04

Implement a function map_longest() that accepts the list of words and returns the length of the longest word in this
list.

Example:

    [IN]: map_longest(['Python', 'sql'])
    [OUT]: 6

    [IN]: map_longest(['java', 'sql', 'r'])
    [OUT]: 4

Note! You only need to define the function.
"""


# Solution I
def map_longest(words):
    longest = 0
    for word in words:
        if len(word) > longest:
            longest = len(word)
    return longest


print(map_longest(['Python', 'sql']))


# Solution II
def map_longest(words):
    lengths = []
    for word in words:
        lengths.append(len(word))
    return max(lengths)


print(map_longest(['Python', 'sql']))
