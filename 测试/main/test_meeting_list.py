#! /usr/bin/python3
# coding= utf-8

import unittest
from web.meeting_list import Meeting_List


class Test_meeting_list(unittest.TestCase):
    def test_list(self):
        url = "https://vzhapi.tamiyun.com/robotadmin/tm/admin/meeting/c2mGetAllMeeting"
        data = {
            "createEndTime": "",
            "createStartTime": "",
            "curPage": 1,
            "employeeId": 22,
            "endTime": "",
            "feeType": "null",
            "isVzh": -1,
            "pageSize": 10,
            "rocessId": "null",
            "startTime": ""}
        headers = {
            "Content-Type": "application/json",
            "token": "f7b8affca1e54dbd960e7ec9a3bd2ead",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like"
                          " Gecko) Chrome/76.0.3809.100 Safari/537.36"
                    }
        re = Meeting_List().meeting_list(url=url, data=data, headers=headers)
        # print(re.json())
        self.assertEqual(200, re.status_code)

if __name__ == '__main__':
    unittest.main()
