"""
Exercise No. 07

The following list is given:

    indexes = ['WIG20', 'mWIG40', 'sWIG80']

Using dict comprehension. convert the above list into the following dictionary:

    {0: 'WIG20', 1: 'mWIG40', 2: 'sWIG80'}

Print the result to the console.
"""
# Solution I
indexes = ['WIG20', 'mWIG40', 'sWIG80']
result = {index: indexes[index] for index in range(len(indexes))}
print(result)


# Solution II
indexes = ['WIG20', 'mWIG40', 'sWIG80']
data = {key: val for key, val in enumerate(indexes)}
print(data)
