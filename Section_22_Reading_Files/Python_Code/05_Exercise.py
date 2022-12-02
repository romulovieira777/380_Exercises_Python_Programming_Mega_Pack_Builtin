"""
Exercise No. 05

The playway.csv file contains Playway's listing for March 2020. This file was loaded as follows to the content variable:

    with open('playway.csv', 'r') as file:
        content = file.read().splitlines()

content:

    [
        'Date,Open,High,Low,Close,Volume',
        '2020-03-02,305,324.5,283.5,310,64081',
        '2020-03-03,325.5,340.5,320,340.5,55496',
        '2020-03-04,324,340.5,315,330,36152',
        '2020-03-05,344,344,310,315,35992',
        '2020-03-06,306.5,307,291,305,32539',
        '2020-03-09,274,291,250,258,79402',
        '2020-03-10,278,284.5,256,264,35700',
        '2020-03-11,270,270,238.5,245,60445',
        '2020-03-12,218,228,196,197,94031',
        '2020-03-13,210,229,198.8,211,100412',
        '2020-03-16,205,248,197.8,240.5,50659',
        '2020-03-17,245,269,232.5,264,99480',
        '2020-03-18,264,280,251,270,70136',
        '2020-03-19,267,280,267,279.5,30732',
        '2020-03-20,297.5,307,280,280.5,43426',
        '2020-03-23,274,289,258,285,37098',
        '2020-03-24,305,309,296.5,309,31939',
        '2020-03-25,313,330,295,304,46724',
        '2020-03-26,300,309,295.5,300,27213',
        '2020-03-27,302,306.5,290,296,13466',
        '2020-03-30,299,300,287,300,10316',
        '2020-03-31,302.5,309,302,306.5,15698'
    ]

Find the day with the highest volume value for the given month and print the result to the console as shown below:

Formatted result:

    Date: 2020-03-13
"""

# Solution I
with open('../Files/playway.csv', 'r') as file:
    content = file.read().splitlines()

    # Remove the header
    content.pop(0)

    # Create a list of lists
    content = [line.split(',') for line in content]

    # Create a list of volumes
    volumes = [float(line[5]) for line in content]

    # Find the max volume
    max_vol = max(volumes)

    # Find the index of the max volume
    index = volumes.index(max_vol)

    # Find the date
    date = content[index][0]

    print(f'Date: {date}')


# Solution II
with open('../Files/playway.csv', 'r') as file:
    content = file.read().splitlines()

data = [
    (line.split(",")[0], line.split(",")[-1]) for line in content
][1:]

data = [(val[0], int(val[1])) for val in data]
max_vol = max([val[1] for val in data])
max_date = list(filter(lambda val: val[1] == max_vol, data))[0][0]
print(f'Date: {max_date}')