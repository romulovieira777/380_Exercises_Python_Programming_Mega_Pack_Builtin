"""
Exercise No. 08

Using the built-in pathlib module create a Path instance that stores the following path:

    - current working directory + 'reports/ecommerce/2020/01'

and assign to path variable.

Then create directories from path (none of the directories: reports/ecommerce/2020/01 exist).

In response. Check if that path is a directory and print the result to the console.

Tip:

    # >>> help(pathlib.Path.mkdir)

    Help on function mkdir in module pathlib:

    mkdir(self, mode=511, parents=False, exist_ok=False)
        Create a new directory at this given path.


    # >>> help(pathlib.Path.is_dir)

    Help on function is_dir in module pathlib:

    is_dir(self)
        Whether this path is a directory.

Expected result:

    True
"""
from pathlib import Path

path = Path.cwd().joinpath('reports/ecommerce/2020/01')
path.mkdir(parents=True)

print(path.is_dir())
