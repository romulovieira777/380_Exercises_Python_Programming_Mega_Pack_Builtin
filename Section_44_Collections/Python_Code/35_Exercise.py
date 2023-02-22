"""
Exercise No. 35

The premiere of a computer game is planned and the option to subscribe to the wish list is opened. When a user subscribes
to the wish list user is added to the deque.

Following users subscribed to the wish list in the given order:

    - '003'
    - '001'
    - '004'
    - '002'
    - '005'

Using the collections built-in module a deque object named wishlist is created based on the data from the user_ids.
Extend the wishlist with three additional users: '007', '009', '010'.

In response, print the wishlist to the console.

Tip:

    # >>> help(deque.extend)

    Help on method_descriptor:

    extend(...)
        Extend the right side of the deque with elements from the iterable

Expected result:

    deque(['003', '001', '004', '002', '005', '007', '009', '010'])
"""
from collections import deque

user_ids = ['003', '001', '004', '002', '005']

wishlist = deque(user_ids)

wishlist.extend(['007', '009', '010'])

print(wishlist)
