from selenium import webdriver
import math
import time
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)

button = browser.find_element_by_xpath("/html/body/form/div/div/button")
button.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

number = browser.find_element_by_xpath("/html/body/form/div/div/div/label/span[2]").text

text = browser.find_element_by_xpath("/html/body/form/div/div/div/input")
text.send_keys(str(calc(number)))
button = browser.find_element_by_xpath("/html/body/form/div/div/button")
button.click()
assert True