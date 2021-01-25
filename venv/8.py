from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"
browser.get(link)
number = browser.find_element_by_xpath("/html/body/div/form/div[1]/label/span[2]").text
edit = browser.find_element_by_xpath("/html/body/div/form/div[1]/input")
edit.send_keys(str(calc(int(number))))
time.sleep(1)
checkbox = browser.find_element_by_xpath("/html/body/div/form/div[2]/input")
checkbox.click()
radiobutton = browser.find_element_by_xpath("/html/body/div/form/div[4]/input")
browser.execute_script("return arguments[0].scrollIntoView(true);",radiobutton)
radiobutton.click()
button = browser.find_element_by_xpath("/html/body/div/form/button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
assert True