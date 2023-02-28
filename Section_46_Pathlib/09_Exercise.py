"""
Exercise No. 09

Using the built-in pathlib module create Path instance that store following path names:

    [
        PosixPath("eval/reports/2020/01"),
        PosixPath("eval/reports/2020/02"),
        PosixPath("eval/reports/2020/03"),
        PosixPath("eval/reports/2020/04"),
        PosixPath("eval/reports/2020/05"),
        PosixPath("eval/reports/2020/06"),
        PosixPath("eval/reports/2020/07"),
        PosixPath("eval/reports/2020/08"),
        PosixPath("eval/reports/2020/09"),
        PosixPath("eval/reports/2020/10"),
        PosixPath("eval/reports/2020/11"),
        PosixPath("eval/reports/2020/12"),
    ]

And assign to paths variable (try to automate the solution, don't enter the names manually).

Then create all directories for the paths in the paths list.

In response, list all directories in the directory named 2020 (eval/reports/2020) sorted alphabetically.

Tip:

    #  >>> help(pathlib.Path.mkdir)

    Help on function mkdir in module pathlib:

    mkdir(self, mode=511, parents=False, exist_ok=False)
        Create a new directory at this given path.


    # >>> help(path.parent.iterdir)

    Help on method iterdir in module pathlib:

    iterdir() method of pathlib.PosixPath instance
        Iterate over the files in this directory.  Does not yield any
        result for the special paths '.' and '..'.

Expected result:

    /eval/reports/2020/01
    /eval/reports/2020/02
    /eval/reports/2020/03
    /eval/reports/2020/04
    /eval/reports/2020/05
    /eval/reports/2020/06
    /eval/reports/2020/07
    /eval/reports/2020/08
    /eval/reports/2020/09
    /eval/reports/2020/10
    /eval/reports/2020/11
    /eval/reports/2020/12
"""
from pathlib import Path

paths = [
    Path.cwd() / f"reports/2020/{str(i).zfill(2)}"
    for i in range(1, 13)
]

for path in paths:
    path.mkdir(parents=True)

for dir in sorted(path.parent.iterdir()):
    print(dir)
