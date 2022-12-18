"""
Exercise No. 01

The gaming.txt file is attached to this exercise. This file has been loaded into the text variable. From the text list
delete all newline characters. Then delete empty lines and print the text to the console.

text before:

    ['Activision Blizzard\n',
     '\n',
     'Activision Blizzard, Inc. is a developer and publisher of interactive entertainment content and services. The Companydevelops and distributes content and services across various gaming platforms,\n',
     'including video game consoles, personal computers (PC) and mobile devices. Its segments include Activision Publishing, Inc. (Activision), Blizzard Entertainment, Inc. (Blizzard),\n',
     'King Digital Entertainment (King) and Other. Activision is a developer and publisher of interactive software products and content. Blizzard is engaged in developing and publishing of interactive\n',
     'software products and entertainment content, particularly in PC gaming. King is a mobile entertainment company. It is engaged in other businesses, including The Major League Gaming (MLG) business;\n',
     'The Activision Blizzard Studios (Studios) business, and The Activision Blizzard Distribution (Distribution) business. It also develops products spanning other genres, including action/adventure,\n',
     'role-playing and simulation.']

text after:

    ['Activision Blizzard',
     'Activision Blizzard, Inc. is a developer and publisher of interactive entertainment content and services. The Company develops and distributes content and services across various gaming platforms,',
     'including video game consoles, personal computers (PC) and mobile devices. Its segments include Activision Publishing, Inc. (Activision), Blizzard Entertainment, Inc. (Blizzard),',
     'King Digital Entertainment (King) and Other. Activision is a developer and publisher of interactive software products and content. Blizzard is engaged in developing and publishing of interactive',
     'software products and entertainment content, particularly in PC gaming. King is a mobile entertainment company. It is engaged in other businesses, including The Major League Gaming (MLG) business;',
     'The Activision Blizzard Studios (Studios) business, and The Activision Blizzard Distribution (Distribution) business. It also develops products spanning other genres, including action/adventure,',
     'role-playing and simulation.']

Expected result:

    ['Activision Blizzard', 'Activision Blizzard, Inc. is a developer and publisher of interactive entertainment content and services. The Company develops and distributes content and services across various gaming platforms,', 'including video game consoles, personal computers (PC) and mobile devices. Its segments include Activision Publishing, Inc. (Activision), Blizzard Entertainment, Inc. (Blizzard),', 'King Digital Entertainment (King) and Other. Activision is a developer and publisher of interactive software products and content. Blizzard is engaged in developing and publishing of interactive', 'software products and entertainment content, particularly in PC gaming. King is a mobile entertainment company. It is engaged in other businesses, including The Major League Gaming (MLG) business;', 'The Activision Blizzard Studios (Studios) business, and The Activision Blizzard Distribution (Distribution) business. It also develops products spanning other genres, including action/adventure,', 'role-playing and simulation.']
"""
# Solution I
with open('../Files/gaming.txt', 'r') as file:
    text = file.readlines()
text = [line.strip() for line in text if line.strip()]
print(text)

# Solution II
with open('../Files/gaming.txt', 'r') as file:
    text = file.readlines()
text = [line.replace('\n', '') for line in text]
text = [line for line in text if len(line) > 0]
print(text)
