import os.path
import json
from bs4 import BeautifulSoup


class FileTools():
    """一个实现文件及目录方法的工具类。"""

    def __init__(self, string):
        """禁止类实例化。"""

        raise Exception('Can not instance')

    @staticmethod
    def path_exist(path_string):
        """提供一个路径字符串，判断该路径是否存在，并返回该路径是目录还是文件。"""

        """ TODO: 不存在应该抛出异常，异常应该不需捕获 """
        try:
            if os.path.exists(path_string):
                if os.path.isfile(path_string):
                    return "该路径是文件"
                elif os.path.isdir(path_string):
                    return "该路径是目录"
            else:
                return False
        except TypeError:
            pass

    @staticmethod
    def write_in_file(path_string, data_string):
        """提供一个路径字符串，将指定字符串数据写入到该路径的文件"""

        """ TODO: 异常应该比较多：文件不存在。如果是在Linux环境下可能目录不可写等等。应该抛出 """
        try:
            with open(path_string, 'a') as f:
                f.write(data_string)
                return True
        except TypeError:
            pass

    @staticmethod
    def read_file():
        """读取file.html文件内容，提取该文件中<li>元素的class属性与值。并返回成json格式。"""

        """ TODO: 不应该是个绝对路径，别人运行不了，应该把file.html放在项目目录，使用相对路径读取，同样应该会有异常抛出 """
        soup = BeautifulSoup(
            open(r'C:\Users\杨天琦\Desktop\file.html'), features='html.parser')
        trs = soup.find_all('li')
        js_file = json.dumps(str(trs))
        return js_file
