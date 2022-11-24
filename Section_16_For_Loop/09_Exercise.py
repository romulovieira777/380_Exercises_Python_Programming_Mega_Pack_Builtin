"""
Exercise No. 09

The following text is given:

    text = '''Python is powerful... and fast
        plays well with others
        runs everywhere
        is friendly & easy to learn
        is Open
        These are some of the reasons people who use Python would rather not use anything else'''

Create a list of words from the given text. Then standardize this text (change uppercase letters to lowercase, remove
punctuation marks). Extract words longer than six characters and print the result to the console.

Expected result:

    ['powerful', 'everywhere', 'friendly', 'reasons', 'anything']
"""

# Solution I
text = '''Python is powerful... and fast
plays well with others
runs everywhere
is friendly & easy to learn
is Open
These are some of the reasons people who use Python would rather not use anything else'''

words = text.split()
result = []
for word in words:
    if len(word) > 6:
        result.append(word.lower().strip('.&'))
print(result)


# Solution II
text = '''Python is powerful... and fast
plays well with others
runs everywhere
is friendly & easy to learn
is Open
These are some of the reasons people who use Python would rather not use anything else'''

words = text.split()
words = [word.lower() for word in words]
words = [word.replace('.', '').replace(',', '') for word in words]
words = [word for word in words if len(word) > 6]
print(words)
