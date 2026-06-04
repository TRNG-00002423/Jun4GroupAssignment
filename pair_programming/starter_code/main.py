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
    inv.add_product(Product("Computer", 120, category="electronics", stock=2))
    inv.add_product(Product("Fish Food", 10, category="pets", stock=99))
    inv.add_product(Product("Trash Bag", 1, category="household", stock=120))
    inv.add_product(Product("Monster Energy Drinks", 5, category="food/drinks", stock=55))
    inv.add_product(Product("Chicken Nuggets", 10, category="food/drink", stock=22))
    inv.add_product(Product("Protein Shakes", 6, category="food/drink", stock=12))
    inv.add_product(Product("Cat Food", 5, category="pets", stock=3))
    inv.add_product(Product("Pro Camera", 80, category="electronics", stock=1))
    
    # 2. Display all products (sorted by price)
    # TODO: Use sorted() with the __lt__ dunder
    products = list(inv.products.values())

    for product in sorted(products):
        print(product)
        print("\n")

    # 3. Search for products containing "pro"
    # TODO: Use inv.search()
    matching_search_products = inv.search("pro")

    for product in matching_search_products:
        print(product)
        print("\n")

    # 4. Show products in a specific category
    # TODO
    for product in inv.by_category('electronics'):
        print(product)


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
    for transactions in inv.history:
        print(transactions)

    # 8. Show inventory summary (using comprehension-powered summary())
    # TODO
    summary = inv.summary()
    for key, value in summary.items():
        print(f'{key}: {value}')

    # 9. Use set operations on categories
    # TODO: Show union, intersection with another set

    # 10. Use a tuple to store immutable product configurations
    # TODO: Create product configs as tuples, iterate over them


if __name__ == "__main__":
    main()