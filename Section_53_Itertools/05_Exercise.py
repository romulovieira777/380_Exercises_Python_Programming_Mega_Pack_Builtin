"""
Exercise No. 05

The following list of companies is given:

    stocks = [
        'Apple',
        'Microsoft',
        'Amazon',
        'Google',
        'Adidas',
        'Audi',
        'Sistemas'
    ]

Using the built-in itertools module and the combinations class create an iterator that iterates over all two-element
combinations from the stocks list. Print the result to the console as shown below.

Tip:

    #>>> help(itertools.combinations)

    Help on class combinations in module itertools:

    class combinations(builtins.object)
     |  combinations(iterable, r)
     |
     |  Return successive r-length combinations of elements in the iterable.
     |
     |  combinations(range(4), 3) --> (0,1,2), (0,1,3), (0,2,3), (1,2,3)

Expected result:

    ('Apple', 'Microsoft')
    ('Apple', 'Amazon')
    ('Apple', 'Google')
    ('Apple', 'Adidas')
    ('Apple', 'Audi')
    ('Apple', 'Siemens')
    ('Microsoft', 'Amazon')
    ('Microsoft', 'Google')
    ('Microsoft', 'Adidas')
    ('Microsoft', 'Audi')
    ('Microsoft', 'Siemens')
    ('Amazon', 'Google')
    ('Amazon', 'Adidas')
    ('Amazon', 'Audi')
    ('Amazon', 'Siemens')
    ('Google', 'Adidas')
    ('Google', 'Audi')
    ('Google', 'Siemens')
    ('Adidas', 'Audi')
    ('Adidas', 'Siemens')
    ('Audi', 'Siemens')
"""
import itertools

stocks = [
    'Apple',
    'Microsoft',
    'Amazon',
    'Google',
    'Adidas',
    'Audi',
    'Sistemas'
]

counter = itertools.combinations(stocks, 2)

for i in counter:
    print(i)
