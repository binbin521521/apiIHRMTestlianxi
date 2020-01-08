import unittest,logging

from api.login_api import LoginApi
from parameterized.parameterized import parameterized
from utils import read_login_data, assert_common


class TestIhrmLoginPara(unittest.TestCase):
    """登录测试类"""
    @classmethod
    def setUpClass(cls) -> None:
        #初始化登录类
        cls.login_api = LoginApi()
    @classmethod
    def tearDownClass(cls) -> None:
        pass
    @parameterized.expand(read_login_data)
    def test_login(self, mobile, password, http_code, success, code, message):
        # 调用封装的登陆接口
        response = self.login_api.login(mobile, password)
        # 接收返回的json数据
        jsonData = response.json()
        # 调试输出登陆接口返回的数据，日志输出只能用作为{}占位符
        logging.info("登陆接口返回的数据为： {}".format(jsonData))

        assert_common(self, response, http_code, success, code, message)