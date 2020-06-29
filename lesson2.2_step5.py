import math
from selenium import webdriver
import time 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"
path = r"C:\Users\Эдуард Шульц\Desktop\kodtest\python\AutoTesting\chromedriver.exe"

try:
    driver = webdriver.Chrome(executable_path=path)
    driver.get(link)

    btn = driver.find_element_by_class_name('btn')
    x_element = driver.find_element_by_id('input_value')

    x = x_element.text
    y = calc(x)

    driver.execute_script("return arguments[0].scrollIntoView(true);", driver.find_element_by_id('answer'))

    driver.find_element_by_id('answer').send_keys(y)

    driver.find_element_by_id('robotCheckbox').click()

    driver.find_element_by_id('robotsRule').click()

    btn.click()

finally: 
    pass

