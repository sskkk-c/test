from datetime import datetime
import calendar

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
            dt = datetime.strptime(str_dt, TimeMethod.time_str)           #str转化为datetime
            ts = datetime.timestamp(dt)
            return int(ts)
        except (ValueError,TypeError):
            pass

    def time_one_month_ago(self, str_dt,months):
        """将给定日期时间字符串解析成一个月以前的日期时间字符串"""
        
        dt = datetime.strptime(str_dt, TimeMethod.time_str)               #str转化为datetime
        try:                                            
            month = dt.month + months -1
            year = dt.year + int(month / 12)
            month = month % 12 +1
            day = min(dt.day,calendar.monthrange(year, month)[1])
            return dt.replace(year=year, month=month, day=day)
        except (ValueError,TypeError):
            pass


t = TimeMethod()
a = t.time_one_month_ago('1990-10-10 10:10:10',1)
print(a)