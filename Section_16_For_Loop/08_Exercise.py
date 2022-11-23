"""
Exercise No. 08

Write a program that creates a histogram as a dictionary of the following values:

    items = ['x', 'y', 'z', 'y', 'x', 'y', 'y', 'z', 'x']

In response print histogram to the console.

Expected result:

    {'x': 3, 'y': 4, 'z': 2}
"""
items = ['x', 'y', 'z', 'y', 'x', 'y', 'y', 'z', 'x']
result = {}
for i in items:
    if i not in result:
        result[i] = 1
    else:
        result[i] += 1
print(result)
