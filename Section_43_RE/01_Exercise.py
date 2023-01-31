"""
Exercise No. 01

Using the built-in re module that allows you to work with regular expressions in Python extract all the numbers as a
list from the following text:
    text = 'Python 3.8'

And print to the console.

Tip:
    #>>> help(re.findall)

    Help on function findall in module re:

    findall(pattern, string, flags=0)
        Return a list of all non-overlapping matches in the string.

        If one or more capturing groups are present in the pattern, return
        a list of groups; this will be a list of tuples if the pattern
        has more than one group.

        Empty matches are included in the result.

Expected result:
    ['3', '8']
"""
import re

text = 'Python 3.8'

result = re.findall(r'\d', string=text)
print(result)
