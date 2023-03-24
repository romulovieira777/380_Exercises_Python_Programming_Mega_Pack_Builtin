"""
Exercise No. 17

The following list is given:

    stocks = [
        'Apple',
        'Microsoft',
        'Amazon',
        'Google',
        'Adidas',
        'Audi',
        'Siemens'
    ]

Create a list called stocks_flag that stores True when the company name starts with the letter 'A', otherwise False.

    [True, False, True, False, True, True, False]

Then, using the built-in itertools module and the compress class create an iterator that allows you to iterate over all
companies whose names start with the letter 'A'.

In response, print all elements of the results iterator to the console as shown below.

Tip:

    #>>> help(itertools.compress)

    Help on class compress in module itertools:

    class compress(builtins.object)
        |  compress(data, selectors)
        |
        |  Return data elements corresponding to true selector elements.
        |
        | Forms a shorter iterator from selected data elements using the selectors to
        | choose the data elements.

Expected result:

    Apple
    Amazon
    Adidas
    Audi
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

# Solution I
stocks_flag = [True if stock.startswith('A') else False for stock in stocks]

for stock in itertools.compress(stocks, stocks_flag):
    print(stock)


# Solution II
stocks_flag = [name.startswith('A') for name in stocks]

results = itertools.compress(stocks, stocks_flag)

for stock in results:
    print(stock)
