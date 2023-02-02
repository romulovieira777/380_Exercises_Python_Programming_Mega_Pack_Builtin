"""
Exercise No. 08

The following text is given:
    text = '''Python plays a key role in our production pipeline. Without it a project the size of Star Wars: Episode II
                would have been very difficult to pull off.'''

Using the built-in re module find all words that start with a capital letter. Print the result to the console.

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
    ['Python', 'Without', 'Star', 'Wars', 'Episode', 'II']
"""
import re

text = '''Python plays a key role in our production pipeline. Without it a project the size of Star Wars: Episode II
            would have been very difficult to pull off.'''

result = re.findall(pattern=r"[A-Z][\w]+", string=text)
print(result)
