"""
Exercise No. 06

The following list of indexes is given:

    indeks = ['WIG20', 'mWIG40', 'sWIG80']

and a list of properties for each index:

    properties = ['number of companies', 'companies', 'cap']

Using dict comprehension, create the following dictionary:

    {'WIG20': {'cap': None, 'companies': None, 'number of companies': None},
     'mWIG40': {'cap': None, 'companies': None, 'number of companies': None},
     'sWIG80': {'cap': None, 'companies': None, 'number of companies': None}}

Set the default value of each property to None and print the result to the console.

Expected result:

    {'WIG20': {'number of companies': None, 'companies': None, 'cap': None},
     'mWIG40': {'number of companies': None, 'companies': None, 'cap': None},
     'sWIG80': {'number of companies': None, 'companies': None, 'cap': None}}
"""
indeks = ['WIG20', 'mWIG40', 'sWIG80']
properties = ['number of companies', 'companies', 'cap']
result = {index: {property: None for property in properties} for index in indeks}
print(result)
