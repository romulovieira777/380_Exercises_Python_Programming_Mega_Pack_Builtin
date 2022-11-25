"""
Exercise No. 02

The following list of hashtags is given:

    hashtags = ["holliday", "sport", "fit", None, "fashion"]

Check if all objects in the list are of str type. If so, print True, otherwise, print False. Use the break statement in
your.

Expected result:

    False
"""

# Solution I
hashtags = ["holliday", "sport", "fit", None, "fashion"]

for item in hashtags:
    if type(item) != str:
        print(False)
        break


# Solution II
hashtags = ["holliday", "sport", "fit", None, "fashion"]

for hashtag in hashtags:
    if not isinstance(hashtag, str):
        result = False
        break
print(result)
