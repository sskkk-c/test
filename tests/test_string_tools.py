import unittest
from test.string_tools import StringTools


class TestStringTools(unittest.TestCase):
    def test_str2int(self):
        print(StringTools.int2str(0.000000000001))

    def test_length(self):
        print(StringTools.length(1))
        print(StringTools.length('Hello, 世界！'))

    def test_coding_length(self):
        print(StringTools.coding_length('Hello, 中国', (str)))

    def test_start_with(self):
        print(StringTools.start_with('ab', 'a'))
        print(StringTools.start_with('ab', ''))
        print(StringTools.start_with(1, ''))

    def test_strip(self):
        print(StringTools.strip(1))

    def test_rjust(self):
        print(StringTools.rjust(2, 'abc'))


if __name__ == '__main__':
    unittest.main()
