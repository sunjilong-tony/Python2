#! /usr/bin/python3
# coding= utf-8

import unittest
from web.web_login import Web_Login
from parameterized import parameterized
from tools.read_json import Read_Json

def get_data():
    datas = Read_Json("login.json").read_json()
    arr = []
    for data in datas.values():
        print(data)
        arr.append((data.get("url"),
                    data.get("mobile"),
                    data.get("password"),
                    data.get("code"),
                    data.get("msg")))
        # print(arr)
        return arr


class Test_login(unittest.TestCase):
    @ parameterized.expand(get_data())
    def test_login(self, url, mobile, password, code, msg):
        re = Web_Login().web_login_post(url, mobile, password)
        # print(re.json())
        self.assertEqual(msg, re.json()["message"])
        self.assertEqual(code, re.json()["code"])

if __name__ == '__main__':
    unittest.main()