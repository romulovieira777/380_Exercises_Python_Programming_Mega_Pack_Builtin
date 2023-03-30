"""
Exercise No. 30

The following list is given:

    fnames = [
        '01_image.jpg',
        '02_image.png',
        '03_image.jpg',
        '04_image.jpg',
        '05_image.jpg',
        '06_image.png',
        '07_image.jpg',
        '08_image.jpg',
    ]

Using the built-in itertools module and the groupby class, group the names of files (properly sort the data before
grouping) into files with the extension jpg and png. Use extension as a grouping keys.

In response, print the keys and the group of names assigned to the appropriate as shown below.

Tip:

    #>>> help(itertools.groupby)

    Help on class groupby in module itertools:

    class groupby(builtins.object)
        |  groupby(iterable, key=None)
        |
        |  make an iterator that returns consecutive keys and groups from the iterable
        |
        |  iterable
        |    Elements to divide into groups according to the key function.
        |  key
        |    A function for computing the group category for each element.
        |    If the key function is not specified or is None, the element itself
        |    is used for grouping.

Expected result:

    jpg -> ['01_image.jpg', '03_image.jpg', '04_image.jpg', '05_image.jpg', '07_image.jpg', '08_image.jpg']
    png -> ['02_image.png', '06_image.png']
"""
import itertools

fnames = [
    '01_image.jpg',
    '02_image.png',
    '03_image.jpg',
    '04_image.jpg',
    '05_image.jpg',
    '06_image.png',
    '07_image.jpg',
    '08_image.jpg',
]

func = lambda x: x.split('.')[1]
sorted_fnames = sorted(fnames, key=func)
grouped_fnames = itertools.groupby(sorted_fnames, key=func)

for key, group in grouped_fnames:
    print(f'{key} -> {list(group)}')
