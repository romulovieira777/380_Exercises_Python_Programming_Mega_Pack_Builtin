"""
Exercise No. 23

The following list is given:

    data = [
        ('technology', Apple),
        ('gaming', 'Techland'),
        ('finance', 'Berkshire Hathaway'),
        ('gaming', 'EA'),
        ('technology', 'Facebook'),
        ('gaming', 'CD Projekt'),
        ('finance', 'Allianz')
    ]

Using the dictionary and the dict.setdefault() method create the following object:

    {
        'finance': ['Berkshire Hathaway', 'Allianz'],
        'gaming': ['Techland', 'EA', 'CD Projekt'],
        'technology': ['Apple', 'Facebook']
    }

And assign it to the data_dict variable.

In response, print this variable to the console.

Tip:

    # >>> help(dict.setdefault)

    Help on method_descriptor:

    setdefault(...)
        D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D

Expected result:

    {
        'technology': ['Apple', 'Facebook'],
        'gaming': ['Techland', 'EA', 'CD Projekt'],
        'finance': ['Berkshire Hathaway', 'Allianz']
    }
"""
data = [
    ('technology', 'Apple'),
    ('gaming', 'Techland'),
    ('finance', 'Berkshire Hathaway'),
    ('gaming', 'EA'),
    ('technology', 'Facebook'),
    ('gaming', 'CD Projekt'),
    ('finance', 'Allianz')
]

data_dict = {}
for key, value in data:
    data_dict.setdefault(key, []).append(value)

print(data_dict)
