# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import unittest,re,os

class News(unittest.TestCase):
    '''实用日记'''    
    def setUp(self):
        # chrome_driver = os.path.abspath(r"C:\Program Files (x86)\\Google\Chrome\\Application\chromedriver.exe")
        # os.environ["webdriver.chrome.driver"] = chrome_driver    
        # self.driver = webdriver.Chrome(chrome_driver)
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.base_url = "http://www.kuaiqiangche.com/"
    
    def test_news8(self):
        driver = self.driver
        driver.get(self.base_url)
        sleep(0.1)
        driver.refresh()
        driver.find_element_by_xpath(".//*[@id='header']/div[3]/div/div/ul/li[3]/a").click()
        now_handle = driver.current_window_handle
        driver.find_element_by_xpath("html/body/div[2]/div[2]/div[2]/div[3]/ul/li[1]/a").click()
        all_handles =driver.window_handles
        for handle in all_handles:
            if handle != now_handle:
                driver.switch_to.window(handle)
                button = driver.find_element_by_xpath(".//*[@id='footer']/div[2]/div/div[1]/div/div[3]/h3").text
                self.assertEqual(button,u"关于我们",msg="this page is incorrect")

    def tearDown(self):
        self.driver.quit()
        
if __name__ == "__main__":
    unittest.main()
