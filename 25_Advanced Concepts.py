import unittest
import random
import string


# 1
class TestNumberOperations(unittest.TestCase):

    def test_number_in_list(self):
        my_list = [5, 7, 8, 10]
        self.assertIn(10, my_list, "Test 01 Failed: 10 is not found in the list")

    def test_type_of_number(self):
        number = 10
        self.assertIsInstance(number, int, "Test 02 Failed: The type of 10 is not int")

    def test_return_true(self):
        number = 100
        self.assertTrue(number, "Test 03 Failed: Number 100 did not return True")

    def test_empty_list(self):
        empty_list = []
        self.assertFalse(empty_list, "Test 04 Failed: Empty list did not return False")

    def test_number_comparison(self):
        number = 100
        self.assertGreaterEqual(number, 90, "Test 05 Failed: 100 is not larger than or equal to 90")


if __name__ == '__main__':
    unittest.main()


# 2
def generate_serial_number():
    serial_number = random.choices(string.ascii_letters + string.digits, k=14)

    serial_number = f"{''.join(serial_number[0:5])}-{''.join(serial_number[5:9])}-{''.join(serial_number[9:15])}"

    return serial_number


print(generate_serial_number())
