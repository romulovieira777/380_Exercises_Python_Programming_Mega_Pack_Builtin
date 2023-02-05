"""
Exercise No. 06

The following text is given:
    text = '''Python is fast enough for our site and allows us to produce maintainable features in record times,
        with a minimum of developers," said Cuong Do, Software Architect, YouTube.com.

        "Python plays a key role in our production pipeline. Without it a project the size of Star Wars:
        Episode II would have been very difficult to pull off. From crowd rendering to batch processing to compositing,
        Python binds all things together," said Tommy Burnette, Senior Technical Director, Industrial Light & Magic.'''

Using the built-in re module split the given text into words/tokens. Standardize the words (all lowercase). Then create
a Counter object that allows you to determine the three most common words in the text. In response, print these words
with the number of occurrences.

Expected result:
    [('to', 4), ('python', 3), ('a', 3)]
"""
from collections import Counter
import re

text = """"Python is fast enough for our site and allows us to produce maintainable features in record times,
with a minimum of developers," said Cuong Do, Software Architect, YouTube.com.

"Python plays a key role in our production pipeline. Without it a project the size of Star Wars:
Episode II would have been very difficult to pull off. From crowd rendering to batch processing to compositing,
Python binds all things together," said Tommy Burnette, Senior Technical Director, Industrial Light & Magic."""

# Solution I
tokens = re.split(r'\W+', text.lower())
counter = Counter(tokens)
print(counter.most_common(3))


# Solution II
tokens = re.findall(r"\w+", text)
tokens = [token.lower() for token in tokens]
cnt = Counter(tokens)
print(cnt.most_common(3))
