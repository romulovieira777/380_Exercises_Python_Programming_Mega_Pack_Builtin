"""
Exercise No. 10

Implement a function is_distinct() to check if the list contains unique values.

Example:

    [IN]: is_distinct([1, 2, 3])
    [OUT]: True

    [IN]: is_distinct([1, 2, 3, 3])
    [OUT]: False

Note! You only need to define the function.
"""


# Solution I
def is_distinct(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                return False
    return True


print(is_distinct([1, 2, 3]))
print(is_distinct([1, 2, 3, 3]))


# Solution II
def is_distinct(lst):
    return len(lst) == len(set(lst))


print(is_distinct([1, 2, 3]))
print(is_distinct([1, 2, 3, 3]))
