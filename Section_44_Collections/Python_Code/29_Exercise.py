""""
Exercise No. 29

The following deque object is given:

    daynames = deque(['Mon.', 'Tue.', 'Wed.', 'Thu.', 'Fri.', 'Sat.', 'Sun.'])

Using the built-in collections module and the deque class, shift three items back in the daynames deque, as shown below:

    deque(['Thu.', 'Fri.', 'Sat.', 'Sun.', 'Mon.', 'Tue.', 'Wed.'])

Then, using the appropriate method pop the last element out of this deque and print to the console.

Tip:

    # >>> help(deque.pop)

    Help on method_descriptor:

    pop(...)
        Remove and return the rightmost element.

Expected result:

    Wed.
"""
from collections import deque

daynames = deque(['Mon.', 'Tue.', 'Wed.', 'Thu.', 'Fri.', 'Sat.', 'Sun.'])

daynames.rotate(-3)

print(daynames.pop())
