"""
Exercise No. 01

From the given file name:

    filename = 'view.jpg'

Extract extension and print it to the console.

Expected result:

    jpg
"""

# Solution I
filename = 'view.jpg'
print(filename.split('.')[1])

# Solution II
filename = 'view.jpg'
print(filename.split('.')[-1])

# Solution III
filename = 'view.jpg'
print(filename[filename.find('.')+1:])

# Solution IV
filename = 'view.jpg'
print(filename[-3:])

# Solution V
filename = 'view.jpg'
print(filename[5:])
