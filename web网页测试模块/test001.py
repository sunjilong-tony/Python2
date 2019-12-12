#! /usr/bin/python3
# coding= utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import requests
import re
from PIL import Image, ImageDraw, ImageFilter, ImageFont

url = "http://www.baidu.com"
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get(url)
driver.maximize_window()
time.sleep(3)
driver.save_screenshot("./first.png")

set_btn=driver.find_element_by_partial_link_text("设置")
ActionChains(driver).move_to_element(set_btn).perform()
search_set=driver.find_element_by_partial_link_text("搜索设置")
ActionChains(driver).move_to_element(search_set).click().perform()
time.sleep(3)
driver.get_screenshot_as_file("e:/python2/web网页测试模块/1456.png")
NO=driver.find_element_by_xpath("//select[@id='nr']")
print(NO.location)
# el = driver.find_element_by_xpath("//select[@id='nr']")
# Select(sel).select_by_value('50')  # 显示50条
Select(NO).select_by_value("50")
driver.find_element_by_class_name("prefpanelgo").click()
time.sleep(4)
# driver.get_screenshot_as_file("e:/python2/web网页测试模块/123.png")
print(driver.switch_to.alert.text)
driver.switch_to.alert.accept()

size = driver.find_element_by_id("kw").size
print(size)
text = driver.find_element_by_id("su").text
above = driver.find_element_by_partial_link_text("新闻")
ActionChains(driver).move_to_element(above).click().perform()
if requests.status_codes == 200:
    print("打开ok")
elif requests.status_codes != 200:
    print("over")
    driver.refresh()
time.sleep(5)
# js="window.alert('hello ');"
# driver.execute_script(js)
time.sleep(3)
imput163 = driver.find_element_by_id("ww").send_keys("163.com")
clock163 = driver.find_element_by_class_name("btn")
ActionChains(driver).move_to_element(clock163).click().perform()
time.sleep(3)
WEB = driver.find_element_by_partial_link_text("网页")
ActionChains(driver).move_to_element(WEB).click().perform()
time.sleep(5)
driver.find_element_by_partial_link_text("官方").click()
all_handle = driver.window_handles
driver.switch_to.window(all_handle[1])
time.sleep(2)
driver.find_element_by_id("lbNormal").click()
time.sleep(2)
login_frame = driver.find_element_by_xpath("//iframe[starts-with(@id, 'x-URS-iframe')]")
driver.switch_to.frame(login_frame)
driver.find_element_by_name("email").clear()
driver.find_element_by_name("email").send_keys("aasun.110")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("qwe123!@#")
driver.find_element_by_id("dologin").click()
driver.switch_to.default_content()
time.sleep(3)
driver.quit()

