"""
Exercise No. 06

Do this exercise in the command line.

Using the built-in sys module create a script called redirection.py which redirects standard output to the file called
'logs.txt' and write to it the result of the following code:
    print('Logging...')
    print('Connecting...')
    print('Closing...')

Then return to the default settings (default stdout) and print the text to console:
    'Completed successfully!'
"""
import sys

saved_stdout = sys.stdout

file = open('logs.txt', 'w')
sys.stdout = file

print('Logging...')
print('Connecting...')
print('Closing...')

file.close()

sys.stdout = saved_stdout
print('Completed successfully')
