"""
Exercise No. 13

The following problem was encountered while implementing the car application. It's necessary to store information about
car settings (with one object in Python). Two parameters are always set:

    - mode
    - power_level

By default, these parameters store the values: 'eco' and 7. However, their values may change depending on the user's
settings.

Let's assume that the user can pass the following settings:

    - {'mode': 'sport', 'power_level': 10}

Consider how you can use the ChainMap class in this case.

Steps:

    - create a dictionary with default settings (default_settings).
    - create a dictionary with user settings (user_settings).
    - create a ChainMap object from the given dictionaries in the right order (settings).

In response, print the value of the 'mode' key of the settings ChainMap.

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

    sport
"""
from collections import ChainMap

default_settings = {'mode': 'eco', 'power_level': 7}
user_settings = {'mode': 'sport', 'power_level': 10}

settings = ChainMap(user_settings, default_settings)
print(settings['mode'])
