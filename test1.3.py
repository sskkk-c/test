from datetime import datetime
from dateutil.relativedelta import relativedelta


class TimeMethod():
    """实现日期和时间一些方法的类"""

    time_str = "%Y-%m-%d %H:%M:%S"

    def time_stamp(self):
        """返回当前秒级时间戳"""
        t = datetime.now()
        tt = t.timestamp()
        return int(tt)

    def micro_time_stamp(self):
        """返回当前毫秒级时间戳"""
        t = datetime.now()
        tt = t.timestamp()
        return int(1000*tt)

    def timestamp_to_time(self, ts):
        """将给定时间戳转化为格式化后的日期时间字符串"""
        t = int(ts)
        t = t if t > 0 else 0
        try:
            dt = datetime.fromtimestamp(t)
            return dt.strftime("%Y年%m月%d日 %H时%M分%S秒")
        except OSError:
            pass

    def time_to_timestamp(self, str_dt):
        """将给定的日期时间字符串解析成秒级时间戳"""
        try:
            dt = datetime.strptime(str_dt, TimeMethod.time_str)
            ts = datetime.timestamp(dt)
            return int(ts)
        except (ValueError, TypeError):
            pass

    def time_one_month_ago(self, str_dt, month):
        """将给定日期时间字符串解析成一个月以前的日期时间字符串"""

        dt = datetime.strptime(str_dt, TimeMethod.time_str)
        try:
            new_dt = dt + relativedelta(months=month)
        except (ValueError, TypeError):
            pass
        return new_dt

    def time_addday(self, str_dt, day):
        """将日期加减，返回格式化后的日期"""

        try:
            dt = datetime.strptime(str_dt, TimeMethod.time_str)
            new_dt = dt + relativedelta(days=day)
            return new_dt.strftime("%Y:%m:%d")
        except (ValueError, TypeError):
            pass
