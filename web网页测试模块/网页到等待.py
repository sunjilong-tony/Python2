#! /usr/bin/python3
# coding= utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

url = "http://www.baidu.com"

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get(url)
driver.maximize_window()
print(driver.title)
time.sleep(3)
assert driver.title=="百度一下，你就知道", print("title err")
news = driver.find_element_by_partial_link_text("新闻")
# ActionChains(driver).move_to_element(news).context_click().perform()
ActionChains(driver).move_to_element(news).click().perform()
time.sleep(3)
finding = driver.find_element_by_id("ww").send_keys("selenium")
driver.find_element_by_id("ww").send_keys(Keys.ENTER)
titles=driver.find_elements_by_xpath("//div/h3/a")
print(titles)
for i in titles:
    print(i.text)
next_page = driver.find_element_by_partial_link_text("2")
ActionChains(driver).move_to_element(next_page).click().perform()
time.sleep(3)
driver.close()

