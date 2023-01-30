"""
Exercise No. 02

Using the built-in copy module, make a deep copy of the following stocks list:
    stocks = [['CDR', '11B'], ['PLW'], ['TEN']]

And assign to the stocks_copied variable. Replace '11B' in the first element of the stocks list with 'CRJ'.

Note the values in the stocks_copied list. Print both stocks and stocks_copied lists (each as a separate line) as shown
below:

Tip:
    #>>> help(copy.deepcopy)

    Help on function copy in module copy:

    copy(x)
        Shallow copy operation on arbitrary Python objects.

        See the module's __doc__ string for more info.

Expected result:
    stocks: [['CDR', 'CRJ'], ['PLW'], ['TEN']]
    stocks_copied: [['CDR', '11B'], ['PLW'], ['TEN']]
"""
import copy

stocks = [['CDR', '11B'], ['PLW'], ['TEN']]
stocks_copied = copy.deepcopy(stocks)
stocks[0][1] = 'CRJ'

print(f'stocks: {stocks}')
print(f'stocks_copied: {stocks_copied}')
