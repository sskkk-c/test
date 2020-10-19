import unittest
from test.time_util import TimeUtil


class TestTimeUtil(unittest.TestCase):
    def test_timestamp(self):
        print(TimeUtil.timestamp())

    def test_timestamp_to_string(self):
        time1 = 1603103619
        time2 = 1603103619000
        self.assertEqual('2020年10月19日 18时33分39秒', TimeUtil.timestamp_to_string(time1))
        self.assertEqual('2020年10月19日 18时33分39秒', TimeUtil.timestamp_to_string(time2))

    def test_time_add_month(self):
        month1 = TimeUtil.time_add_month('2020-10-01 00:00:00', months=-1)
        self.assertEqual('2020-09-01 00:00:00', month1)

if __name__ == '__main__':
    unittest.main()
