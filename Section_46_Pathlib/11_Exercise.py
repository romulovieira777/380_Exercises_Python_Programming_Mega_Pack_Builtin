"""
Exercise No. 11

The following path is given:

    path = Path.cwd() / 'hello.txt'

Using the built-in pathlib module check if the specified file exists. If not, create it using the pathlib module and
write into it the following text:

    Open,High,Low,Close

Then open this file using the pathlib module and load its contents into the content variable.

In response, print the content variable to the console.

Tip:

    # >>> help(pathlib.Path.write_text)
    Help on function write_text in module pathlib:

    write_text(self, data, encoding=None, errors=None)
        Open the file in text mode, write to it, and close the file.

    # >>> help(pathlib.Path.read_text)
    Help on function read_text in module pathlib:

    read_text(self, encoding=None, errors=None)
        Open the file in text mode, read it, and close the file.

Expected result:

    Open,High,Low,Close
"""
from pathlib import Path

path = Path.cwd() / 'hello.txt'

# Solution I
if not path.exists():
    path.write_text('Open,High,Low,Close')

content = path.read_text()

print(content)


# Solution II
if not path.is_file():
    path.write_text('Open,High,Low,Close')

content = path.read_text()

print(content)
