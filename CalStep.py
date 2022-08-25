from time import sleep

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

use_step_matcher("re")


@given("User is on calculator")
def step_impl(context):
    context.driver = webdriver.Chrome("Resource/chromedriver.exe")
    context.driver.get("https://www.calculator.net/")
    context.driver.maximize_window()


@when("user enter following values")
def step_impl(context):
    num1 = context.table[0][0]
   # print("Num1 is", +num1)
    for i in range(0, len(num1)):
        context.driver.find_element("xpath", " //span[text()='" + num1[i] + "']").click()
        sleep(2)

    operator = context.table[0][2]
    context.driver.find_element("xpath", " //span[text()='" + operator + "']").click()
    sleep(2)

    num2 = context.table[0][1]
    #print("num2 is :" + num2)
    context.driver.find_element("xpath", " //span[text()='" + num2 + "']").click()
    sleep(2)


@when("user verify total")
def step_impl(context):
    result = context.driver.find_element(By.ID, "sciOutPut").text
    result = result.lstrip()
    print("Result is:" + result)
    assert result == result
    sleep(3)
