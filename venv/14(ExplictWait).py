from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = browser.find_element_by_xpath("/html/body/div/div/div/button")
text = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.XPATH, "/html/body/div/div/div/div[1]/h5[2]"),"$100")
    )
button.click()

browser.execute_script("window.scrollBy(0, 100);")

number = browser.find_element_by_xpath("/html/body/form/div/div/div/label/span[2]").text
edit = browser.find_element_by_xpath("/html/body/form/div/div/div/input")
edit.send_keys(str(calc(number)))

button = browser.find_element_by_xpath("/html/body/form/div/div/button")
button.click()