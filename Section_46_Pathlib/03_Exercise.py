"""
Exercise No. 03

Using the built-in pathlib module create an instance of the Path class assign the following path:

    /home/evaluator/reports/2020/01/sales.csv

to the path variable. In response, print the path variable to the console.

Tip:

    # >>> help(pathlib.Path)

    Help on class Path in module pathlib:

    class Path(PurePath)
     |  PurePath subclass that can make system calls.
     |
     |  Path represents a filesystem path but unlike PurePath, also offers
     |  methods to do system calls on path objects. Depending on your system,
     |  instantiating a Path will return either a PosixPath or a WindowsPath
     |  object. You can also instantiate a PosixPath or WindowsPath directly,
     |  but cannot instantiate a WindowsPath on a POSIX system or vice versa.

Expected result:

    /home/evaluator/reports/2020/01/sales.csv
"""
from pathlib import Path

path = Path('/home/evaluator/reports/2020/01/sales.csv')
print(path)
