"""
Exercise No. 12

A list of names entered by users into the system is given below (without validation process):

    names = ['Jack', 'Leon', 'Alice', '32-3c', 'Bob']

Iterate through the names list and check if each names is correct (contains only letters). If so, print to the console
following message: f'Hello {name}!' otherwise do nothing.

Tip: Use the str.isalpha() method.

Expected result:

    Hello Jack!
    Hello Leon!
    Hello Alice!
    Hello Bob!
"""
names = ['Jack', 'Leon', 'Alice', '32-3c', 'Bob']

for name in names:
    if name.isalpha():
        print(f'Hello {name}!')
