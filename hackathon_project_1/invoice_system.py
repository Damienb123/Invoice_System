import datetime
import random


# Item Model
# ===============================
class Item:
    def __init__(self, name, quantity, unit_price):
        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price

    @property
    def total(self):
        return self.quantity * self.unit_price



# Invoice Model
# ===============================
class Invoice:
    TAX_RATE = 0.10
    DISCOUNT_CODE = "SAVE10"
    DISCOUNT_RATE = 0.10

    def __init__(self):
        self.items = []
        self.invoice_number = self.generate_invoice_number()
        self.date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    def add_item(self, item):
        self.items.append(item)

    def generate_invoice_number(self):
        return random.randint(1000, 9999)

    def subtotal(self):
        return sum(item.total for item in self.items)

    def tax(self):
        return self.subtotal() * self.TAX_RATE

    def discount(self, code):
        if code == self.DISCOUNT_CODE:
            return self.subtotal() * self.DISCOUNT_RATE
        return 0

    def grand_total(self, discount_amount):
        return self.subtotal() + self.tax() - discount_amount



# Formatting for invoice
# ===============================
def format_invoice(invoice, discount_amount):
    lines = []
    lines.append("=" * 45)
    lines.append(f"INVOICE #{invoice.invoice_number}")
    lines.append(f"Date: {invoice.date}")
    lines.append("=" * 45)
    lines.append(f"{'Item':15} {'Qty':>5} {'Price':>8} {'Total':>10}")
    lines.append("-" * 45)

    for item in invoice.items:
        lines.append(f"{item.name:15} {item.quantity:>5} "
                     f"${item.unit_price:>7.2f} ${item.total:>9.2f}")

    lines.append("-" * 45)
    lines.append(f"{'Subtotal:':30} ${invoice.subtotal():>9.2f}")
    lines.append(f"{'Tax (10%):':30} ${invoice.tax():>9.2f}")
    lines.append(f"{'Discount:':30} -${discount_amount:>8.2f}")
    lines.append("=" * 45)
    lines.append(f"{'Grand Total:':30} ${invoice.grand_total(discount_amount):>9.2f}")
    lines.append("=" * 45)
    return "\n".join(lines)



# Main Program
# ===============================
def main():
    invoice = Invoice()
    print("Enter invoice items (type 'done' when finished):")

    while True:
        name = input("Item name: ")
        if name.lower() == "done":
            break

        try:
            quantity = int(input("Quantity: "))
            price = float(input("Price per item: "))
            invoice.add_item(Item(name, quantity, price))
        except ValueError:
            print("Invalid input. Please try again.")

    discount_code = input("Enter discount code (or press Enter to skip): ")
    discount_amount = invoice.discount(discount_code)

    invoice_text = format_invoice(invoice, discount_amount)
    print("\n" + invoice_text)
    # Included feature - saving to a file
    save = input("Save invoice to file? (y/n): ").lower()
    if save == "y":
        filename = f"invoice_{invoice.invoice_number}.txt"
        with open(filename, "w") as file:
            file.write(invoice_text)
        print(f"Invoice saved as {filename}")


if __name__ == "__main__":
    main()



