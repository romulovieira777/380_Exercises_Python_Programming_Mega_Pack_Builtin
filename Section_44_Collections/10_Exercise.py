""""
Exercise No. 10

Using the built-in collections module from the following dictionaries:

    techs = {'Apple': 370, 'Samsung': 1100, 'Microsoft': 201}
    finance = {'Citigroup': 51, 'Allianz': 180}
    gaming = {'Sony': 76, 'Nintendo': 470, 'EA': 135}

Create a ChainMap object and assign to the stocks variable. Find the value for the 'Samsung' key in the ChainMap object
and print to the console.

Tip:
    #>>> help(ChainMap)

    Help on class ChainMap in module collections:

    class ChainMap(collections.abc.MutableMapping)
     |  A ChainMap groups multiple dicts (or other mappings) together
     |  to create a single, updateable view.
     |
     |  The underlying mappings are stored in a list.  That list is public and can
     |  be accessed or updated using the *maps* attribute.  There is no other
     |  state.
     |
     |  Lookups search the underlying mappings successively until a key is found.
     |  In contrast, writes, updates, and deletions only operate on the first
     |  mapping.

Expected result:

    1100
"""
from collections import ChainMap

techs = {'Apple': 370, 'Samsung': 1100, 'Microsoft': 201}
finance = {'Citigroup': 51, 'Allianz': 180}
gaming = {'Sony': 76, 'Nintendo': 470, 'EA': 135}

stocks = ChainMap(techs, finance, gaming)
print(stocks['Samsung'])
