"""
Exercise No. 08

Write a program that creates a histogram as a dictionary of the following values:

    items = ['x', 'y', 'z', 'y', 'x', 'y', 'y', 'z', 'x']

In response print histogram to the console.

Expected result:

    {'x': 3, 'y': 4, 'z': 2}
"""

# Solution I
items = ['x', 'y', 'z', 'y', 'x', 'y', 'y', 'z', 'x']
result = {}
for i in items:
    if i not in result:
        result[i] = 1
    else:
        result[i] += 1
print(result)


# Solution II
items = ['x', 'y', 'z', 'y', 'x', 'y', 'y', 'z', 'x']
freq = {}
for item in items:
    if item not in freq.keys():
        freq[item] = 1
    else:
        freq[item] += 1
print(freq)
