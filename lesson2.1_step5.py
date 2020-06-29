import math
from selenium import webdriver
import time 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"
path = r"C:\Users\Эдуард Шульц\Desktop\kodtest\python\AutoTesting\chromedriver.exe"

try:
    driver = webdriver.Chrome(executable_path=path)
    driver.get(link)

    x_element = driver.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    answer = driver.find_element_by_id('answer')
    answer.send_keys(y)

    driver.find_element_by_id('robotCheckbox').click()
    driver.find_element_by_id('robotsRule').click()
    driver.find_element_by_class_name('btn').click()

finally: 
    pass

