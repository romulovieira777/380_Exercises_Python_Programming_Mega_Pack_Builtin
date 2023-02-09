"""
Exercise No. 16

Using the built-in collections module and the namedtuple() function, a class named Point was implemented.

Then the following points were created:

    - pt1 - Point(3, 4)
    - pt2 - Point(-2, 6)

Find the midpoint of the segment at points pt1 and pt2 and print the result to the console.

Tip:

    #>>> help(namedtuple)

    Help on function namedtuple in module collections:

    namedtuple(typename, field_names, *, verbose=False, rename=False, module=None)
        Returns a new subclass of tuple with named fields.

Expected result:

    Point(x=0.5, y=5.0)
"""
from collections import namedtuple

Point = namedtuple(typename='Point', field_names=['x', 'y'])

pt1 = Point(3, 4)
pt2 = Point(-2, 6)

midpoint = Point((pt1.x + pt2.x) / 2, (pt1.y + pt2.y) / 2)

print(midpoint)
