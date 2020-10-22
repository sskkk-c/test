import re
import random


class StringMethods():
    """提供验证字符串的一些方法"""

    default_code_list = ['2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'p', 'q', 'r', 's', 't',
                         'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    def __init__(self):
        """禁止类实例化。"""

        raise Exception('Can not instance')

    @staticmethod
    def username_verification(username_string):
        """ 提供字符串，验证是否符合网站名用户名要求（用户名要求是：长度是4-32，必须是字母开头，只能包含字母、数字、下划线）"""

        try:
            ret = re.match(r'^[a-zA-Z][\w\_]{3,31}$', username_string)
            if ret:
                return True
            else:
                return False
        except TypeError:
            return False

    @staticmethod
    def string_repalace(string):
        """提供字符串，返回替换后字符串，替换规则是将字符串中的所有大写字母和数字替换为空。"""

        try:
            ret = re.sub(r'[A-Z0-9]*', '', string)
            return ret
        except TypeError:
            return string

    @staticmethod
    def verificationcode_generate(length, code_list=default_code_list):
        """实现一个随机验证码。验证码包含大小写字母和数字，可以指定生成验证码的长度。"""

        code = ''.join(random.sample(code_list, length))  
        return code

