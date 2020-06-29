from selenium import webdriver
import time 
import math

url = "http://suninjuly.github.io/find_link_text"
path = r"C:\Users\Эдуард Шульц\Desktop\kodtest\python\AutoTesting\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)

try:
    driver.get( url )
    link = driver.find_element_by_link_text( str(math.ceil(math.pow(math.pi, math.e)*10000)) )
    link.click()

    first_name = driver.find_element_by_name('first_name')
    first_name.send_keys('Eduard')
    last_name = driver.find_element_by_name('last_name')
    last_name.send_keys('Eduard')
    city = driver.find_element_by_name('firstname')
    city.send_keys('Moscow')
    land = driver.find_element_by_id('country')
    land.send_keys('Moscow')

    btn = driver.find_element_by_class_name('btn')
    btn.click()


finally:
    pass
