"""
Exercise No. 24

The following list is given:

    data = [
        ('technology', 'Apple'),
        ('gaming', 'Techland'),
        ('finance', 'Berkshire Hathaway'),
        ('gaming', 'EA'),
        ('technology', 'Facebook'),
        ('gaming', 'CD Projekt'),
        ('finance', 'Allianz')
    ]

Using the built-in collections module and the defaultdict class create the following object:

    defaultdict(<class 'list'>, {'technology': ['Apple', 'Facebook'], 'gaming': ['Techland', 'EA', 'CD Projekt'],
    'finance': ['Berkshire Hathaway', 'Allianz']})

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

    defaultdict(<class 'list'>, {'technology': ['Apple', 'Facebook'], 'gaming': ['Techland', 'EA', 'CD Projekt'],
    'finance': ['Berkshire Hathaway', 'Allianz']})
"""
from collections import defaultdict

data = [
    ('technology', 'Apple'),
    ('gaming', 'Techland'),
    ('finance', 'Berkshire Hathaway'),
    ('gaming', 'EA'),
    ('technology', 'Facebook'),
    ('gaming', 'CD Projekt'),
    ('finance', 'Allianz')
]

def_dict = defaultdict(list)
for key, value in data:
    def_dict[key].append(value)

print(def_dict)
