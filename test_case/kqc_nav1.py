# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import unittest,re,os

class Navigation(unittest.TestCase):
    '''首页按钮'''
    def setUp(self):
        chrome_driver = os.path.abspath(r"C:\Program Files (x86)\\Google\Chrome\\Application\chromedriver.exe")
        os.environ["webdriver.chrome.driver"] = chrome_driver    
        self.driver = webdriver.Chrome(chrome_driver)
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.base_url = "http://www.kuaiqiangche.com/"
        
    def test_nav1(self):
        driver = self.driver
        driver.get(self.base_url)
        sleep(0.1)
        driver.refresh()
        driver.find_element_by_xpath(".//*[@id='header']/div[3]/div/div/ul/li[1]/a").click()
        url = driver.current_url
        self.assertEqual(url,"http://www.kuaiqiangche.com/",msg="failed")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
