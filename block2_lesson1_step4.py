from selenium import webdriver
import time
import math

# open page
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/math.html")

    # находим значение переменной x и передаем его в функцию для расчета
    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text

    # функция для расчета переменной x
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    y = calc(x)
    input_answer = browser.find_element_by_css_selector("#answer")\
        .send_keys(y)
    robot_checkbox_click = browser.find_element_by_css_selector("#robotcheckbox")\
        .click()
    robot_radio_click = browser.find_element_by_css_selector("#robotsRule")\
        .click()
    submit_btn_click = browser.find_element_by_css_selector(".btn")\
        .click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()

