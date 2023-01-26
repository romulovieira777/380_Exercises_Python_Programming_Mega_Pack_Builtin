"""
Exercise No. 02

Using the sys built-in module print the path list where Python looks for modules.

Expected result:
    [
        '/eval', '/usr/lib/python38.zip', '/usr/lib/python3.8', '/usr/lib/python3.8/lib-dynload',
        '/usr/local/lib/python3.8/dist-packages', '/usr/lib/python3/dist-packages'
    ]
"""
import sys

print(sys.path)
