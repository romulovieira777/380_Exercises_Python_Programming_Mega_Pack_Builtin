"""
Exercise No. 06

The following text is given:
    text = 'Please send an email to info@template.com or sales-info@template.it'

Using the built-in re module extract all e-mail addresses from the text and print to the console.

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
    ['info@template.com', 'sales-info@template.it']
"""
import re

text = 'Please send an email to info@template.com or sales-info@template.it'

result = re.findall(pattern=r"[\w\.-]+@[\w\.-]+", string=text)
print(result)

