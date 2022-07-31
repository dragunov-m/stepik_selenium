import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


def captcha():
    # Options
    options = Options()
    options.add_argument('headless')
    #

    # Service
    service = Service(executable_path='/home/user/chromedriver')
    #

    # Driver
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(5)
    #

    url = 'http://suninjuly.github.io/math.html'
    driver.get(url)

    x_element = driver.find_element(By.ID, 'input_value')
    x = x_element.text
    calculation = calc(x)

    answer = driver.find_element(By.ID, 'answer')
    answer.send_keys(calculation)

    checkbox = driver.find_element(By.ID, 'robotCheckbox')
    checkbox.click()

    radio = driver.find_element(By.ID, 'robotsRule')
    radio.click()

    button_submit = driver.find_element(By.XPATH, '//button[@type="submit"]')
    button_submit.click()

    alert_message = driver.switch_to.alert
    alert_text = alert_message.text

    print(alert_text)

    driver.quit()


if __name__ == '__main__':
    captcha()
