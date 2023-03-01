"""
Exercise No. 12

The following directories were created:

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

Using the pathlib module change the names of directories 01-12 to the names 01_sales - 12_sales.

In response, print the names of the directories in the /eval/reports/2020 directory, sorted alphabetically to the
console.

Tip:

    # >>> help(pathlib.Path.rename)

    Help on function rename in module pathlib:

    rename(self, target)
        Rename this path to the given path.

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

paths = [Path.cwd() / f"eval/reports/2020/{i:02d}" for i in range(1, 13)]

# Solution I
for path in paths:
    path.mkdir(parents=True)

for path in paths:
    path.rename(path.with_name(f"{path.name}_sales"))

for dir in sorted(path.parent.iterdir()):
    print(dir)


# Solution II
for path in paths:
    path.mkdir(parents=True)

targets = [Path.cwd() / f"reports/2020/{str(i).zfill(2)}_sales" for i in range(1, 13)]

for path, target in zip(paths, targets):
    path.rename(target)

for dir in sorted(Path.cwd().joinpath("reports/2020").iterdir()):
    print(dir)
