"""
Exercise No. 10

The following path is given:

    path = Path.cwd() / 'hello.txt'

Using the built-in pathlib module check if the specified file exists. If not, create it in the standard way (statement
with open...) and write into it the following text:

    Open,High,Low,Close

Then open this file in the standard way (statement with open...) and load its contents into the content variable.

In response, print the content variable to the console.

Expected result:

    Open,High,Low,Close
"""
from pathlib import Path

path = Path.cwd() / 'hello.txt'

# Solution I
if not path.exists():
    with open(path, 'w') as file:
        file.write('Open,High,Low,Close')

with open(path, 'r') as file:
    content = file.read()

print(content)


# Solution II
if not path.is_file():
    with open(path, 'w') as file:
        file.write('Open,High,Low,Close')

with open(path, 'r') as file:
    content = file.read()

print(content)
