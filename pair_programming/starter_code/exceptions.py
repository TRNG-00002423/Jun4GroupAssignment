class InventoryError(Exception):
    """Base exception for inventory system."""
    pass

class ProductNotFoundError(InventoryError):
    """Raised when a product lookup fails."""
    def __init__(self, product_id):
        self.product_id = product_id
        super().__init__(f"Product not found: {product_id}")

class InsufficientStockError(InventoryError):
    """Raised when stock is too low for an operation."""
    def __init__(self, product_name, requested, available):
        self.product_name = product_name
        self.requested = requested
        self.available = available
        super().__init__(
            f"Cannot fulfill {requested} units of '{product_name}'. "
            f"Only {available} in stock."
        )