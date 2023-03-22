"""
Exercise No. 12

The following lists are given:

    stocks_us = ['Apple', 'Microsoft', 'Amazon', 'Google']
    stocks_de = ['Adidas', 'Audi', 'Siemens']

Using the built-in itertools module and the chain class create an iterator to iterator through all company names in the
stocks_us and stocks_de lists and assign to the results variable.

In response, print all elements of the results iterator to the console as shown below.

Tip:

    #>>> help(itertools.chain)

    Help on class chain in module itertools:

    class chain(builtins.object)
     |  chain(*iterables) --> chain object
     |
     |  Return a chain object whose .__next__() method returns elements from the
     |  first iterable until it is exhausted, then elements from the next
     |  iterable, until all of the iterables are exhausted.

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

for stock in itertools.chain(stocks_us, stocks_de):
    print(stock)
