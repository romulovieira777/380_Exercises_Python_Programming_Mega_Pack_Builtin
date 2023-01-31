"""
Exercise No. 03

Using the built-in re module extract all digits except zero as a list from the following code:
    code = '0010-000-423'

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
    ['1', '4', '2', '3']
"""
import re

code = '0010-000-423'

result = re.findall(pattern=r"[^0-]", string=code)
print(result)
