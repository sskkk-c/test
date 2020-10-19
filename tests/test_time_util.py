import unittest
from test.time_util import TimeUtil

class TestTimeUtil(unittest.TestCase):
    def test_timestamp(self):
        print(TimeUtil.timestamp())

    def test_timestamp_to_string(self):
        time = 16031036190000
        print(TimeUtil.timestamp_to_string(time))
        # self.assertEqual(TimeUtil.timestamp_to_string(time), '2020年10月19日 18时33分39秒')

if __name__ == '__main__':
    unittest.main()

