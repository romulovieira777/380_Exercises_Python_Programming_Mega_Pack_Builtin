"""
Exercise No. 09

Using the built-in collections module from the following dictionaries:

    stocks_1 = {'CDR': 400, 'PLW': 490}
    stocks_2 = {'PLW': 500, 'TEN': 550, 'BBT': 30}

A ChainMap object has been created and assigned to the stocks variable. Find the value for the key 'PLW' in the ChainMap
object and print to the console.

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

    490
"""
from collections import ChainMap

stocks_1 = {'CDR': 400, 'PLW': 490}
stocks_2 = {'PLW': 500, 'TEN': 550, 'BBT': 30}

stocks = ChainMap(stocks_1, stocks_2)
print(stocks['PLW'])
