#! /usr/bin/python3
# coding= utf-8

import json


class Read_Json(object):
    def __init__(self, filename):
        self.filepath = "e:/python2/测试/data/" + filename


    def read_json(self):
        with open(self.filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            # print(data)
            return data

# if __name__ == '__main__':
#     datas = Read_Json("login.json").read_json()
#     arr = []
#     for data in datas.values():
#         arr.append((data.get("url"),
#                     data.get("mobile"),
#                     data.get("password"),
#                     data.get("code"),
#                     data.get("msg")))
#         print(arr)


