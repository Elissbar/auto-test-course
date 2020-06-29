from selenium import webdriver
import time

url = "http://suninjuly.github.io/huge_form.html"
path = r"C:\Users\Эдуард Шульц\Desktop\kodtest\python\AutoTesting\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)

try:
    driver.get("http://suninjuly.github.io/huge_form.html")
    elements = driver.find_elements_by_css_selector('input[type="text"]')
    for element in elements:
       element.send_keys("Мой ответ")

    button = driver.find_element_by_css_selector("button.btn")
    button.click()

finally:
    pass
