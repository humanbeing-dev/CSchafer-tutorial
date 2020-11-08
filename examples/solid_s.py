"""This is example of SOLID - single responsibility principle based on
youtube channel 'edutechional'

SRP: Each class and module in a program should focus on a single task
"""


class Invoice:
    def __init__(self, customer, total):
        self.customer = customer
        self.total = total

    def details(self):
        return f"Customer: {self.customer}, Total: {self.total}"


class SalesTax:
    def __init__(self, state):
        self.state = state

    @property
    def tax_rate(self):
        if self.state == 'AZ': return 5.5
        elif self.state == 'TX': return 3.2
        elif self.state == 'CA': return 8.7


class Mailer:
    @classmethod
    def email(cls, content):
        print("Emailing...")
        print(content)


if __name__ == '__main__':
    invoice = Invoice('Google', 100)
    tax = SalesTax('CA')
    print(tax.tax_rate)
    Mailer.email(invoice.details())
