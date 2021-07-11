from UIAutoPytest.testenv.DAGSample.Utilities.baseClass import BaseClass
#from DAGSample.Utilities.baseClass import BaseClass
# from UIAutoPytest.testenv.DAGSample.pageObjects.Checkoutpage import CheckOutPage
# from UIAutoPytest.testenv.DAGSample.pageObjects.Homepage import HomePage
import pytest 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions 


#@pytest.mark.usefixtures("setup")
class test_shope2e(BaseClass):

    def test_e2e(self):
        
        self.driver.find_element_by_css_selector("a[href*='shop']").click()
        products = self.driver.find_elements_by_xpath("//div[@class='card h-100']")

        #//div[@class='card h-100']/div/h4/a
        #product =//div[@class='card h-100']
        for product in products:
            productName = product.find_element_by_xpath("div/h4/a").text
            if productName == "Blackberry":
            #Add item into cart
                product.find_element_by_xpath("div/button").click()

        #click on checkout
        self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()

        #total_amount =(driver.find_element_by_xpath("/html[1]/body[1]/app-root[1]/app-shop[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[3]/td[5]/h3[1]/strong[1]").text)
        #print("Total amount is : "+ total_amount)

        self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()

        #pass autosuggestive value ind
        self.driver.find_element_by_id("country").send_keys("ind")
        wait = WebDriverWait(self.driver, 7)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.driver.find_element_by_link_text("India").click()
        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()

        #click on purchase
        self.driver.find_element_by_css_selector("[type='submit']").click()
        successText = self.driver.find_element_by_class_name("alert-success").text
        print(successText)
    
        assert "Success! Thank you!" in successText

    #driver.get_screenshot_as_file("screen.png")
        self.driver.quit()
