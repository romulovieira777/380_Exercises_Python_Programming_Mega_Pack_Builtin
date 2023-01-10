"""
Exercise No. 05

The following list is given:

    items = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

Implement a function called flatten(), which takes the nested list and returns the following:

    [1, 2, 3, 4, 5, 6, 7, 8, 9]

Note: You only need to implement this function.
"""


# Solution I
def flatten(items):
    return [item for sublist in items for item in sublist]


# Solution II
def flatten(items):
    result = []
    for item in items:
        result.extend(item)
    return result
