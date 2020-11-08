import unittest
from unittest.mock import patch
from examples.solid_s import Invoice, SalesTax


class TestInvoice(unittest.TestCase):
    def setUp(self) -> None:
        """Run its code BEFORE every single test"""
        self.comp_1 = Invoice("Google", 100)
        self.comp_2 = Invoice("ProMCS", 0)

    def test_details(self):
        self.assertEqual(self.comp_1.details, "Customer: Google, Total: 100")
        self.assertEqual(self.comp_2.details, "Customer: ProMCS, Total: 0")


class TestSalesTax(unittest.TestCase):
    def setUp(self) -> None:
        """Run its code BEFORE every single test"""
        self.tax_1 = SalesTax("AZ")
        self.tax_2 = SalesTax("TX")
        self.tax_3 = SalesTax("CA")

    def test_tax_rate(self):
        self.assertEqual(self.tax_1.tax_rate, 5.5)
        self.assertEqual(self.tax_2.tax_rate, 3.2)
        self.assertEqual(self.tax_3.tax_rate, 8.7)


if __name__ == '__main__':
    unittest.main()
