"""
Exercise No. 34

The premiere of a computer game is planned and the option to subscribe to the wish list is opened. When a user subscribes
to the wish list user is added to the deque.

Using the built-in collections module create an empty deque object named wishlist with the maximum length of three
elements.

Following users subscribed to the wish list in the given order:

    - '003'
    - '001'
    - '004'
    - '006'
    - '002'
    - '005'

Add these users to the wishlist deque. In response, print wishlist deque to the console each time you add a user as
shown below.

Tip:

    # >>> help(deque.maxlen)

    Help on getset descriptor collections.deque.maxlen:

    maxlen
        maximum size of a deque or None if unbounded

Expected result:

    deque(['003'], maxlen=3)
    deque(['003', '001'], maxlen=3)
    deque(['003', '001', '004'], maxlen=3)
    deque(['001', '004', '006'], maxlen=3)
    deque(['004', '006', '002'], maxlen=3)
    deque(['006', '002', '005'], maxlen=3)
"""
from collections import deque

user_ids = ['003', '001', '004', '006', '002', '005']

wishlist = deque(maxlen=3)

for user_id in user_ids:
    wishlist.append(user_id)
    print(wishlist)
