"""
Exercise No. 02

Using the built-in re module extract all non-numbers characters as a list from the following text:
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
    ['P', 'y', 't', 'h', 'o', 'n', ' ', '.']
"""
import re

text = 'Python 3.8'

result = re.findall(r'\D', string=text)
print(result)
