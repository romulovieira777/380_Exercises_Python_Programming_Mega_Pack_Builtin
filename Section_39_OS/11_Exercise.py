"""
Exercise No. 11

The names of files related to sales in a certain company was generated (fnames list):
    [
        "001_sales.csv",
        "002_sales.csv",
        "003_sales.csv",
        "004_sales.csv",
        "005_sales.csv",
        "006_sales.csv",
        "007_sales.csv",
        "008_sales.csv",
        "009_sales.csv",
        "010_sales.csv",
        "011_sales.csv",
        "012_sales.csv",
        "013_sales.csv",
        "014_sales.csv",
        "015_sales.csv",
        "016_sales.csv",
        "017_sales.csv",
        "018_sales.csv",
        "019_sales.csv",
        "020_sales.csv",
        "021_sales.csv",
        "022_sales.csv",
        "023_sales.csv",
        "024_sales.csv",
    ]

The path to the working directory:
    /eval

Using the built-in os module transform the names of the files (fnames list).

Set the first 12 files to directory called 2020, the next 12 files to directory called 2021. Assign absolute paths to
the paths variable (list).

In response, print each path as shown below.

Tip:
    #>>> help(os.path.join)

    Help on function join in module ntpath:

    join(path, *paths)
        # Join two (or more) paths.

Expected result:
    /eval/2020/01_sales.csv
    /eval/2020/02_sales.csv
    /eval/2020/03_sales.csv
    /eval/2020/04_sales.csv
    /eval/2020/05_sales.csv
    /eval/2020/06_sales.csv
    /eval/2020/07_sales.csv
    /eval/2020/08_sales.csv
    /eval/2020/09_sales.csv
    /eval/2020/10_sales.csv
    /eval/2020/11_sales.csv
    /eval/2020/12_sales.csv
    /eval/2021/13_sales.csv
    /eval/2021/14_sales.csv
    /eval/2021/15_sales.csv
    /eval/2021/16_sales.csv
    /eval/2021/17_sales.csv
    /eval/2021/18_sales.csv
    /eval/2021/19_sales.csv
    /eval/2021/20_sales.csv
    /eval/2021/21_sales.csv
    /eval/2021/22_sales.csv
    /eval/2021/23_sales.csv
    /eval/2021/24_sales.csv
"""
import os

fnames = [f"{str(i).zfill(3)}_sales.csv" for i in range(1, 25)]
base_dir = '/eval'
paths = [
    os.path.join(os.getcwd(), "2020", fname)
    if idx < 12
    else os.path.join(os.getcwd(), "2021", fname)
    for idx, fname in enumerate(fnames)
]

for path in paths:
    print(path)
