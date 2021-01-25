from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select



link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    y_element = browser.find_element_by_xpath("/html/body/div/form/h2/span[2]").text
    x_element = browser.find_element_by_xpath("/html/body/div/form/h2/span[4]").text
    number = int(y_element)+int(x_element)
    print(number)
    spisok = browser.find_element_by_xpath("/html/body/div/form/div/select")
    spisok.click()
    select = Select(spisok)
    select.select_by_visible_text(str(number))
    button = browser.find_element_by_xpath("/html/body/div/form/button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()