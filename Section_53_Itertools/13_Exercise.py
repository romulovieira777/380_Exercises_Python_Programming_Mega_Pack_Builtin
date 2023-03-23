"""
Exercise No. 13

The following lists are given:

    stocks_us = ['Apple', 'Microsoft', 'Amazon', 'Google']
    stocks_de = ['Adidas', 'Audi', 'Siemens']

Then these lists are combined in one as follows:

    stocks = [stocks_us, stocks_de]

which gives:

    [['Apple', 'Microsoft', 'Amazon', 'Google'], ['Adidas', 'Audi', 'Siemens']]

Using the built-in itertools module and the chain class create an iterator that iterates through all company names from
the stocks list and assign to the results variable.

In response, print all elements of the results iterator to the console as shown below.

Tip:

    #>>> help(itertools.chain.from_iterable)

    Help on built-in function from_iterable:

    from_iterable(iterable, /) method of builtins.type instance
        Alternative chain() constructor taking a single iterable argument that evaluates lazily.

Expected result:

    Apple
    Microsoft
    Amazon
    Google
    Adidas
    Audi
    Siemens
"""
import itertools

stocks_us = ['Apple', 'Microsoft', 'Amazon', 'Google']
stocks_de = ['Adidas', 'Audi', 'Siemens']

stocks = [stocks_us, stocks_de]

for stock in itertools.chain.from_iterable(stocks):
    print(stock)
