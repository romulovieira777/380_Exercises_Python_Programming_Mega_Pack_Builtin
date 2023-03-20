"""
Exercise No. 06

The following list of companies is given:

    stocks = [
        'Apple',
        'Microsoft',
        'Amazon',
        'Google',
        'Adidas',
        'Audi',
        'Siemens'
    ]

Using the built-in itertools module and the combinations_with_replacement class create an iterator to iterate over all
two-element combinations with replacement from the stocks list. Print the result to the console as shown below.

Tip:

    #>>> help(itertools.combinations_with_replacement)

    Help on class combinations_with_replacement in module itertools:

    class combinations_with_replacement(builtins.object)
        |  combinations_with_replacement(iterable, r)
        |
        |  Return successive r-length combinations of elements in the iterable allowing individual elements to have
           successive repeats.
        |
        |  combinations_with_replacement('ABC', 2) --> AA AB AC BB BC CC"

Expected result:

    ('Apple', 'Apple')
    ('Apple', 'Microsoft')
    ('Apple', 'Amazon')
    ('Apple', 'Google')
    ('Apple', 'Adidas')
    ('Apple', 'Audi')
    ('Apple', 'Siemens')
    ('Microsoft', 'Microsoft')
    ('Microsoft', 'Amazon')
    ('Microsoft', 'Google')
    ('Microsoft', 'Adidas')
    ('Microsoft', 'Audi')
    ('Microsoft', 'Siemens')
    ('Amazon', 'Amazon')
    ('Amazon', 'Google')
    ('Amazon', 'Adidas')
    ('Amazon', 'Audi')
    ('Amazon', 'Siemens')
    ('Google', 'Google')
    ('Google', 'Adidas')
    ('Google', 'Audi')
    ('Google', 'Siemens')
    ('Adidas', 'Adidas')
    ('Adidas', 'Audi')
    ('Adidas', 'Siemens')
    ('Audi', 'Audi')
    ('Audi', 'Siemens')
    ('Siemens', 'Siemens')

"""
import itertools

stocks = [
    'Apple',
    'Microsoft',
    'Amazon',
    'Google',
    'Adidas',
    'Audi',
    'Siemens'
]

combinations = itertools.combinations_with_replacement(stocks, 2)

for combination in combinations:
    print(combination)
