import time

#webdriver это и есть абор команд для управления браузером
from selenium import webdriver
#инициализируем хромдрайвер
driver = webdriver.Chrome()
#Ожидаем 5 сек
time.sleep(5)
#Заходим на сайт
driver.get("https://stepik.org/lesson/25969/step/12")
time.sleep(5)
#Находим текст
textarea = driver.find_element_by_css_selector(".textarea")
#Вводим в поле
textarea.send_keys("get()")
time.sleep(5)

#Находим кнопку сss селектора
submit_button = driver.find_element_by_css_selector(".submit-submission")

submit_button.click()
#выключаем браузер
driver.quit()
