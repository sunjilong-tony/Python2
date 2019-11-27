# coding= utf-8
import random
import os
import win32con
import win32gui
import win32com.client
def outer():
    num = 10
    def inner():
        nonlocal num   # nonlocal关键字声明
        num = 100
        print(num)
    inner()
    print(num)
outer()

# tony = win32com.client.Dispatch("SAPI.SPVOICE")
# tony.Speak("GOOD MAN")
# qqWin = win32gui.FindWindow("TXGuiFoundation", "QQ")
# win32gui.ShowWindow(qqWin, win32con.SW_HIDE)

# a = "23455"
# for i in random.randrange(a):
#     print(i)
# print(range(a))
# str = "tony is good man! tony is nice man! tony is good man! tony is nice man!"
# # print(str.count("tony"))
# # str1 = str.split(" ")
# # d = {}
# # print(str1)
# # str2 = dict.fromkeys(str1)
# # # print(str2)
# # for i in str1:
# #      cou = d.get(i)
# #      if cou  == None:
# #           d[i] = 1
# #      else:
# #           d[i] += 1
# # print(d)
#
#
# def say(age):
#     # err = Exception("DFHDFK")
#     # raise err
#     print("tony is age %d" %age)
# ll = say(11)
# try:
#     say(11)
# except Exception as error:
#     print("%s" % error)
# else:
#     print("1111")
# finally:
#     print("2343443")
# f1 = open("./aa", "r")
# f2 = open("./ab.text", "w")
# f1read = f1.readline()
# f1.flush()
#
# f2.write(f1read)
# f1.close()
# f2.close()
#
# # print(os.name)
# # print(os.environ)
# print(os.getcwd())
# print(os.listdir(os.getcwd()))
# print(os.stat(f1))
# os.system("services.msc")
