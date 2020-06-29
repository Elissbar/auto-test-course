import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"
path = r"C:\Users\Эдуард Шульц\Desktop\kodtest\python\AutoTesting\chromedriver.exe"

try:
    driver = webdriver.Chrome(executable_path=path)
    driver.get(link)
    wait = WebDriverWait(driver, 12)

    wait.until( EC.text_to_be_present_in_element( ( By.ID, 'price' ), "$100" ) )
    driver.find_element_by_id('book').click()

    x = driver.find_element_by_id('input_value').text
    y = calc(x)

    driver.find_element_by_id('answer').send_keys(y)

    driver.execute_script('return arguments[0].scrollIntoView(true)', driver.find_element_by_id('solve'))
    
    driver.find_element_by_id('solve').click()

finally: 
    pass
