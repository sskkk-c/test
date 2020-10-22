import json
import os.path
import sys

from bs4 import BeautifulSoup


class FileTools():
    """一个实现文件及目录方法的工具类。"""

    def __init__(self, string):
        """禁止类实例化。"""

        raise Exception('Can not instance')

    @staticmethod
    def path_exist(path_string):
        """提供一个路径字符串，判断该路径是否存在，并返回该路径是目录还是文件。"""

        if os.path.exists(path_string):
            if os.path.isfile(path_string):
                return "该路径是文件"
            elif os.path.isdir(path_string):
                return "该路径是目录"
        else:
            return False

    @staticmethod
    def write_in_file(path_string, data_string):
        """提供一个路径字符串，将指定字符串数据写入到该路径的文件"""

        with open(path_string, 'a') as f:
            f.write(data_string)
            return True

    @staticmethod
    def read_file():
        """读取file.html文件内容，提取该文件中<li>元素的class属性与值。并返回成json格式。"""

        path = os.path.join(sys.path[0], "file.html")
        soup = BeautifulSoup(
            open(path), features='html.parser')
        trs = soup.find_all('li')
        js_file = json.dumps(str(trs))
        
        return js_file
