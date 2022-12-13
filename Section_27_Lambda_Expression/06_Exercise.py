"""
Exercise No. 06

The following list is given:

    stocks = [
        {'index': 'mWIG40', 'name': 'TEN', 'price': 304},
        {'index': 'mWIG40', 'name': 'PLW', 'price': 309},
        {'index': 'sWIG80', 'name': 'BBT', 'price': 22}
    ]

Extract companies from the 'mWIG40' index and print the result to the console.

Formatted result:

    [{'index': 'mWIG40', 'name': 'TEN', 'price': 304},
        {'index': 'mWIG40', 'name': 'PLW', 'price': 309}]

Expected result:

    [{'index': 'mWIG40', 'name': 'TEN', 'price': 304},
        {'index': 'mWIG40', 'name': 'PLW', 'price': 309}]
"""

# Solution I
stocks = [
    {'index': 'mWIG40', 'name': 'TEN', 'price': 304},
    {'index': 'mWIG40', 'name': 'PLW', 'price': 309},
    {'index': 'sWIG80', 'name': 'BBT', 'price': 22}
]

mwig40 = list(filter(lambda x: x['index'] == 'mWIG40', stocks))
print(mwig40)


# Solution II
stocks = [
    {'index': 'mWIG40', 'name': 'TEN', 'price': 304},
    {'index': 'mWIG40', 'name': 'PLW', 'price': 309},
    {'index': 'sWIG80', 'name': 'BBT', 'price': 22}
]

print(list(filter(lambda stock: stock['index'] == 'mWIG40', stocks)))
