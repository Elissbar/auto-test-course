import os
from selenium import webdriver

link = "http://suninjuly.github.io/file_input.html"
path = r"C:\Users\Эдуард Шульц\Desktop\kodtest\python\AutoTesting\chromedriver.exe"
# current_dir = os.path.dirname( __file__ )
# file_path = os.path.join(current_dir, 'file.txt')
file_path = os.getcwd() + '/' + "file.txt"

try:
    driver = webdriver.Chrome(executable_path=path)
    driver.get(link)

    f_name = driver.find_element_by_name( 'firstname' )
    l_name = driver.find_element_by_name( 'lastname' )
    email = driver.find_element_by_name( 'email' )
    input_file = driver.find_element_by_name( 'file' )
    btn = driver.find_element_by_class_name( 'btn' )

    f_name.send_keys('Eduard')
    l_name.send_keys('Eduard')
    email.send_keys('Eduard')
    input_file.send_keys(file_path)

    btn.click()


finally: 
    pass
