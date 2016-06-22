# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import unittest,re,os
import win32api

class Banner(unittest.TestCase):
    '''banner专题'''   
    def setUp(self):
        chrome_driver = os.path.abspath(r"C:\Program Files (x86)\\Google\Chrome\\Application\chromedriver.exe")
        os.environ["webdriver.chrome.driver"] = chrome_driver    
        self.driver = webdriver.Chrome(chrome_driver)
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.base_url = "http://www.kuaiqiangche.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
        
    def test_banner(self):
        driver = self.driver
        driver.get(self.base_url)
        sleep(0.1)
        driver.refresh()
        now_handle = driver.current_window_handle
        driver.find_element_by_xpath("html/body/a/div").click()
        all_handles =driver.window_handles
        for handle in all_handles:
            if handle != now_handle:
                driver.switch_to.window(handle)
                url = driver.current_url
                self.assertEqual(url,"http://www.kuaiqiangche.com/detail/3621",msg="url is incorrect")
                we = driver.find_element_by_xpath("html/body/div[2]/div/div[2]/div[2]/h1").text
                self.assertEqual(we,u"标致4082014款 1.8L 自动 豪华版",msg="page is error")
      
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
