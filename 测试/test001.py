#! /usr/bin/python3
# coding= utf-8
from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.maximize_window()
driver.get("http://news.baidu.com/")
driver.back()
time.sleep(5)
driver.forward()

driver.refresh()
driver.close()