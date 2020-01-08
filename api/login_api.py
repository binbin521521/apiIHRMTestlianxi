"""
封装登录接口
"""
import requests
import app


class LoginApi:
    """登录类"""

    def __init__(self):
        self.login_url = app.HOST + "/api/sys/login"
        self.headers = app.handlers

    def login(self, mobile, password):
        """登录方法"""
        # 使用data来接收外部传入的mobile和password,拼接成
        # 要发送的数据
        data = {"mobile": mobile, "password": password}
        # 发送登录请求
        response = requests.post(self.login_url,
                                 json=data,
                                 headers=self.headers)
        #返回响应数据
        return response
