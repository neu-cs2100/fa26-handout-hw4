"""HW4 Question 3


Please write a class Receipt that accumulates line items and can compute totals across a 
variable number of prices at once.

Requirements:

The constructor should take and store the name of the store and initialize an empty internal list 
    of (item: str, price: float) entries.
A method add_items(self, *items: tuple[str, float]) -> None that accepts a variable number of 
    (item, price) tuples and appends all of them to the internal list in a single call.
A method total(self, *categories: str) -> float that accepts a variable number of category 
    names (matched against item names) and returns the sum of prices for only the matching 
    items. If no categories are passed, it should return the total of all items.
The __str__(self) -> str method should return a formatted string listing every item and its 
    price, plus the grand total. The format of the output is up to you.
The __eq__(self, other: object) -> bool method should return True if the other object is a 
    Receipt with the same store name and identical list of (item, price) entries, and False 
    otherwise.

Make sure to write tests in test_q3.py.

Example usage:

receipt = Receipt("Corner Market")
receipt.add_items(("Apples", 3.50), ("Bread", 4.25), ("Milk", 2.75))

print(receipt.total())                     # 10.5
print(receipt.total("Apples", "Milk"))     # 6.25
print(receipt)
# Corner Market
# Apples: $3.50
# Bread: $4.25
# Milk: $2.75
# Total: $10.50
"""

class Receipt:
    """A class representing a receipt for a store, which can accumulate line items 
    and compute totals."""
