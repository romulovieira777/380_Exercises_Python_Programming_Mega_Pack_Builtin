"""
Exercise No. 05

Using the built-in module for regular expressions, find all alphanumeric characters in the following text:

    string = '!@#$%^&45wc'

Print the result to the console.

Tip: Use the findall() function and the regular expression '\w'.

Expected result:

    ['4', '5', 'w', 'c']
"""
import re

string = '!@#$%^&45wc'

# Solution I
print(re.findall('\w', string))


# Solution II
result = re.findall(pattern=r"\w", string=string)
print(result)
