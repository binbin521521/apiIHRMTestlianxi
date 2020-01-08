import app
import json
import pymysql


# 断言函数参数化
def assert_common(self, response,
                  http_code, success, code, message):
    # 断言响应状态码
    self.assertEqual(http_code, response.status_code)
    # 断言success
    self.assertEqual(success, response.json().get("success"))
    # 断言code
    self.assertEqual(code, response.json().get("code"))
    # 断言message
    self.assertEqual(message, response.json().get("message"))


def read_login_data():
    """增加员工数量参数化"""
    path = app.BASE_DIR + "/data/employee.json"
    with open(path, mode="r", encoding="utf-8") as f:
        jsonData = json.load(f)
        # 由于employee.json是一个字典数据，那么我们可以使用字典的get方法获取其中数据
        # 根据键取值
        add_emp_data = jsonData.get("add_emp")
        # 新建一个空列表
        result_list = []
        username = add_emp_data.get("username")
        mobile = add_emp_data.get("mobile")
        success = add_emp_data.get("success")
        code = add_emp_data.get("code")
        message = add_emp_data.get("message")
        http_code = add_emp_data.get("http_code")
        #将上面获取的数据加入列表中
        result_list.append((username, mobile, success, code, message, http_code))
        #打印列表
    print('列表中添加员工的数据：',result_list)
    return result_list

def read_query_emp_data():
    path = app.BASE_DIR + "/data/employee.json"
    # 打开文件
    with open(path, mode='r', encoding='utf-8') as f:
        # 加载Json数据文件
        jsonData = json.load(f)
        # 由于employee.json是一个字典数据，那么我们可以使用字典的get方法获取
        result_list = []
        query_emp_data = jsonData.get("query_emp")
        success = query_emp_data.get("success")
        code = query_emp_data.get("code")
        message = query_emp_data.get("message")
        http_code = query_emp_data.get("http_code")
        result_list.append((success, code, message, http_code))
    print("查询员工数据为：", result_list)
    return result_list


def read_modify_emp_data():
    path = app.BASE_DIR + "/data/employee.json"
    # 打开文件
    with open(path, mode='r', encoding='utf-8') as f:
        # 加载Json数据文件
        jsonData = json.load(f)
        # 由于employee.json是一个字典数据，那么我们可以使用字典的get方法获取
        result_list = []
        modify_emp_data = jsonData.get("modify_emp")
        username = modify_emp_data.get("username")
        success = modify_emp_data.get("success")
        code = modify_emp_data.get("code")
        message = modify_emp_data.get("message")
        http_code = modify_emp_data.get("http_code")
        result_list.append((username, success, code, message, http_code))
    print("修改员工数据为：", result_list)
    return result_list


def read_delete_emp_data():
    path = app.BASE_DIR + "/data/employee.json"
    # 打开文件
    with open(path, mode='r', encoding='utf-8') as f:
        # 加载Json数据文件
        jsonData = json.load(f)
        # 由于employee.json是一个字典数据，那么我们可以使用字典的get方法获取
        result_list = []
        delete_emp_data = jsonData.get("delete_emp")
        success = delete_emp_data.get("success")
        code = delete_emp_data.get("code")
        message = delete_emp_data.get("message")
        http_code = delete_emp_data.get("http_code")
        result_list.append((success, code, message, http_code))
    print("删除员工数据为：", result_list)
    return result_list

class DBUtils:

    def __init__(self, host="182.92.81.159",
                 user='readuser',
                 password='iHRM_user_2019',
                 database='ihrm'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    #  __enter__和__exit__是一对魔法方法，主要要和with结合使用
    # 如：with DBUtils() as db:
    # 我们就可以在with的代码快中使用db来执行sql语句。这个db就相当于cursor
    def __enter__(self):
        self.conn = pymysql.connect(self.host, self.user, self.password, self.database)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()


if __name__ == '__main__':
    # main函数的作用？
    # 防止调用这个模块或者类时，自动执行代码
    read_delete_emp_data()
    print("11111")
















