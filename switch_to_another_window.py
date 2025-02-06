from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x1):
  return str(math.log(abs(12*math.sin(int(x1)))))

value1="input_value"
value2="answer"


link="http://suninjuly.github.io/redirect_accept.html"


browser = webdriver.Chrome()
browser.get(link)

try:
    #Нажмаем на кнопку в окне
    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    button.click()

    # Переключаемся на новую вкладку
    browser.switch_to.window(browser.window_handles[1])

    # Считываем значение для переменной x
    x_element = browser.find_element(By.ID, value1).text
    # Получаем результат математической функцию от x
    y = calc(x_element)
    # Вводим ответ в текстовое поле
    answer = browser.find_element(By.ID, value2)
    answer.send_keys(str(y))

    # Нажимаем кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
   # Выводим результат сообщения (алерта) для отправки решения 
    print('Ответ для отправки решения: ', browser.switch_to.alert.text.split()[-1])
    # Оцениваем сделаную работу
    time.sleep(3)


finally:

    # Закрываем браузер после всех манипуляций
    browser.quit()
