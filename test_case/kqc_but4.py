# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
import unittest,re,os
import win32api

class button(unittest.TestCase):
    '''免费订阅按钮'''
    def setUp(self):
        # chrome_driver = os.path.abspath(r"C:\Program Files (x86)\\Google\Chrome\\Application\chromedriver.exe")
        # os.environ["webdriver.chrome.driver"] = chrome_driver    
        # self.driver = webdriver.Chrome(chrome_driver)
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.base_url = "http://www.kuaiqiangche.com/"
        
    def test_but4(self):
        driver = self.driver
        driver.get(self.base_url)
        sleep(0.1)
        driver.refresh()
        now_handle = driver.current_window_handle
        driver.find_element_by_xpath(".//*[@id='hotbrand']/div[1]/ul/li[1]/a/span").click()
        all_handles = driver.window_handles
        for handle in all_handles:
            if handle != now_handle:
                driver.switch_to.window(handle)
                driver.find_element_by_xpath(".//*[@id='online-topic']/div/div/form/div/div[3]/div[1]/input").clear()
                driver.find_element_by_xpath(".//*[@id='online-topic']/div/div/form/div/div[3]/div[1]/input").send_keys(u"测试车型")
                driver.find_element_by_xpath(".//*[@id='online-topic']/div/div/form/div/div[3]/div[2]/input").send_keys("13071832065")
                driver.find_element_by_css_selector("button.submit.submit-input").click()
                warn = driver.find_element_by_xpath("html/body/div[6]").text
                self.assertEqual(warn,u"操作成功",msg="your submit failed")
                
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
