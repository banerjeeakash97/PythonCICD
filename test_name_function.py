import unittest
from name_function import formatted_name


class MyTestCase(unittest.TestCase):

    def test_first_last_name(self):
        result = formatted_name("Tarun", "Sisodia")
        self.assertEqual(result, "Tarun Sisodia")

    def test_first_last_middle_name(self):
        result = formatted_name("Tarun", "Sisodia", "Singh")
        self.assertEqual(result, "Tarun Singh Sisodia")


if __name__ == '__main__':
    unittest.main()
