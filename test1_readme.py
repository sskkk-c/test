from datetime import datetime
from dateutil.relativedelta import relativedelta

# 这个类这是一个工具类，工具类一般不需要创建对象和实例化，所以应当都是静态方法(没有self参数，self属于实例)
# 静态方法跟函数差不多，只不过组织到了一起。
# 命名我们可以是xxUtil、xxHelper、xxTool
# VSCode全选右键格式化文档，可以格式化代码（需要安装插件，可能是autopep8、yapf、black）


class TimeUtil():
    """实现日期和时间一些方法的类"""

    # 良好的命名习惯
    default_format = "%Y-%m-%d %H:%M:%S"

    # 禁止类实例化
    def __init__(self):
        raise Exception('Can not instance')

    # timestamp 是一个单词，不用下划线
    # 我们可以在写代码时加入适当的换行，比如一段逻辑结束，return 之前等，更易读一些，用于记住代码不仅仅是机器看，更要是给人看的
    # 局部变量命名也要稍微注意下，有时候需要在长短和清楚表达意思之间权衡
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

    # 参数不要缩写，使用者不知道啥意思，根据需求应该返回的是字符串，也要注意下方法命名习惯
    # 注释的 # 后面要有个空格，一般都是单独一行。对一大堆变量进行注释的时候考虑写在行后，如下：
    # a = {
    #   'key1' : 'value1'   # 注释1
    #   'key2' : 'value2'   # 注释2
    #
    # }
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

    # 这里我们加了一个默认值参数，可以自定义 format 传入
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

print(TimeUtil.timestamp())
print(TimeUtil.timestamp_to_string(123456789))
t = TimeUtil()