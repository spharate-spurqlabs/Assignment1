from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("Resource/chromedriver.exe")
driver.get("https://www.calculator.net/bmi-calculator.html?ctype=metric")
driver.maximize_window()

age = driver.find_element(By.ID, 'cage')
age.clear()
age.send_keys(24)
age.click()

try:

    mgen = driver.find_element(By.XPATH, '//*[text()="Male"]')
    mgen.clear()
    mgen.click()

except:
    fgen = driver.find_element(By.XPATH, '//*[text()="Female"]')
    fgen.click()

height = driver.find_element(By.ID, 'cheightmeter')
height.clear()
height.send_keys(180)
height.click()

weight = driver.find_element(By.ID, 'ckg')
weight.clear()
weight.send_keys(45)
weight.click()

calculate = driver.find_element("xpath", "//input[@value='Calculate']")
calculate.click()
sleep(13)

driver.close()
