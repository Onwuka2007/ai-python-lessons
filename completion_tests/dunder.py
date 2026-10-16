class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} (₦{self.price})"


class ShoppingCart:
    def __init__(self):
        # Internal list to store our items (we'll store dictionaries with product and quantity)
        self.items = []

    def add_item(self, product, quantity):
        self.items.append({"product": product, "quantity": quantity})

    # 1. Dunder __len__: Teaches Python how to use len() on your cart
    def __len__(self):
        return len(self.items)

    # 2. Dunder __iter__: Teaches Python how to loop through your cart with a 'for' loop
    def __iter__(self):
        return iter(self.items)

    # 3. Dunder __add__: Teaches Python what the '+' operator means between two carts
    def __add__(self, other_cart):
        combined_cart = ShoppingCart()
        
        # Add items from the first cart
        for item in self.items:
            combined_cart.add_item(item["product"], item["quantity"])
            
        # Add items from the second cart
        for item in other_cart.items:
            combined_cart.add_item(item["product"], item["quantity"])
            
        return combined_cart

    # 4. Dunder __str__: Provides a clean text summary when printed
    def __str__(self):
        total_items = sum(item["quantity"] for item in self.items)
        total_price = sum(item["product"].price * item["quantity"] for item in self.items)
        return f"ShoppingCart -> {total_items} total item(s) | Estimated Total: ₦{total_price:,.2f}"


def main():
    # Create some products
    p1 = Product(101, "Mechanical Keyboard", 45000)
    p2 = Product(102, "Ergonomic Mouse", 15000)
    p3 = Product(103, "Desk Mat", 8000)

    # --- Cart 1 ---
    cart1 = ShoppingCart()
    cart1.add_item(p1, 1)
    cart1.add_item(p2, 2)

    # --- Cart 2 ---
    cart2 = ShoppingCart()
    cart2.add_item(p3, 1)

    print("=== TESTING INDIVIDUAL CARTS ===")
    print(cart1)
    print(cart2)
    print()

    # Testing Dunder __len__
    print(f"Number of distinct product lines in Cart 1: {len(cart1)}")
    print()

    # Testing Dunder __iter__ (Looping directly over our custom class object!)
    print("=== LOOPING THROUGH CART 1 ===")
    for entry in cart1:
        prod = entry["product"]
        qty = entry["quantity"]
        print(f"- {qty}x {prod.name} at ₦{prod.price} each")
    print()

    # Testing Dunder __add__ (Merging cart1 and cart2 using the '+' sign!)
    print("=== MERGING CARTS WITH '+' ===")
    mega_cart = cart1 + cart2
    print(mega_cart)
    
    print("\nItems inside the merged Mega Cart:")
    for entry in mega_cart:
        print(f"- {entry['quantity']}x {entry['product'].name}")


if __name__ == "__main__":
    main()