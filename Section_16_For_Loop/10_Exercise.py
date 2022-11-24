"""
Exercise No. 10

The list of stock indexes is given:

    indexes = [
        "BOVESPA",
        "DOW JONES COMP",
        "DOW JONES INDU",
        "DOW JONES TRANS",
        "DOW JONES UTIL",
        "IPC",
        "IPSA",
        "MERVAL",
        "NASDAQ COMP",
        "NASDAQ100",
        "S&P500",
        "S&P/TSX COMP",
    ]

Iterate through the indexes list and print to the console only those indexes containing 'DOW' or 'S&P'.

Expected result:

    DOW JONES COMP
    DOW JONES INDU
    DOW JONES TRANS
    DOW JONES UTIL
    S&P500
    S&P/TSX COMP
"""
indexes = [
    "BOVESPA",
    "DOW JONES COMP",
    "DOW JONES INDU",
    "DOW JONES TRANS",
    "DOW JONES UTIL",
    "IPC",
    "IPSA",
    "MERVAL",
    "NASDAQ COMP",
    "NASDAQ100",
    "S&P500",
    "S&P/TSX COMP",
]

for index in indexes:
    if 'DOW' in index or 'S&P' in index:
        print(index)
