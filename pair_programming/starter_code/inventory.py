from collections import deque
from exceptions import ProductNotFoundError, InsufficientStockError
from functools import reduce

class Inventory:
    """A collection of products with search, filter, and transaction capabilities.

    Features:
        - Add/remove products
        - Search by name or category
        - Transaction history (deque with maxlen=50)
        - Restock and sell operations with exception handling
    """
    next_id = 0

    def __init__(self):
        self.products = {}          # {product_id: Product}
        self.categories = set()     # Unique categories
        self.history = deque(maxlen=50)  # Recent transactions
        self._next_id = 1

    def add_product(self, product):
        """Add a product to inventory. Return the assigned ID."""
        self.products[self.next_id] = product
        self.next_id += 1

        return self.next_id
        
    def remove_product(self, product_id):
        """Remove a product. Raise ProductNotFoundError if missing."""
        try:
            del self.products[product_id]
        except:
            raise ProductNotFoundError

    def get_product(self, product_id):
        """Get a product by ID. Raise ProductNotFoundError if missing."""
        try:
            return self.products[product_id]
        except:
            raise ProductNotFoundError
        
    def sell(self, product_id, quantity):
        """Sell units of a product.
        Raise ProductNotFoundError if ID doesn't exist.
        Raise InsufficientStockError if not enough stock.
        Record transaction in history.
        """
        try:
            product = self.products[product_id]
            if product.stock < quantity:
                raise InsufficientStockError
            product.stock -= quantity
            self.history.append((product_id, quantity))
        except KeyError:
            raise ProductNotFoundError
    
    def restock(self, product_id, quantity):
        """Add stock. Raise ProductNotFoundError if missing."""
        try:
            product = self.products[product_id]
            product.stock += quantity
            self.history.append((product_id, quantity))
        except KeyError:
            raise ProductNotFoundError

    # --- Comprehension-powered queries ---

    def search(self, keyword):
        """Return products containing keyword (case-insensitive).
        Use a list comprehension and the __contains__ dunder.
        """
        return [product for product in self.products.values() if product.__contains__(keyword)]

    def by_category(self, category):
        """Return products in a category. Use a list comprehension."""
        return [product for product in self.products.values() if product.category == category]


    def in_stock(self):
        """Return products with stock > 0. Use __bool__ dunder + filter."""
        return filter(lambda product: product.stock > 0, [self.products.values()])

    def price_range(self, min_price, max_price):
        """Return products in the price range. Use a list comprehension."""
        return [product for product in self.products.values() if product.price <= max_price and product.price >= min_price]



    def summary(self):
        """Return a dict with:
        - total_products
        - total_value (sum of price * stock for each product)
        - categories (sorted list)
        - out_of_stock_count
        Use dict/list comprehensions.
        """
        return {
            "total_products": len(self.products),
            "total_value": reduce(lambda total, product: total + product.stock * product.price, self.products.values(), 0),
            "category": sorted(list(set(product.category for product in self.products.values()))),
            "out_of_stock_count": reduce(lambda count, product: count + 1 if product.stock > 0 else count, self.products.values(), 0)
        }