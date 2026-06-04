class Product:
    """A product in the inventory.

    Must implement these dunder methods:
        __str__     — "Laptop ($999.99) — 15 in stock"
        __repr__    — "Product('Laptop', 999.99, stock=15, category='electronics')"
        __eq__      — Equal if same name AND category
        __lt__      — Compare by price (enables sorting)
        __hash__    — Based on name + category (enables use in sets)
        __bool__    — True if in stock (stock > 0)
        __contains__ — Check if substring in product name

    Class attributes:
        total_products (int): Count of all Product instances
    """
    def __init__(self, product_name, price, category = "", stock = 0):
        self.product_name = product_name
        self.category = category
        self.price = price
        self.stock = stock
    
    def __str__(self):
        return f"{self.product_name} (${self.price}) - {self.stock} in stock"
    
    def __repr__(self):
        return f"Product('{self.product_name}', {self.price}, stock={self.stock}, category='{self.category}')"
    
    def __eq__(self, product):
        return self.product_name == product.product_name and self.category == product.category
    
    def __lt__(self, product):
        return self.price  < product.price
    
    def __hash__(self):
        return hash((self.product_name,self.category))
    
    def __bool__(self):
        return self.stock > 0

    def __contains__(self, substr):
        return substr.lower() in self.product_name.lower()
    
p1 = Product("Laptop", 999.99, stock=15, category="electronics")
p2 = Product("Laptop", 1099.99, stock=5, category="electronics")
p3 = Product("Mouse", 29.99, stock=50, category="electronics")

print(p1)                    # Laptop ($999.99) — 15 in stock
print(repr(p1))              # Product('Laptop', 999.99, stock=15, category='electronics')
print(p1 == p2)              # True (same name + category)
print(p1 < p3)               # False (999.99 > 29.99)
print(sorted([p1, p3]))      # Sorted by price
print(bool(p1))              # True (in stock)
print("laptop" in p1)        # True (case-insensitive search)
print({p1, p2})              # Set with ONE item (they're equal)
