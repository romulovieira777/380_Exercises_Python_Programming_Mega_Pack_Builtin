"""
Exercise No. 05

The contents of the file plw.txt were loaded as follows:

    with open('plw.txt', 'r') as file:
        lines = file.read().splitlines()

lines variable:

    ['PLAYWAY',
     '',
     'PlayWay is a producer and publisher of computer and mobile games. The company is characterized by a very large number of development teams and a large number of games produced simultaneously.',
     "PlayWay sells, among others via the STEAM portal, AppStore and GooglePlay. The US and German markets are the two largest markets for the Group's sales.",
     'In addition, the company has PlayWay Campus - a campus for cooperating development teams.']

Tasks to perform:

    1. Get rid of blank lines.
    2. Split each line into tokens/words as shown below and print the result to the console.

Formatted result:

    [['PLAYWAY'],
 ['PlayWay',
  'is',
  'a',
  'producer',
  'and',
  'publisher',
  'of',
  'computer',
  'and',
  'mobile',
  'games.',
  'The',
  'company',
  'is',
  'characterized',
  'by',
  'a',
  'very',
  'large',
  'number',
  'of',
  'development',
  'teams',
  'and',
  'a',
  'large',
  'number',
  'of',
  'games',
  'produced',
  'simultaneously.'],
 ['PlayWay',
  'sells,',
  'among',
  'others',
  'via',
  'the',
  'STEAM',
  'portal,',
  'AppStore',
  'and',
  'GooglePlay.',
  'The',
  'US',
  'and',
  'German',
  'markets',
  'are',
  'the',
  'two',
  'largest',
  'markets',
  'for',
  'the',
  "Group's",
  'sales.'],
 ['In',
  'addition,',
  'the',
  'company',
  'has',
  'PlayWay',
  'Campus',
  '-',
  'a',
  'campus',
  'for',
  'cooperating',
  'development',
  'teams.']]

Expected result:

    [['PLAYWAY'], ['PlayWay', 'is', 'a', 'producer', 'and', 'publisher', 'of', 'computer', 'and', 'mobile', 'games.',
      'The', 'company', 'is', 'characterized', 'by', 'a', 'very', 'large', 'number', 'of', 'development', 'teams',
      'and', 'a', 'large', 'number', 'of', 'games', 'produced', 'simultaneously.'], ['PlayWay', 'sells,', 'among',
      'others', 'via', 'the', 'STEAM', 'portal,', 'AppStore', 'and', 'GooglePlay.', 'The', 'US', 'and', 'German',
      'markets', 'are', 'the', 'two', 'largest', 'markets', 'for', 'the', "Group's", 'sales.'], ['In', 'addition,',
      'the', 'company', 'has', 'PlayWay', 'Campus', '-', 'a', 'campus', 'for', 'cooperating', 'development', 'teams.']]
"""
# Solution I
with open('../Files/plw.txt', 'r') as file:
    lines = file.read().splitlines()

lines = [line for line in lines if line != '']
lines = [line.split() for line in lines]
print(lines)


# Solution II
with open('../Files/plw.txt', 'r') as file:
    lines = file.read().splitlines()

lines = [line for line in lines if len(line) > 0]
lines = [line.split() for line in lines]
print(lines)
