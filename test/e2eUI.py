import pytest 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions 

def test_form_submission():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()

    #Select the UI to automate
    driver.get("https://rahulshettyacademy.com/angularpractice/")

    #identifying developer atrtributes and creationg suitable locators out of it
    driver.find_element_by_name("name").send_keys("Chiran")
    driver.find_element_by_name("email").send_keys("daschiran@pqrd")
    driver.find_element_by_id("exampleInputPassword1").send_keys("password")
    driver.find_element_by_id("exampleCheck1").click()

    #driver.find_element_by_id("exampleFormControlSelect1").send_keys("Male")


    #select class provide the methods to handle the options in dropdown
    dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
    dropdown.select_by_visible_text("Female")
    dropdown.select_by_index(0)

    driver.find_element_by_xpath("//input[@type='submit']").click()

    message = driver.find_element_by_class_name("alert-success").text
    print(driver.find_element_by_class_name("alert-success").text)

    #check whether subtext "Sucess" present in 'message' or not
    assert "Success" in message
    driver.quit()


def test_checkout():
    driver = webdriver.Chrome(ChromeDriverManager().install())

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.find_element_by_css_selector("a[href*='shop']").click()
    products = driver.find_elements_by_xpath("//div[@class='card h-100']")

    #//div[@class='card h-100']/div/h4/a
    #product =//div[@class='card h-100']
    for product in products:
        productName = product.find_element_by_xpath("div/h4/a").text
        if productName == "Blackberry":
        #Add item into cart
            product.find_element_by_xpath("div/button").click()

    #click on checkout
    driver.find_element_by_css_selector("a[class*='btn-primary']").click()

    #total_amount =(driver.find_element_by_xpath("/html[1]/body[1]/app-root[1]/app-shop[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[3]/td[5]/h3[1]/strong[1]").text)
    #print("Total amount is : "+ total_amount)

    driver.find_element_by_xpath("//button[@class='btn btn-success']").click()

    #pass autosuggestive value ind
    driver.find_element_by_id("country").send_keys("ind")
    wait = WebDriverWait(driver, 7)
    wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
    driver.find_element_by_link_text("India").click()
    driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()

    #click on purchase
    driver.find_element_by_css_selector("[type='submit']").click()
    successText = driver.find_element_by_class_name("alert-success").text
    print(successText)
    
    assert "Success! Thank you!" in successText

    driver.get_screenshot_as_file("screen.png")
    driver.quit()




