"""
Exercise No. 14

Using the json pakcage, dump the following dictionary:

    stocks = {'PLW': 360, 'TEN': 320.0, 'CDR': 329.0}

To the string, sorted by keys with ident 4. Print the result to the console.

Expected result:

    {
        "CDR": 329.0,
        "PLW": 360,
        "TEN": 320.0
    }
"""
import json

stocks = {'PLW': 360, 'TEN': 320.0, 'CDR': 329.0}

# Solution I
print(json.dumps(stocks, indent=4, sort_keys=True))
