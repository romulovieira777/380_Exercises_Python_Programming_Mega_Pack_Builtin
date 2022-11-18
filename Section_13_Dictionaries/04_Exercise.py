"""
Exercise No. 04

The following dictionary is given:

    capitals = {
        'USA': 'Washington',
        'Germany': 'Berlin',
        'Austria': 'Vienna'
    }

Use the appropriate method, extract the list containing tuple objects (key, value) from the capitals dictionary and
print to the console as shown below.

Expected result:

    [('USA', 'Washington'), ('Germany', 'Berlin'), ('Austria', 'Vienna')]
"""
capitals = {'USA': 'Washington', 'Germany': 'Berlin', 'Austria': 'Vienna'}

print(capitals.items())
