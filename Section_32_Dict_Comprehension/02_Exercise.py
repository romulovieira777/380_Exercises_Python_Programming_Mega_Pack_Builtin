"""
Exercise No. 02

The following list is given:

    stocks = ['Playway', 'CD Projekt', 'Boombit']

Use dict comprehension to build a dictionary that maps the names to the numbers of characters of its name and print the
result to the console.

Expected result:

    {'Playway': 7, 'CD Projekt': 10, 'Boombit': 7}
"""
stocks = ['Playway', 'CD Projekt', 'Boombit']
result = {stock: len(stock) for stock in stocks}
print(result)
