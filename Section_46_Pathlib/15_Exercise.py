"""
Exercise No. 15

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

Using the pathlib built-in module, the given directories were created. Then the decision was made to change the
directory structure by adding the name of the quarter after the 2020 directory. For this purpose, a targets list was
created, which stores the target path names.

    /eval/reports/2020/Q1/01_sales
    /eval/reports/2020/Q1/02_sales
    /eval/reports/2020/Q1/03_sales
    /eval/reports/2020/Q2/04_sales
    /eval/reports/2020/Q2/05_sales
    /eval/reports/2020/Q2/06_sales
    /eval/reports/2020/Q3/07_sales
    /eval/reports/2020/Q3/08_sales
    /eval/reports/2020/Q3/09_sales
    /eval/reports/2020/Q4/10_sales
    /eval/reports/2020/Q4/11_sales
    /eval/reports/2020/Q4/12_sales

Using the pathlib built-in module change the directory structure as shown in the targets list.

In response, print all directories in the /reports/2020 directory to the console.

Expected result:

    /eval/reports/2020/Q1
    /eval/reports/2020/Q2
    /eval/reports/2020/Q3
    /eval/reports/2020/Q4
"""
from pathlib import Path

paths = [Path.cwd() / f"reports/2020/{str(i).zfill(2)}_sales" for i in range(1, 13)]

for path in paths:
    path.mkdir(parents=True)

t = 3

targets = [Path.cwd() / f"reports/2020/Q{str(i // t)}/{str(i - t + 1).zfill(2)}_sales" for i in range(t, t + 12)]

for target in targets:
    if not target.parent.is_dir():
        target.mkdir(parents=True)

for path, target in zip(paths, targets):
    path.rename(target)

for dir in sorted(Path.cwd().joinpath("reports/2020").iterdir()):
    print(dir)
