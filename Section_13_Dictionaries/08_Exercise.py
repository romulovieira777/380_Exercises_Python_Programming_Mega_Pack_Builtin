"""
Exercise No. 08

The following dictionary is given:

    stocks = {
        'MSFT.US': {'Microsoft Corp': 184},
        'AAPL.US': {'Apple Inc': 310},
        'MMM.US': {'3M Co': 148}
    }

Update the price for Microsoft to 190 and print the value fot the 'MSFT.US' key to the console.

Expected result:

    {'Microsoft Corp': 190}
"""
stocks = {
    'MSFT.US': {'Microsoft Corp': 184},
    'AAPL.US': {'Apple Inc': 310},
    'MMM.US': {'3M Co': 148}
}

stocks['MSFT.US']['Microsoft Corp'] = 190
print(stocks['MSFT.US'])
