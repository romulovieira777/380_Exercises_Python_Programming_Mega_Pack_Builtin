"""
Exercise No. 05

Two customer ID sets are given. The first one tells you whether a person clicked on the banner ad. Second. whether the
person purchased the product:

    is_clicked = {'9001', '9002', '9005'}
    is_bought = {'9002', '9004', '9005'}

Return the ID of those customers who clicked on the ad and bought the product.

Expected result:

    Customer ID: {'9005', '9002'}

Note: Remember that the set is an unordered data structure. You may get a different order of items than the expected
result. You don't have to worry about it.
"""

# Solutio I
is_clicked = {'9001', '9002', '9005'}
is_bought = {'9002', '9004', '9005'}

customer_id = is_clicked & is_bought
print(f"Customer ID: {customer_id}")


# Solution II
is_clicked = {'9001', '9002', '9005'}
is_bought = {'9002', '9004', '9005'}

customer_id = is_clicked.intersection(is_bought)
print(f"Customer ID: {customer_id}")
