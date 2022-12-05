"""
Exercise No. 04

Two tuples are given:

    ticker = ('TEN', 'PLW', 'CDR')
    full_name = ('Ten Square Games', 'Playway', 'CD Projekt')

Using the appropriate function, create a list consisting of tuples (ticker, full_name) and print the result to the
console as shown below.

Tip: Use the zip() function.

Expected result:

    [('TEN', 'Ten Square Games'), ('PLW', 'Playway'), ('CDR', 'CD Projekt')]
"""
ticker = ('TEN', 'PLW', 'CDR')
full_name = ('Ten Square Games', 'Playway', 'CD Projekt')

print(list(zip(ticker, full_name)))
