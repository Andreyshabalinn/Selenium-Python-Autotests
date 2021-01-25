from selenium import webdriver
import time

link1 = "https://suninjuly.github.io/registration1.html"
link2 = "https://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
try:
    browser.get(link2)
    # Код, который заполняет обязательные поля
    value1 = 'body > div.container > form > div.first_block > div.form-group.first_class > input'
    value2 = 'body > div.container > form > div.first_block > div.form-group.second_class > input'
    value3 = 'body > div.container > form > div.first_block > div.form-group.third_class > input'
    input1 = browser.find_element_by_css_selector(value1)
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector(value2)
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector(value3)
    input3.send_keys("Smolensk@gmail.com")
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)
    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
