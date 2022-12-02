"""
Exercise No. 02

The following dictionary:

    stocks = {'PLW': ['Playway', 350], 'BBT': ['Boombit', 22]}

Save to stocks.json usingthe json package. Set the ident to 4.

File stocks.json after saving:

    {
        "PLW": [
            "Playway",
            350
        ],
        "BBT": [
            "Boombit",
            22
        ]
    }
"""
import json

stocks = {'PLW': ['Playway', 350], 'BBT': ['Boombit', 22]}

with open('../File/stocks.json', 'w') as file:
    json.dump(stocks, file, indent=4)
