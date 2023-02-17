"""
Exercise No. 28

The following deque object is given:

    daynames = deque(['Mon.', 'Tue.', 'Wed.', 'Thu.', 'Fri.', 'Sat.', 'Sun.'])

Using the built-in module and the deque class, move one item forward in the daynames deque, as shown below:

    deque([ 'Sun.', 'Mon.', 'Tue.', 'Wed.', 'Thu.', 'Fri.', 'Sat.'])

In response, print the daynames to the console.

Tip:

    # >>> help(deque.rotate)

    Help on method_descriptor:

    rotate(...)
        Rotate the deque n steps to the right (default n=1).  If n is negative, rotates left.

Expected result:

    deque(['Sun.', 'Mon.', 'Tue.', 'Wed.', 'Thu.', 'Fri.', 'Sat.'])
"""
from collections import deque

daynames = deque(['Mon.', 'Tue.', 'Wed.', 'Thu.', 'Fri.', 'Sat.', 'Sun.'])

daynames.rotate(1)

print(daynames)
