class StringTools:
    """字符串操作的一些方法。"""

    def __init__(self):
        """禁止类实例化。"""

        raise Exception('Can not instance')

    @staticmethod
    def str2int(string):
        """将字符串转换为整型。"""

        return int(float(string))

    @staticmethod
    def int2str(integer):
        """将整型转换为字符串。"""

        return str(integer)

    @staticmethod
    def length(string):
        """提供字符串，返回字符串的长度。"""

        if isinstance(string, str):
            return len(string)
        else:
            return 0

    @staticmethod
    def coding_length(string, encoding):
        """提供字符串，以及编码，返回字符串的编码字节长度。"""

        if isinstance(string, str):
            return len(string.encode(encoding))
        else:
            return 0

    @staticmethod
    def start_with(a_string, b_string):
        """提供字符串A，返回检查是否以字符串B开头。"""

        if isinstance(a_string, str) and isinstance(b_string, str):
            return a_string.startswith(b_string)
        else:
            return 0

    @staticmethod
    def strip(string):
        """去除字符串两端的空格。"""

        if isinstance(string, str):
            return string.strip()
        else:
            return string

    @staticmethod
    def rjust(string, width):
        """对字符串左侧用0进行填充。"""

        if width >= len(string):
            return string.rjust(width, '0')
        else:
            raise Exception('Too short to filling')