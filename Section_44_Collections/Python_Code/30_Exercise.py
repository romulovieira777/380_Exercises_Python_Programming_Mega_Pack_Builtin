"""
Exercise No. 30

The following deque object is given:

    daynames = deque(['Mon.', 'Tue.', 'Wed.', 'Thu.', 'Fri.', 'Sat.', 'Sun.'])

Using the built-in collections module and the deque class reverse the order of the daynames queue as shown below:

    deque(['Sun.', 'Sat.', 'Fri.', 'Thu.', 'Wed.', 'Tue.', 'Mon.'])

Then, using the appropriate method pop the first element out of this deque and print to the console.

Tip:

    # >>> help(deque.reverse)

    Help on method_descriptor:

    reverse(...)
        D.reverse() -- reverse *IN PLACE*
    # >>> help(deque.popleft)

    Help on method_descriptor:

    popleft(...)
        Remove and return the leftmost element.

Expected result:

    Sun.
"""
from collections import deque

daynames = deque(['Mon.', 'Tue.', 'Wed.', 'Thu.', 'Fri.', 'Sat.', 'Sun.'])

daynames.reverse()

print(daynames.popleft())
