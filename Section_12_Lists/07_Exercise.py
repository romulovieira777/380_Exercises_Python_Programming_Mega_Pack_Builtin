"""
Exercise No. 07

The following list is given:

    hashtags = ['summer', 'time', 'vibes']

using the appropriate method, combine the elements of the list with the '#' character. Also add this sign to the
beginning of the text and print the result to the console as shown below.

Expected result:

    '#summer#time#vibes'
"""
hashtags = ['summer', 'time', 'vibes']
hashtags = '#' + '#'.join(hashtags)
print(hashtags)
