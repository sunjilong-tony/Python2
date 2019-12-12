#! /usr/bin/python3
# coding= utf-8
from selenium import webdriver
import time
from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
driver.get("https://mail.163.com/")
sleep(1)
driver.find_element_by_id("lbNormal").click()
sleep(5)
#login_frame=driver.find_element_by_id("x-URS-iframe")
# //*[@id="lbNormal"]
login_frame=driver.find_element_by_xpath("//iframe[starts-with(@id, 'x-URS-iframe')]")
driver.switch_to.frame(login_frame)
driver.find_element_by_name("email").send_keys("####")
driver.find_element_by_name("password").send_keys("#######")
driver.find_element_by_id("dologin").click()
driver.switch_to.default_content()
driver.quit()

