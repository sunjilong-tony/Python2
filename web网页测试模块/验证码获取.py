#! /usr/bin/python3
# coding= utf-8
from selenium import webdriver
from PIL import ImageFont, Image,ImageDraw,ImageFilter
from pytesseract import pytesseract
import time
import re
import os
path=r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

url = "https://weixin.sogou.com/antispider/?from=http%3A%2F%2Fweixin.sogou.com%2Fweixin%3Ftype%3D2%26query%3Dpython"
driver = webdriver.Chrome()
driver.get(url)
driver.minimize_window()
time.sleep(3)
driver.save_screenshot("./baidu首页.png")
code_image = driver.find_element_by_id("seccodeImage")
location = code_image.location
print(location)
im = Image.open("./baidu首页.png")
x = location["x"]+100
y = location["y"]+40
im_crop = im.crop((int(location["x"]), int(location["y"]), int(x), int(y)))
im_crop.save("code.png", "png")
new_img = im_crop.convert("L")
# 识别太低
pixdata = new_img.load()
w, h = new_img.size
threshold = 160  # 该阈值不适合所有验证码，具体阈值请根据验证码情况设置
# 遍历所有像素，大于阈值的为黑色
# for y in range(h):
#     for x in range(w):
#             if pixdata[x, y] < threshold:
#                 pixdata[x, y] = 0
#             else:
#                 pixdata[x, y] = 255
# black_point = 0
# data = new_img.getdata()
# for x in range(1, w - 1):
#     for y in range(1, h - 1):
#         mid_pixel = data[w * y + x]  # 中央像素点像素值
#         if mid_pixel < 50:  # 找出上下左右四个方向像素点像素值
#                 top_pixel = data[w * (y - 1) + x]
#                 left_pixel = data[w * y + (x - 1)]
#                 down_pixel = data[w * (y + 1) + x]
#                 right_pixel = data[w * y + (x + 1)]
#                 # 判断上下左右的黑色像素点总个数
#                 if top_pixel < 10:
#                     black_point += 1
#                 if left_pixel < 10:
#                     black_point += 1
#                 if down_pixel < 10:
#                     black_point += 1
#                 if right_pixel < 10:
#                     black_point += 1
#                 if black_point < 1:
#                     new_img.putpixel((x, y), 255)
new_img.save("./new.png", "png")
pytesseract.tesseract_cmd = path  # 设置pyteseract路径
string = pytesseract.image_to_string(new_img, lang="eng")
string = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", string)
print(string)
driver.quit()

