"""
Exercise No. 07

Using the built-in module for regular expressions, split the following text by whitespace (spaces):

    text = "Programming in Python - from A to Z"

Print the result to the console.

Tip: Use the re.split() function and the regular expression '\s+'.
"""
import re

text = "Programming in Python - from A to Z"

# Solution I
print(re.split('\s+', text))


# Solution II
result = re.split(pattern=r"\s+", string=text)
print(result)
