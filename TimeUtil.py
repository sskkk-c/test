from datetime import datetime
from dateutil.relativedelta import relativedelta

class TimeUtil():
    """实现日期和时间一些方法的类"""

    default_format = "%Y-%m-%d %H:%M:%S"

    # 禁止类实例化
    def __init__(self):
        raise Exception('Can not instance')

    @staticmethod
    def timestamp():
        """返回当前秒级时间戳"""

        now = datetime.now()
        timestamp = now.timestamp()

        return int(timestamp)

    @staticmethod
    def micro_timestamp():
        """返回当前毫秒级时间戳"""

        now = datetime.now()
        micro_timestamp = now.timestamp()
        return int(1000 * micro_timestamp)

    @staticmethod
    def timestamp_to_string(timestamp):
        """将给定时间戳转化为格式化后的日期时间字符串"""

        timestamp = int(timestamp)
        t = timestamp if timestamp > 0 else 0
        try:
            dt = datetime.fromtimestamp(t)
            return dt.strftime("%Y年%m月%d日 %H时%M分%S秒")
        except OSError:
            pass

    @staticmethod
    def string_to_timestamp(time_string, format=default_format):
        """将给定的日期时间字符串解析成秒级时间戳"""
        try:
            dt = datetime.strptime(time_string, format)
            timestamp = datetime.timestamp(dt)

            return int(timestamp)
        except (ValueError, TypeError):
            pass

    @staticmethod
    def time_add_month(time_string, months):
        """将给定日期时间字符串解析成一个月以前的日期时间字符串"""

        dt = datetime.strptime(time_string, TimeUtil.default_format)
        try:
            new_dt = dt + relativedelta(months=months)

            return new_dt
        except (ValueError, TypeError):
            pass

    @staticmethod
    def time_add_day(time_string, days):
        """将日期加减，返回格式化后的日期"""

        try:
            dt = datetime.strptime(time_string, TimeUtil.default_format)
            new_dt = dt + relativedelta(days=days)

            return new_dt.strftime("%Y-%m-%d")
        except (ValueError, TypeError):
            pass
