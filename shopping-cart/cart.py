#23. Implement a class ShoppingCart with methods to add items, remove items, calculate total, and apply discounts.

class ShoppingCart:
    def __init__(self):
        self.items = []
    
    # add items
    def add_items(self, *items):
        for item, price, qty in items:
            self.items.append({"item": item, "price": price, "quantity": qty})
    
    # remove items
    def remove_items(self, remove):
        self.remove = remove
        for i in self.items:
            if self.remove in i["item"]:
                self.items.remove(i)
                return "item removed from the list"
        else:
            return "item your are trying to remove does not exist in cart"
    
    # calculate total
    def calculate_total(self):
        price = 0
        for i in self.items:
            price +=  i["price"] * i["quantity"]
        return price
    
    # show total
    def show_total(self):
        return f"Total: {self.calculate_total()} USD"
    
    # add discount
    def discount(self):
        if self.calculate_total() >= 100: 
            return f"After 10% Discount: {self.calculate_total() - (self.calculate_total() * 0.1)}" # 10% if total = 100 or + 
        else:
            return f"After 5% Discount: {self.calculate_total() - (self.calculate_total() * 0.05)}" # 5% if less than 100

s1 = ShoppingCart()


s1.add_items(("chocolate", 10,2), ("pepsi",25,2), ("chicken",50,1)) # add 
print(s1.items)

print(s1.remove_items("chocolate")) # remove
print(f"Cart: {s1.items}")

print(s1.show_total())

print(s1.discount())
