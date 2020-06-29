import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"
path = r"C:\Users\Эдуард Шульц\Desktop\kodtest\python\AutoTesting\chromedriver.exe"

try:
    driver = webdriver.Chrome(executable_path=path)
    driver.get(link)

    driver.find_element_by_class_name( 'trollface' ).click()

    new_window = driver.window_handles[1]
    old_window = driver.window_handles[0]

    driver.switch_to.window( new_window )

    x = driver.find_element_by_id('input_value').text
    y = calc(x)

    driver.find_element_by_id('answer').send_keys(y)
    
    driver.find_element_by_class_name('btn').click()


finally: 
    pass
