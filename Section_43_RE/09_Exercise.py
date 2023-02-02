"""
Exercise No. 09

The following text is given:
    message = 'For more information, please call: 123-456-789'

Using the built-in re module extract the phone number from the given message.

In response, print the result to the console.

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
    123-456-789
"""
import re

message = 'For more information, please call: 123-456-789'

result = re.findall(r"\d{3}-\d{3}-\d{3}", message)[0]
print(result)
