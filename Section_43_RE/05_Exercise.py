"""
Exercise No. 05

Using the built-in re module and the appropriate regular expression, extract from the following code:
    code = 'PL code: XG-GH-110'

A list of the following values:
    ['PL', '110']

In response, print this list to the console.

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
    ['PL', '110']
"""
import re

code = 'PL code: XG-GH-110'

result = re.findall(pattern=r"PL|\d+", string=code)
print(result)
