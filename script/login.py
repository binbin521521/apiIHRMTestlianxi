"""
登录
"""
import unittest, logging

import app
from api.login_api import LoginApi


class Login(unittest.TestCase):
    """测试登录类"""

    @classmethod
    def setUpClass(cls) -> None:
        # 初始化登录类
        cls.login_api = LoginApi()

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test_login(self):
        # 调用封装的登录接口
        response = self.login_api.login('13800000002', '123456')
        # 接收返回的json数据
        jsonData = response.json()
        # 调试输出登录接口返回的数据，日志输出只能{}做占位符
        logging.info("登录成功接口返回的数据为：{}".format(jsonData))
        # 获取令牌，并拼接成以Bearer 开头的令牌字符串
        token = jsonData.get("data")
        # 保存令牌到全局变量
        app.HEADERS["Authorization"] = 'Bearer' + token
        # 打印令牌
        logging.info("保存的令牌是：{}".format(app.HEADERS))
