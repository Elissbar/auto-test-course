from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 

link = "http://suninjuly.github.io/selects1.html"
path = r"C:\Users\Эдуард Шульц\Desktop\kodtest\python\AutoTesting\chromedriver.exe"

try:
    driver = webdriver.Chrome(executable_path=path)
    driver.get(link)
    
    num1 = driver.find_element_by_id('num1')
    num2 = driver.find_element_by_id('num2')

    summ = int( num1.text ) + int( num2.text )

    select = Select( driver.find_element_by_id('dropdown') )
    select.select_by_value( str(summ) )

    btn = driver.find_element_by_class_name('btn')
    btn.click()    

finally: 
    pass
