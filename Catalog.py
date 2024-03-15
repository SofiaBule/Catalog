class Product:
    def __init__(self, id, name, price, description):
        self.id = id
        self.name = name
        self.price = price
        self.description = description

class WebStore:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_catalog(self):
        print("Product Catalog:")
        for product in self.products:
            print(f"{product.id}: {product.name} - ${product.price}")

# Example usage:
webstore = WebStore()
webstore.add_product(Product(1, "T-shirt", 20, "Comfortable cotton T-shirt"))
webstore.add_product(Product(2, "Jeans", 40, "Classic denim jeans"))
webstore.display_catalog()
