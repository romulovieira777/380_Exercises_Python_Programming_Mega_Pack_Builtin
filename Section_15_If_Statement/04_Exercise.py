"""
Exercise No. 04

The following password is given:

    password = 'cskdnjcasa#!'

Check if the password has 11 characters.

If so, print 'Password correct', otherwise 'Password too short'.

Expected result:

    Password correct
"""
password = 'cskdnjcasa#!'

if len(password) == 11:
    print('Password correct')
else:
    print('Password too short')
