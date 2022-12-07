"""
Exercise No. 09

Implement a function remove_duplicates() that removes duplicates from the list (the order of the items in the list does
not have to be kept).

Example:

    [IN]: remove_duplicates([1, 5, 3, 2, 2, 4, 2, 4])
    [OUT]: [1, 2, 3, 4, 5]

    [IN]: remove_duplicates([1, 1, 1, 1])
    [OUT]: [1]

Note! You only need to define the function.
"""


# Solution I
def remove_duplicates(lst):
    lst.sort()
    for i in range(len(lst) - 1, 0, -1):
        if lst[i] == lst[i - 1]:
            lst.pop(i)
    return lst


print(remove_duplicates([1, 5, 3, 2, 2, 4, 2, 4]))
print(remove_duplicates([1, 1, 1, 1]))


# Solution II
def remove_duplicates(lst):
    return list(set(lst))


print(remove_duplicates([1, 5, 3, 2, 2, 4, 2, 4]))
print(remove_duplicates([1, 1, 1, 1]))
