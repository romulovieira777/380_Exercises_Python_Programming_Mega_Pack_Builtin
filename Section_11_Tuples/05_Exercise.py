"""
Exercise No. 05

Sort the given tuple (from A to Z):

    names = ('Monica', 'Tom', 'John', 'Michael')

Print the result to the console as shown below.

Expected result:

    ('John', 'Michael', 'Monica', 'Tom')
"""
names = ('Monica', 'Tom', 'John', 'Michael')

names = sorted(names)
print(tuple(names))
