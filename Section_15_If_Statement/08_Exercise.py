"""
Exercise No. 08

Write a program that checks if the given item:

    item = '001'

Is in the list:

    items = ['001', '000', '003', '005', '006']

If so, remove this item from the list and print this list to the console.

Expected result:

    ['000', '003', '005', '006']
"""
items = ['001', '000', '003', '005', '006']
item = '001'

if item in items:
    items.remove(item)

print(items)
