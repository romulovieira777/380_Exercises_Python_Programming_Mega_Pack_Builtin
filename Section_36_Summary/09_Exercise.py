"""
Exercise No. 09

Implement a function called concat() that accepts two lists in the format given below:

    l1 = [[1], [2]]
    l2 = [[3], [4]]

and returns:

    [[1, 3], [2, 4]]

Note: You only need to implement this function.
"""


# Solution I
def concat(l1, l2):
    return [[l1[i][j], l2[i][j]] for i in range(len(l1)) for j in range(len(l1[i]))]


print(concat([[1], [2]], [[3], [4]]))


# Solution II
def concat(l1, l2):
    result = []
    for i, j in zip(l1, l2):
        result.append([i[0], j[0]])
    return result


print(concat([[1], [2]], [[3], [4]]))
