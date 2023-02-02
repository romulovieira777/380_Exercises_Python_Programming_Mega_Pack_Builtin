"""
Exercise No. 10

The following text is given:
    text = 'Please send an email to info@template.com or call to: 123-456-789.'

Using the built-in module mask the telephone number as follows '***_***_***'.

In response, print this text to the console.

Tip:
    #>>> help(re.sub)

    Help on function sub in module re:

    sub(pattern, repl, string, count=0, flags=0)
        Return the string obtained by replacing the leftmost
        non-overlapping occurrences of the pattern in string by the
        replacement repl.  repl can be either a string or a callable;
        if a string, backslash escapes in it are processed.  If it is
        a callable, it's passed the match object and must return
        a replacement string to be used.

Expected result:
    Please send an email to info@template.com or call to: ***-***-***.
"""
import re

text = 'Please send an email to info@template.com or call to: 123-456-789.'

result = re.sub(r"\d{3}-\d{3}-\d{3}", "***-***-***", text)
print(result)
