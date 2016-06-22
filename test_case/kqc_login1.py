# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import unittest,re,os

class Login(unittest.TestCase):   
    '''正确登录'''
    def setUp(self):
        chrome_driver = os.path.abspath(r"C:\Program Files (x86)\\Google\Chrome\\Application\chromedriver.exe")
        os.environ["webdriver.chrome.driver"] = chrome_driver    
        self.driver = webdriver.Chrome(chrome_driver)
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.base_url = "http://www.kuaiqiangche.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_login1(self):
        driver = self.driver
        driver.get(self.base_url)
        sleep(0.1)
        driver.refresh()
        driver.find_element_by_link_text(u"登录").click()
        driver.find_element_by_css_selector("input.login-input.login-tel").clear()
        driver.find_element_by_css_selector("input.login-input.login-tel").send_keys("13071832065")
        driver.find_element_by_css_selector("input.login-input.login-code").clear()
        driver.find_element_by_css_selector("input.login-input.login-code").send_keys("1111" +Keys.RETURN)
        sleep(0.5)
        #判断是否成功登录
        login = driver.find_element_by_xpath(".//*[@id='header']/div[1]/div[2]/div[1]/a/span").text
        self.assertEqual(login,u"欢迎，13071832065",msg="your login is fail")

        driver.find_element_by_xpath(".//*[@id='header']/div[1]/div[2]/div[1]/a/span").click()
        sleep(2)
        order = driver.find_element_by_xpath("html/body/div[2]/div[2]/div[1]").text
        self.assertEqual(order,u"商品信息",msg="click is fail")
        sleep(2)
        driver.find_element_by_link_text(u"注销").click()
        sleep(0.5)
       
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
