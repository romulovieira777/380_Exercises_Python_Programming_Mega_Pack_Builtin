"""
Exercise No. 14

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

To the given paths, right after the directory with the year 2020, add a directory with the name of the quarter,
respectively: Q1, Q2, Q3, Q4 depending on the month number and assign it to the variable targets.

Print each path in the targets list to the console as shown below.

Expected result:

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
"""
from pathlib import Path

paths = [Path.cwd() / f"reports/2020/{str(i).zfill(2)}_sales" for i in range(1, 13)]

t = 3

targets = [Path.cwd() / f"reports/2020/Q{i // t}/{str(i - t + 1).zfill(2)}_sales" for i in range(t, t + 12)]

for target in targets:
    print(target)
