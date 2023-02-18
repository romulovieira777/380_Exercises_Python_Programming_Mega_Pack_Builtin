"""
Exercise No. 31

The premiere of a computer game is planned and the option to subscribe to the wish list is opened.

When a user subscribes to the wish list user is added to the deque.

Using the built-in collections module create an empty deque object named wishlist.

Following users subscribed to the wish list in the given order:

    - '003'
    - '001'
    - '004'
    - '002'
    - '005'

Add these users to the wishlist deque.

You should get following object:

    deque(['003', '001', '004', '002', '005'])

Using the appropriate method pop the first subscribed user from this deque and print to the console.

Tip:

    # >>> help(deque.popleft)

    Help on method_descriptor:

    popleft(...)
        Remove and return the leftmost element.

Expected result:

    003
"""
from collections import deque

wishlist = deque()

wishlist.append('003')
wishlist.append('001')
wishlist.append('004')
wishlist.append('002')
wishlist.append('005')

print(wishlist.popleft())
