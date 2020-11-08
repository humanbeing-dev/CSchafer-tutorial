"""
Best practices:
1. Tests should be isolated - should not rely on other tests
2. TDD - write the tests before you write the code
3. 'Any testing is better than no testing'
"""

import unittest
from unittest.mock import patch
from examples.employee import Employee


class TestEmployee(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('setupClass')

    @classmethod
    def tearDownClass(cls) -> None:
        print("teardownClass")

    def setUp(self) -> None:
        """Run its code BEFORE every single test"""
        self.emp_1 = Employee('Corey', 'Schafer', 50000)
        self.emp_2 = Employee('John', 'Bydlak', 60000)

    def tearDown(self) -> None:
        """Run its code AFTER every single test"""
        pass

    def test_email(self):
        self.assertEqual(self.emp_1.email, 'Corey.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'John.Bydlak@email.com')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'John.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Bydlak@email.com')

    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, 'Corey Schafer')
        self.assertEqual(self.emp_2.fullname, 'John Bydlak')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John Schafer')
        self.assertEqual(self.emp_2.fullname, 'Jane Bydlak')

    def test_apply_raise(self):
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def test_monthly_schedule(self):
        with patch('examples.employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Schafer/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Bydlak/June')
            self.assertEqual(schedule, 'Bad Response!')


if __name__ == '__main__':
    unittest.main()
