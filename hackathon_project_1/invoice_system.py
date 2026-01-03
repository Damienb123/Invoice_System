import datetime
import random

# Item model
# -------------------------------------------------------------------
class Item:
    def __init__(self, name, quantity, unit_price):
        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price

@property
def total(self):
    return self.quantity * self.unit_price

# Invoice model
# -------------------------------------------------------------------
class Invoice:
    TAX_RATE = 0.10
    DISCOUNT_CODE = "SAVE10"
    DISCOUNT_RATE = 0.10

def __init__(self):
    self.items = []
    self.invoice_number = self.generate_invoice_number()
    self.data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

def add_item(self, item):
    self.items.append(item)

def generate_invoice_number(self):
    return random.randit(1000, 9999)

def subtotal(self):
    return sum(item.total for item in self.items)

def tax(self):
    return self.total() * self.TAX_RATE

def discount(self, code):
    if code == self.DISCOUNT_CODE:
        return self.subtotal() * self.DISCOUNT_RATE
    return 0

def grand_total(self, discount_amount):
    return self.subtotal() + self.tax() - discount_amount
