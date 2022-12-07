"""
Exercise No. 08

Implement a function count_str(), which returns the number of str objects with a length more than 2 characters from an
iterable object (list, tuple, set).

Example:

    [IN]: count_str([1, '#hello', '', 'go'])
    [OUT]: 2

    [IN]: count_str([1, 2, 3, 'python'])
    [OUT]: 1

Note! You only need to define the function.
"""


# Solution I
def count_str(iterable):
    count = 0
    for i in iterable:
        if type(i) == str and len(i) > 2:
            count += 1
    return count


print(count_str([1, '#hello', '', 'go']))
print(count_str([1, 2, 3, 'python']))


# Solution II
def count_str(iterable):
    count = 0
    for item in iterable:
        if isinstance(item, str) and len(item) > 2:
            count += 1
    return count


print(count_str([1, '#hello', '', 'go']))
print(count_str([1, 2, 3, 'python']))


# Solution III
def count_str(iterable):
    total = 0
    for item in iterable:
        if isinstance(item, str):
            if len(item) > 2:
                total += 1
    return total


print(count_str([1, '#hello', '', 'go']))
print(count_str([1, 2, 3, 'python']))
