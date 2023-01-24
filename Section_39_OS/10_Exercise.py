"""
Exercise No. 10

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

Using the built-in os module combine the path to the current working directory with the name of each file and assign it
to the paths list.

In response, print paths list to the console.

Tip:
    #>>> help(os.path.join)

    Help on function join in module ntpath:

    join(path, *paths)
        # Join two (or more) paths.

Expected result:
    ['/eval/001_sales.csv', '/eval/002_sales.csv', '/eval/003_sales.csv', '/eval/004_sales.csv', '/eval/005_sales.csv',
    '/eval/006_sales.csv', '/eval/007_sales.csv', '/eval/008_sales.csv', '/eval/009_sales.csv', '/eval/010_sales.csv',
    '/eval/011_sales.csv', '/eval/012_sales.csv', '/eval/013_sales.csv', '/eval/014_sales.csv', '/eval/015_sales.csv',
    '/eval/016_sales.csv', '/eval/017_sales.csv', '/eval/018_sales.csv', '/eval/019_sales.csv', '/eval/020_sales.csv',
    '/eval/021_sales.csv', '/eval/022_sales.csv', '/eval/023_sales.csv', '/eval/024_sales.csv']
"""
import os

fnames = [f"{str(i).zfill(3)}_sales.csv" for i in range(1, 25)]
paths = [os.path.join(os.getcwd(), fname) for fname in fnames]
print(paths)
