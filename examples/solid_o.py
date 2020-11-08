"""This is example of SOLID - open/closed principle based on
youtube channel 'edutechional'

OCP: Software elements(classes, modules, functions) should be open for extension,
but closed for modification
"""


class OrderReport:
    def __init__(self, customer, total):
        self.customer = customer
        self.total = total


class Invoice(OrderReport):
    def print_out(self):
        print("Invoice")
        print(self.customer)
        print(self.total)


class BillOfLading(OrderReport):
    def __init__(self, address, **kwargs):
        super().__init__(**kwargs)
        self.address = address

    def print_out(self):
        print("BOL")
        print(self.customer)
        print("Shiping Label...")
        print(self.address)


invoice = Invoice('Google', 100)
bill_of_lading = BillOfLading(customer="Yahoo", total=200, address="123 Any Street")
invoice.print_out()
bill_of_lading.print_out()