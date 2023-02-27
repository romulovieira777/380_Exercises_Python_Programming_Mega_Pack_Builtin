"""
Exercise No. 04

Using the built-in pathlib module create two objects of the Path class that store the following paths:

    - home directory path + 'reports/2020/01/sales.csv'
    - path to working directory + 'reports/2020/01/sales.csv'

and assign to the variables path1 and path2 respectively.

In response, print the path1 and path2 to the console.

Tip:

    # >>> help(pathlib.Path.joinpath)

    Help on function joinpath in module pathlib:

    joinpath(self, *args)
        Combine this path with one or several arguments, and return a
        new path representing either a subpath (if all arguments are relative
        paths) or a totally different path (if one of the arguments is
        anchored).

Expected result:

    /home/evaluator/reports/2020/01/sales.csv
    /eval/reports/2020/01/sales.csv
"""
from pathlib import Path

path1 = Path.home().joinpath('reports/2020/01/sales.csv')
path2 = Path.cwd().joinpath('reports/2020/01/sales.csv')

print(path1)
print(path2)
