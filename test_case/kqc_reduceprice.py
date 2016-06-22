# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import unittest,re,os

class Reduce(unittest.TestCase):
    '''降价通知'''
    def setUp(self):
        chrome_driver = os.path.abspath(r"C:\Program Files (x86)\\Google\Chrome\\Application\chromedriver.exe")
        os.environ["webdriver.chrome.driver"] = chrome_driver    
        self.driver = webdriver.Chrome(chrome_driver)
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.base_url = "http://www.kuaiqiangche.com/"
    
    def test_reduce(self):
        driver = self.driver
        driver.get(self.base_url)
        sleep(0.1)
        driver.refresh()
        driver.find_element_by_link_text(u"登录").click()
        driver.find_element_by_css_selector("input.login-input.login-tel").clear()
        driver.find_element_by_css_selector("input.login-input.login-tel").send_keys("13071832065")
        driver.find_element_by_css_selector("input.login-input.login-code").clear()
        driver.find_element_by_css_selector("input.login-input.login-code").send_keys("1111" +Keys.RETURN)
        sleep(2)
        #搜车
        input_car = driver.find_element_by_xpath(".//*[@id='header']/div[2]/div/div[3]/form/div[1]/input")
        input_car.clear()
        input_car.send_keys(u"思铂睿")
        driver.find_element_by_class_name("search-button").click()
        sleep(2)
        #选车
        now_handle = driver.current_window_handle
        driver.find_element_by_xpath("html/body/div[2]/div[4]/ul/li/div[1]/a/img").click()
        all_handles = driver.window_handles
        for handle in all_handles:
            if handle != now_handle:
                driver.switch_to.window(handle)
                driver.find_element_by_xpath("html/body/div[2]/div/div[2]/div[2]/div[1]/div[1]/button[1]").click()#降价通知
                driver.find_element_by_xpath("html/body/div[6]/div[3]/div[2]/div[2]/input").send_keys("13071832065")
                driver.find_element_by_xpath("html/body/div[6]/div[3]/button").click()
                sleep(0.1)
                notice = driver.find_element_by_xpath("html/body/div[8]").text
                self.assertEqual(notice,u"操作成功",msg="your click is failed")

    def tearDown(self):
        self.driver.quit()
        
if __name__ == "__main__":
    unittest.main()
            