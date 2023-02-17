"""
Exercise no. 27

The following list is given:

    ['Tue.', 'Wed.', 'Thu.', 'Fri.', 'Sat.']

Using the collections built-in module create a double-ended queue object (deque) from the given list and assign it to
the daynames variable. Then add the item 'Mon.' at the beginning and the element 'Sun.' at the end of the daynames
object.

In response, print the daynames deque to the console.

Tip:

    # >>> help(deque)

    Help on class deque in module collections:

    class deque(builtins.object)
     |  deque([iterable[, maxlen]]) --> deque object
     |
     |  A list-like sequence optimized for data accesses near its endpoints.

Expected result:

    deque(['Mon.', 'Tue.', 'Wed.', 'Thu.', 'Fri.', 'Sat.', 'Sun.'])
"""
from collections import deque

daynames = deque(['Tue.', 'Wed.', 'Thu.', 'Fri.', 'Sat.'])

daynames.appendleft('Mon.')
daynames.append('Sun.')

print(daynames)
