"""
Exercise No. 25

The following list is given:

    data = [
        ('technology', 'Facebook'),
        ('technology', 'Apple'),
        ('gaming', 'Techland'),
        ('finance', 'Berkshire Hathaway'),
        ('gaming', 'EA'),
        ('gaming', 'EA'),
        ('technology', 'Facebook'),
        ('gaming', 'CD Projekt'),
        ('finance', 'Allianz')
    ]

Notice that the list contains duplicate values. Using the built-in collections module and the defaultdict class create
the following object:

    defaultdict(<class 'set'>, {'technology': {'Facebook', 'Apple'}, 'gaming': {'Techland', 'CD Projekt', 'EA'},
    'finance': {'Berkshire Hathaway', 'Allianz'}})

And assign it to def_dict. Print this variable to the console.

Tip:

    # >>> help(defaultdict)

    Help on class defaultdict in module collections:

    class defaultdict(builtins.dict)
     |  defaultdict(default_factory[, ...]) --> dict with default factory
     |
     |  The default factory is called without arguments to produce
     |  a new value when a key is not present, in __getitem__ only.
     |  A defaultdict compares equal to a dict with the same items.
     |  All remaining arguments are treated the same as if they were
     |  passed to the dict constructor, including keyword arguments.

Expected result:

    defaultdict(<class 'set'>, {'technology': {'Facebook', 'Apple'}, 'gaming': {'EA', 'CD Projekt', 'Techland'},
    'finance': {'Allianz', 'Berkshire Hathaway'}})
"""
from collections import defaultdict

data = [
    ('technology', 'Facebook'),
    ('technology', 'Apple'),
    ('gaming', 'Techland'),
    ('finance', 'Berkshire Hathaway'),
    ('gaming', 'EA'),
    ('gaming', 'EA'),
    ('technology', 'Facebook'),
    ('gaming', 'CD Projekt'),
    ('finance', 'Allianz')
]

def_dict = defaultdict(set)
for key, value in data:
    def_dict[key].add(value)

print(def_dict)
