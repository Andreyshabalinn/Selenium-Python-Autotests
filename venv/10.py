from selenium import webdriver
import math
import time
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)
fn = browser.find_element_by_xpath("/html/body/div/form/div/input[1]")
fn.send_keys("Andrey")
sn = browser.find_element_by_xpath("/html/body/div/form/div/input[2]")
sn.send_keys("Andrey")
email = browser.find_element_by_xpath("/html/body/div/form/div/input[3]")
email.send_keys("Andrey")
filebut = browser.find_element_by_xpath("/html/body/div/form/input")
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
print(file_path)
filebut.send_keys(file_path)
button = browser.find_element_by_xpath("/html/body/div/form/button")
button.click()
assert True