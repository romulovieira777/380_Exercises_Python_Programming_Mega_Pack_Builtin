"""
Exercise No. 21

Consider an empty dictionary named quotations as defined below:

    quotations = {}

When trying to read a value for non-existing key, e.g. 'source'.

    quotations['source']

We get the KeyError. We can deal with it in several ways. For this exercise, consider the dict.get() method:

    # >>> help(dict.get)

    Help on method_descriptor:

    get(...)
        D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.

In this case, when we execute the code:

    quotations.get('source')

No error is raised and the return value is None.

Using the dict.get() method, set the default value to 'NYSE' and print value for 'source' key of quotations dictionary
to the console.

Also print the quotations dictionary to the console.

Expected result:

    NYSE
    {}
"""
quotations = {}

print(quotations.get('source', 'NYSE'))
print(quotations)
