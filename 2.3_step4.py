from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


 
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

#открываем страницу
try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #нажать на кнопку 'I want ot go on a magical journey'
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()

    #переключаемся на окно алерт, нажимает ок(accept)
    alert = browser.switch_to.alert
    alert.accept()

    #решаем задачу для роботов

    #считать значение x
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    print(x)
    
    y = calc(x)
    print(y)

    #находим поле ввода
    input_y = browser.find_element(By.ID, "answer")

    #вводим значение
    input_y.send_keys(y)

    #нажать на кнопку submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
