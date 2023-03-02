"""
Exercise No. 13

The following list of directory paths is given:

    [
        PosixPath("eval/reports/2020/01_sales"),
        PosixPath("eval/reports/2020/02_sales"),
        PosixPath("eval/reports/2020/03_sales"),
        PosixPath("eval/reports/2020/04_sales"),
        PosixPath("eval/reports/2020/05_sales"),
        PosixPath("eval/reports/2020/06_sales"),
        PosixPath("eval/reports/2020/07_sales"),
        PosixPath("eval/reports/2020/08_sales"),
        PosixPath("eval/reports/2020/09_sales"),
        PosixPath("eval/reports/2020/10_sales"),
        PosixPath("eval/reports/2020/11_sales"),
        PosixPath("eval/reports/2020/12_sales"),
    ]

Using the pathlib built-in module create the given directories from this list.

In response print the contents of the eval/reports/2020 directory to the console.

Expected result:

    /eval/reports/2020/01_sales
    /eval/reports/2020/02_sales
    /eval/reports/2020/03_sales
    /eval/reports/2020/04_sales
    /eval/reports/2020/05_sales
    /eval/reports/2020/06_sales
    /eval/reports/2020/07_sales
    /eval/reports/2020/08_sales
    /eval/reports/2020/09_sales
    /eval/reports/2020/10_sales
    /eval/reports/2020/11_sales
    /eval/reports/2020/12_sales
"""
from pathlib import Path

paths = [Path.cwd() / f"reports/2020/{str(i).zfill(2)}_sales" for i in range(1, 13)]

# Solution I
for path in paths:
    path.mkdir(parents=True)

for dir in sorted(path.parent.iterdir()):
    print(dir)


# Solution II
for path in paths:
    path.mkdir(parents=True)

for dir in sorted(Path.cwd().joinpath("reports/2020").iterdir()):
    print(dir)
