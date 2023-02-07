"""
Exercise No. 13

Using the built-in collections module from the following dictionaries:

    techs = {'Apple': 370, 'Samsung': 1100, 'Microsoft': 201}
    finance = {'Citigroup': 51, 'Allianz': 180}
    gaming = {'Sony': 76, 'Nintendo': 470, 'EA': 135}

An object of the ChainMap class was created and assigned to the stocks variable.

Print all keys of the ChainMap object to the console (sorted alphabetically).

Tip:
    #>>> help(ChainMap.keys)

    Help on function keys in module collections.abc:

    keys(self)
        D.keys() -> a set-like object providing a view on D's keys

Expected result:

    ['Allianz', 'Apple', 'Citigroup', 'EA', 'Microsoft', 'Nintendo', 'Samsung', 'Sony']
"""
from collections import ChainMap

techs = {'Apple': 370, 'Samsung': 1100, 'Microsoft': 201}
finance = {'Citigroup': 51, 'Allianz': 180}
gaming = {'Sony': 76, 'Nintendo': 470, 'EA': 135}

stocks = ChainMap(techs, finance, gaming)
print(sorted(stocks.keys()))    # Solution I
print(sorted(list(stocks.keys())))  # Solution II
