"""
Exercise No. 09

Using the four print() function (one line - one function), print the following text:

    ========================================
    author: johnsmith@sample.com
    date: 01-01-2021
    ========================================

Tip: The lines consist of 40 equal signs: '='.
"""
from datetime import date

print('=' * 40)
print('author: romulo.vieira777')
print(f'date: {format(date.today(), "%d-%m-%Y")}')
print('=' * 40)
