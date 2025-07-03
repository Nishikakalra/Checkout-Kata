class Product:
    def __init__(self, code, unit_price, special_qty=None, special_price=None):
        self.code = code
        self.unit_price = unit_price
        self.special_qty = special_qty
        self.special_price = special_price

    def calculate_price(self, quantity):
        if self.special_qty and self.special_price:
            groups = quantity // self.special_qty
            remainder = quantity % self.special_qty
            return groups * self.special_price + remainder * self.unit_price
        return quantity * self.unit_price


class CheckoutSystem:
    def __init__(self):
        self.products = {
            'A': Product('A', 50, 3, 130),
            'B': Product('B', 30, 2, 45),
            'C': Product('C', 20),
            'D': Product('D', 15)
        }

    def calculate_total(self, cart_items):
        cart_items = cart_items.upper() #("ABBA")
        if not cart_items:
            return 0,[]
        
        item_counts = {} #{A:2,B:2 }
        message=[]
        unavailable_items=set()
        for item in cart_items:
            if item in self.products:
                item_counts[item] = item_counts.get(item, 0) + 1
            else:
                if item not in unavailable_items:
                    message.append(f"The item {item} is not available")
                    print(f"The item {item} is not available")
                    unavailable_items.add(item)

        total = 0
        for code, qty in item_counts.items():  #{A:2,B:2}
            product = self.products[code] 
            total += product.calculate_price(qty)

        return total, message
