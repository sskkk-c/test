import re, random

class SringMethods():
    """提供验证字符串的一些方法"""

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
            pass

    @staticmethod
    def string_repalace(string):
        """提供字符串，返回替换后字符串，替换规则是将字符串中的所有大写字母和数字替换为空。"""

        try:
            ret = re.sub(r'[A-Z0-9]*', '', string)
            return ret
        except TypeError:
            pass

    @staticmethod
    def verificationcode_generate(length):
        """实现一个随机验证码。验证码包含大小写字母和数字，可以指定生成验证码的长度。"""
        
        try:
            lst = []
            for i in range(length):
                r = random.randint(0, 3) 
                if r == 0 :  
                    num = random.randint(0, 9)
                    lst.append(str(num))
                elif r == 1:  
                    temp = random.randint(65, 90)
                    lst.append(chr(temp))
                else:
                    temp = random.randint(97, 122)  
                    lst.append(chr(temp))
            r_code = ''.join(lst)

            return r_code  
        except TypeError:
            pass
