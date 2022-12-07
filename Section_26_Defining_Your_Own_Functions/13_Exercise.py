"""
Exercise No. 13

Implement the function is_palindrome(), which takes as an argument str object and checks if this object is a palindrome
(expression that sounds the same from left to right and from right to left).

If so, the function should return True, on the contrary False.

Example:

    [IN]: is_palindrome('level')
    [OUT]: True

    [IN]: is_palindrome('python')
    [OUT]: False

Note: The function should be case insensitive.
"""


# Solution I
def is_palindrome(string):
    string = string.lower()
    return string == string[::-1]


print(is_palindrome('level'))
print(is_palindrome('python'))


# Solution II
def is_palindrome(string):
    inverse = string[::-1]
    if string == inverse:
        return True
    else:
        return False


print(is_palindrome('level'))
print(is_palindrome('python'))
