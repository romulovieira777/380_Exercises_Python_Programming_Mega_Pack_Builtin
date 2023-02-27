"""
Exercise No. 06

Using the built-in pathlib module an object of the Path class was created to store the path:

    - home directory path + 'reports/2020/01/sales.csv'

and assign to the path variable. Examine the value of the parents attribute for this object. Then, iterating over this
attribute, print each element to the console.

Tip:

    # >>> help(pathlib.Path.parents)

    Help on property:

        A sequence of this path's logical parents.

Expected result:

    /home/evaluator/reports/2020/01
    /home/evaluator/reports/2020
    /home/evaluator/reports
    /home/evaluator
    /home
    /
"""
from pathlib import Path

path = Path.home().joinpath('reports/2020/01/sales.csv')

for parent in path.parents:
    print(parent)
