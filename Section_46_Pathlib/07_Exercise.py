"""
Exercise No. 07

Using the built-in pathlib module check if the directory named reports exists in your working directory.

If not, create this directory. Then list all files / directories in your working directory sorted alphabetically.

Print the result to the console as shown below.

Tip:

    # >>> help(pathlib.Path.is_dir)
    Help on function is_dir in module pathlib:

    is_dir(self)
        Whether this path is a directory.


    # >>> help(pathlib.Path.mkdir)

    Help on function mkdir in module pathlib:

    mkdir(self, mode=511, parents=False, exist_ok=False)
        Create a new directory at this given path.


    # >>> help(pathlib.Path.iterdir)

    Help on function iterdir in module pathlib:

    iterdir(self)
        Iterate over the files in this directory.  Does not yield any
        result for the special paths '.' and '..'.

Expected result:

    /eval/__pycache__
    /eval/evaluate.py
    /eval/exercise.py
    /eval/reports
    /eval/result.py
    /eval/run_unittest.py
"""
from pathlib import Path

# Solution I
if not Path.cwd().joinpath('reports').is_dir():
    Path.cwd().joinpath('reports').mkdir()

for file in sorted(Path.cwd().iterdir()):
    print(file)


# Solution II
path = Path.cwd() / 'reports'

if not path.is_dir():
    path.mkdir()

for item in sorted(Path.cwd().iterdir()):
    print(item)
