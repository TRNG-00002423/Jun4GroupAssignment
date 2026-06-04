"""
Product Inventory System — Main Program
Demonstrates the full system with exception handling.
"""

from product import Product
from inventory import Inventory
from exceptions import ProductNotFoundError, InsufficientStockError


def main():
    inv = Inventory()

    # 1. Add at least 8 products across 3+ categories
    # TODO
    
    # 2. Display all products (sorted by price)
    # TODO: Use sorted() with the __lt__ dunder

    # 3. Search for products containing "pro"
    # TODO: Use inv.search()

    # 4. Show products in a specific category
    # TODO

    # 5. Sell products — include at least one that fails
    try:
        inv.sell(1, 3)   # Should succeed
        inv.sell(1, 999) # Should raise InsufficientStockError
    except InsufficientStockError as e:
        print(f"❌ {e}")
        print(f"   Requested: {e.requested}, Available: {e.available}")

    # 6. Try to access a product that doesn't exist
    try:
        inv.get_product(999)
    except ProductNotFoundError as e:
        print(f"❌ {e}")

    # 7. Show transaction history
    # TODO: Print recent entries from inv.history

    # 8. Show inventory summary (using comprehension-powered summary())
    # TODO

    # 9. Use set operations on categories
    # TODO: Show union, intersection with another set

    # 10. Use a tuple to store immutable product configurations
    # TODO: Create product configs as tuples, iterate over them


if __name__ == "__main__":
    main()