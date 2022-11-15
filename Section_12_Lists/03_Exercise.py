"""
Exercise No. 03

The following text is given:

    text = 'Python programming'

Standardize the text (replace uppercase letters with lowercase). Then create a list of unique characters in the text.
Remove the space from this list and sort from a to z. After all print the list to the console.

Tip: You can use a set to generate unique characters.

Expected result:

    ['a', 'g', 'i', 'm', 'n', 'o', 'p', 'r', 't', 'y']
"""
text = 'Python programming'

text = text.lower()
text = set(text)
text.remove(' ')
text = sorted(text)
print(text)
