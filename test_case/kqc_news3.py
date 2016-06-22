# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
import unittest,re,urllib,os
import win32api

class News(unittest.TestCase):    
    '''第三个日记(首页)'''
    def setUp(self):
        chrome_driver = os.path.abspath(r"C:\Program Files (x86)\\Google\Chrome\\Application\chromedriver.exe")
        os.environ["webdriver.chrome.driver"] = chrome_driver    
        self.driver = webdriver.Chrome(chrome_driver)
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.base_url = "http://www.kuaiqiangche.com/"
    
    def test_news3(self):
        driver = self.driver
        driver.get(self.base_url)
        sleep(0.1)
        driver.refresh()
        win32api.keybd_event(35,0,0,0)
        sleep(1)
        win32api.keybd_event(35,0,0,0)
        now_handle = driver.current_window_handle
        a = driver.find_elements_by_css_selector(".community-title-1>a")
        a[2].click()
        all_handles = driver.window_handles
        for handle in all_handles:
            if handle != now_handle:
                driver.switch_to.window(handle)
                url = driver.current_url
                statusCode =urllib.urlopen(url).getcode()
                self.assertEqual(statusCode,200,msg="page status error")
                button = driver.find_element_by_xpath(".//*[@id='footer']/div[2]/div/div[1]/div/div[3]/h3").text
                self.assertEqual(button,u"关于我们",msg="this page is incorrect")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
