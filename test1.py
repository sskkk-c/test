import time

class TimeMethod():
    """实现日期和时间一些方法的类"""

    def time_stamp(self):
        """返回当前秒级时间戳"""
        t = time.time()
        return int(t)

    def micro_time_stamp(self):
        """返回当前毫秒级时间戳"""
        t = time.time()
        return int(1000*t)
        
    def timestamp_to_time(self, ts):
        """将给定时间戳转化为格式化后的日期时间字符串"""
        try:
            self.dt = time.strftime("%Y年%m月%d日 %H时%M分%S秒", time.localtime(ts))
            return self.dt
        except OSError:
            pass

    def time_to_timestamp(self, dt):
        """将给定的日期时间字符串解析成秒级时间戳"""
        try:
            self.ts = time.mktime(time.strptime(dt, "%Y-%m-%d %H:%M:%S"))
            return int(self.ts)
        except (ValueError,TypeError):
            pass

    def time_one_month_ago(self, dt):
        """将给定日期时间字符串解析成一个月以前的日期时间字符串"""
        try:
            self.new_timestamp = time.mktime(time.strptime(dt, "%Y-%m-%d %H:%M:%S")) - 30*24*60*60
            new_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self.new_timestamp))
            return new_time
        except (ValueError,TypeError):
            pass

#调试
t = TimeMethod()
a = t.timestamp_to_time(-5252)
print(a)
b = t.time_to_timestamp('2019-03-01 01:01:01')
print(b)
c = t.time_one_month_ago('1970-07-11 01:22:36')
print(c)