"""
Exercise No. 01

Use the built-in copy module, make a shallow copy of the following stocks list:
    stocks = [['CDR', '11B'], ['PLW'], ['TEN']]

And assign to the stocks_copied variable. Replace '11B' in the first element of the stocks list with 'CRJ'.

Note the values in the stocks_copied list. Print both stocks and stocks_copied lists (each as a separate line) as shown
below:

Tip:
    #>>> help(copy.copy)

    Help on function copy in module copy:

    copy(x)
        Shallow copy operation on arbitrary Python objects.

        See the module's __doc__ string for more info.

Expected result:
    stocks: [['CDR', 'CRJ'], ['PLW'], ['TEN']]
    stocks_copied: [['CDR', 'CRJ'], ['PLW'], ['TEN']]
"""
import copy

stocks = [['CDR', '11B'], ['PLW'], ['TEN']]
stocks_copied = copy.copy(stocks)
stocks[0][1] = 'CRJ'

print('stocks:', stocks)
print('stocks_copied:', stocks_copied)
