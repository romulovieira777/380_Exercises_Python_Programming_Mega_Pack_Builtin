"""
Exercise No. 05

Using the built-in pathlib module an object of the Path class was created to store the path:

    - home directory path + 'reports/2020/01/sales.csv'

and assigned to the path variable.

As an answer print to the console.

    - whole path (path variable)
    - value of the parent attribute
    - value of the name attribute
    - value of the stem attribute
    - value of the suffix attribute
    - value of the parts attribute

Tip:

    #  >>> help(pathlib.Path.parent)
    Help on property:

        The logical parent of the path.


    # >>> help(pathlib.Path.name)
    Help on property:

        The final path component, if any.


    # >>> help(pathlib.Path.stem)
    Help on property:

        The final path component, minus its last suffix.


    # >>> help(pathlib.Path.suffix)
    Help on property:

        The final component's last suffix, if any.


    # >>> help(pathlib.Path.parts)
    Help on property:

        An object providing sequence-like access to the
        components in the filesystem path.

Expected result:

    /home/evaluator/reports/2020/01/sales.csv
    /home/evaluator/reports/2020/01
    sales.csv
    sales
    .csv
    ('/', 'home', 'evaluator', 'reports', '2020', '01', 'sales.csv')
"""
from pathlib import Path

path = Path.home().joinpath('reports/2020/01/sales.csv')

print(path)
print(path.parent)
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parts)
