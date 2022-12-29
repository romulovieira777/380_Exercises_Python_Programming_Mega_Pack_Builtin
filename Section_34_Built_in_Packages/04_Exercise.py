"""
Exercise No. 04

Using the built-in module for regular expressions, find all digits in the following text:

    string = 'Python 3.8'

Print the result to the console.

Tip: Use the findall() function and the regular expression '\d'.

Expected result:

    ['3', '8']
"""
import re

string = 'Python 3.8'

# Solution I
print(re.findall('\d', string))


# Solution II
result = re.findall(pattern=r"\d", string=string)
print(result)
