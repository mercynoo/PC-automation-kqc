# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import unittest,re,os

class Login(unittest.TestCase):
    '''仅输入手机号'''
    def setUp(self):
        chrome_driver = os.path.abspath(r"C:\Program Files (x86)\\Google\Chrome\\Application\chromedriver.exe")
        os.environ["webdriver.chrome.driver"] = chrome_driver    
        self.driver = webdriver.Chrome(chrome_driver)
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.base_url = "http://www.kuaiqiangche.com/"
    
    def test_login3(self):
    	driver = self.driver
        driver.get(self.base_url)
        sleep(0.1)
        driver.refresh()
        driver.find_element_by_link_text(u"登录").click()
        driver.find_element_by_css_selector("input.login-input.login-tel").clear()
        driver.find_element_by_css_selector("input.login-input.login-tel").send_keys("13071832065")
        driver.find_element_by_xpath(".//*[@id='regin']/form/div[6]").click()
        #判断
        login3 = driver.find_element_by_xpath(".//*[@id='regin']/form/div[6]").text
        self.assertEqual(login3,u"登录",msg="your login is success")
        driver.find_element_by_css_selector("input.login-input.login-tel").clear()
       
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
