"""
Exercise No. 07

The following text is given:
    text = '''Python plays a key role in our production pipeline. Without it a project the size of Star Wars: Episode II
             would have been very difficult to pull off.'''

Using the built-in re module split the text into words/tokens as shown below. Print the result to the console. Pay
attention to punctuation marks.

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
    ['Python', 'plays', 'a', 'key', 'role', 'in', 'our', 'production', 'pipeline', 'Without', 'it', 'a', 'project',
     'the', 'size', 'of', 'Star', 'Wars', 'Episode', 'II', 'would', 'have', 'been', 'very', 'difficult', 'to', 'pull',
     'off'
    ]
"""
import re

text = '''Python plays a key role in our production pipeline. Without it a project the size of Star Wars: Episode II
            would have been very difficult to pull off.'''
result = re.findall(pattern=r"[\w]+", string=text)
print(result)
