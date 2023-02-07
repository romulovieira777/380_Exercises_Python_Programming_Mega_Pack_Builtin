"""
Exercise No. 11

Using the built-in collections module from the following dictionaries:

    techs = {'Apple': 370, 'Samsung': 1100, 'Microsoft': 201}
    finance = {'Citigroup': 51, 'Allianz': 180}
    gaming = {'Sony': 76, 'Nintendo': 470, 'EA': 135}

A ChainMap object was created and assigned to the stocks variable. Update the value for the 'Microsoft' in the techs
dictionary to 120.

Then read the value for this key and print to the console.

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

    210
"""
from collections import ChainMap

techs = {'Apple': 370, 'Samsung': 1100, 'Microsoft': 201}
finance = {'Citigroup': 51, 'Allianz': 180}
gaming = {'Sony': 76, 'Nintendo': 470, 'EA': 135}

stocks = ChainMap(techs, finance, gaming)
stocks['Microsoft'] = 210
print(stocks['Microsoft'])
