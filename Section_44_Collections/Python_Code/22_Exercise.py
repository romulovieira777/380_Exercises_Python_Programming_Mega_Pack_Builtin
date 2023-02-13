"""
Exercise No. 22

Consider an empty dictionary named quotations as defined below:

    quotations = {}

When trying to read a value for non-existing key, e.g. 'source'.

    quotations['source']

We get the KeyError. We can deal with it in several ways. For this exercise, consider the dict.setdefault() method:

    # >>> help(dict.setdefault)

    Help on method_descriptor:

    setdefault(...)
        D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D

Using the dict.setdefault() method set the default value for the 'source' key to 'NYSE'. Then print the quotations
dictionary to the console.

Try again to set the default value for the key 'source' to 'LSE' this time. Then print the dictionary quotations and the
value for the key 'source' of quotations dictionary as shown below to the console.

Expected result:

    {'source': 'NYSE'}
    {'source': 'NYSE'}
    NYSE
"""
quotations = {}
quotations.setdefault('source', 'NYSE')
print(quotations)

quotations.setdefault('source', 'LSE')
print(quotations)
print(quotations['source'])
