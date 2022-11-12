"""
Exercise No. 02

The following tuples are given:

    dji1 = ('AAPL.US', 'IBM.US', 'MSFT.US')
    dji2 = ('HD.US', 'GS.US', 'NKE.US')

Nest these tuples into one as shown below and print the result to the console.

Expected result:

    ('AAPL.US', 'IBM.US', 'MSFT.US', ('HD.US', 'GS.US', 'NKE.US'))
"""
dji1 = ('AAPL.US', 'IBM.US', 'MSFT.US')
dji2 = ('HD.US', 'GS.US', 'NKE.US')

dj = (dji1,) + (dji2,)
print(dj)
