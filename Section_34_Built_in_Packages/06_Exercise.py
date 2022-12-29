"""
Exercise No. 06

Using the built-in module for regular expressions, find all email addresses in the following text:

    raw_text = "Send an email to info@template.com or sales-info@template.it"

Print the result to the console.

Tip: Use the findall() function and the regular expression '[\w\.-]+@[\w\.-]+'.

Expected result:

    ['info@template.com', 'sales-info@template.it']
"""
import re

raw_text = "Send an email to info@template.com or sales-info@template.it"

# Solution I
print(re.findall('[\w\.-]+@[\w\.-]+', raw_text))


# Solution II
result = re.findall(r"[\w\.-]+@[\w\.-]+", raw_text)
print(result)
