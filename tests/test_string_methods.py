import unittest
from test.string_methods import StringMethods


class TestStringMethods(unittest.TestCase):
    def test_username_verification(self):
        print(StringMethods.username_verification(111))

    def test_verificationcode_generate(self):
        print(StringMethods.verificationcode_generate(4))


if __name__ == '__main__':
    unittest.main()
