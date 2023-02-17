"""
Exercise No. 26

The following list is given:

    transactions = [
        ('001', 100),
        ('003', 10),
        ('002', 80),
        ('001', 90),
        ('002', 46),
        ('001', 43),
        ('003', 23),
    ]

Using the built-in collections module and the defaultdict class create the following object (group by the first element
- user_id):

    defaultdict(<class 'int'>, {'001': 233,, '003': 33, '002': 126})

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

    defaultdict(<class 'int'>, {'001': 233, '003': 33, '002': 126})
"""
from collections import defaultdict

transactions = [
    ('001', 100),
    ('003', 10),
    ('002', 80),
    ('001', 90),
    ('002', 46),
    ('001', 43),
    ('003', 23),
]

def_dict = defaultdict(int)
for key, value in transactions:
    def_dict[key] += value

print(def_dict)
