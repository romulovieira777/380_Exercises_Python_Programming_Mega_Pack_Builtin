"""
Exercise No. 07

The following tuple is given:

    stocks = (
        ("Apple Inc", ("AAPL.US", 310)),
        ("Microsoft Corp", ("MSFT.US", 184)),
    )

Extract a ticker for Apple and print the result to the console.

Expected result:

    AAPL.US
"""
stocks = (
    ("Apple Inc", ("AAPL.US", 310)),
    ("Microsoft Corp", ("MSFT.US", 184)),
)

print(stocks[0][1][0])
