"""
Exercise No. 07

The following dictionary is given:

    data = dict(zip(('a', 'b', 'c', 'd', 'e', 'f'), (1, 2, 3, 4, 5, 6)))

Convert this dictionary into the following list and print the result to the console.

Expected result:

    [['a', 1], ['b', 2], ['c', 3], ['d', 4], ['e', 5], ['f', 6]]
"""
# Solution I
data = dict(zip(('a', 'b', 'c', 'd', 'e', 'f'), (1, 2, 3, 4, 5, 6)))
print([[key, value] for key, value in data.items()])


# Solution II
data = dict(zip(('a', 'b', 'c', 'd', 'e', 'f'), (1, 2, 3, 4, 5, 6)))
result = [[key, value] for key, value in data.items()]
print(result)
