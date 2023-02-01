"""
Exercise No. 04

Using the built-in module re and the appropriate regular expression, extract from the following code:
    code = '0010-000-423-22'

A list of the following values:
    ['0010', '000', '423', '22']

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


    #>>> help(re.split)

    Help on function split in module re:

    split(pattern, string, maxsplit=0, flags=0)
        Split the source string by the occurrences of the pattern,
        returning a list containing the resulting substrings.  If
        capturing parentheses are used in pattern, then the text of all
        groups in the pattern are also returned as part of the resulting
        list.  If maxsplit is nonzero, at most maxsplit splits occur,
        and the remainder of the string is returned as the final element
        of the list.

Expected result:
    ['0010', '000', '423', '22']
"""
import re

# Solution I
code = '0010-000-423-22'

result = re.split(pattern=r"-", string=code)
print(result)


# Solution II
code = '0010-000-423-22'

result = re.findall(pattern=r"[^-]+", string=code)
print(result)
