from catalog import catalog_data

class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"Item #{self.product_id}: {self.name}\n₦{self.price} (In Stock: {self.stock}).\n"
    
    @property
    def price(self):
        return self._price

    @property
    def stock(self):
        return self._stock

    @price.setter
    def price(self, price):
        if price <= 0:
            raise ValueError("Price must be greater than zero. Lock In!")
        self._price = price

    @stock.setter
    def stock(self, stock):
        if stock < 0:
            raise ValueError("Stock cannot be a negative number. Lock In!")
        self._stock = stock

    def purchase(self, quantity):
        if self.stock != 0 and self.stock >= quantity:
            self.stock -= quantity
            return True
        raise ValueError("Out of stock or insufficient quantity")


class DigitalProducts(Product):
    def __init__(self, product_id, name, price, stock, file_size_mb: float):
        super().__init__(product_id, name, price, stock)
        self.file_size_mb = file_size_mb

    def purchase(self, quantity):
        return f"{self.file_size_mb}MB downloaded successfully for {quantity} products!"


class PhysicalProduct(Product):
    def __init__(self, product_id, name, price, stock, shipping_weight_kg):
        super().__init__(product_id, name, price, stock)
        self.shipping_weight_kg = shipping_weight_kg

    def calculate_shipping(self):
        return self.shipping_weight_kg * 1500

def main():
    try:
        _ = Product(101, "Trousers", -2000, -1)
    except ValueError as e:
        print(f"Validation Caught: {e}\n")

    catalog = []

    for item in catalog_data:
        if item["type"] == "digital":
            digital_prod = DigitalProducts(
                item["product_id"],
                item["name"],
                item["price"],
                item["stock"],
                item["file_size_mb"],
            )
            catalog.append(digital_prod)
        elif item['type'] == 'physical':
            physical_prod = PhysicalProduct(
                item["product_id"],
                item["name"],
                item["price"],
                item["stock"],
                item["shipping_weight_kg"],
            )
            catalog.append(physical_prod)
            
    print('--- STORE CATALOG ---')
    for product in catalog:
        print(product)
        # Polymorphism in action: check if it's physical to calculate shipping
        if isinstance(product, PhysicalProduct):
            fee = product.calculate_shipping()
            print(f"   -> Shipping Fee: ₦{fee}")
        print()
            
if __name__ == "__main__":
    main()
