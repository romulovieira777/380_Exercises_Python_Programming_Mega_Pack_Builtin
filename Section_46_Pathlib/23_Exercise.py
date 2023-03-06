"""
Exercise No. 23

The README.md file from the pandas library is given. Using the built-in pathlib module, load this file into the content
variable. Then using the built-in re module and the following regular expression:

    pattern = r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+"

extract from the content variable all unique links sorted alphabetically.

In response, print each link on a separate line to the console.

Tip:

    # >>> help(pathlib.Path.read_text)

    Help on function read_text in module pathlib:

    read_text(self, encoding=None, errors=None)
        Open the file in text mode, read it, and close the file.


    # >>> help(re.findall)

    Help on function findall in module re:

    findall(pattern, string, flags=0)
        Return a list of all non-overlapping matches in the string.

        If one or more capturing groups are present in the pattern, return
        a list of groups; this will be a list of tuples if the pattern
        has more than one group.

        Empty matches are included in the result.

Expected result:

    https://anaconda.org
    https://badges.gitter.im
    https://codecov.io
    https://dev.azure.com
    https://dev.pandas.io
    https://doi.org
    https://github.com
    https://gitter.im
    https://groups.google.com
    https://img.shields.io
    https://labix.org
    https://mail.python.org
    https://numfocus.org
    https://pandas.pydata.org
    https://pip.pypa.io
    https://pypi.org
    https://pythonhosted.org
    https://stackoverflow.com
    https://travis-ci.org
    https://www.codetriage.com
    https://www.numpy.org
    https://zenodo.org
"""
from pathlib import Path
import re

pattern = r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+"

path = Path.cwd() / '../Files/README.md'
content = path.read_text()

links = re.findall(pattern, content)
links = sorted(set(links))

print('\n'.join(links))
