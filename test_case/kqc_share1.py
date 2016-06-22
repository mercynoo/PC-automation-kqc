# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import unittest,re,os,urllib

class Share(unittest.TestCase):
    '''车辆详情页面微博的分享'''
    def setUp(self):
        # chrome_driver = os.path.abspath(r"C:\Program Files (x86)\\Google\Chrome\\Application\chromedriver.exe")
        # os.environ["webdriver.chrome.driver"] = chrome_driver    
        # self.driver = webdriver.Chrome(chrome_driver)
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.base_url = "http://www.kuaiqiangche.com/detail/8"
        
    def test_share1(self):
        driver = self.driver
        driver.get(self.base_url)
        sleep(0.1)
        now_handle = driver.current_window_handle
        driver.find_element_by_xpath("html/body/div[2]/div/div[2]/div[1]/div[3]/div[1]").click()
        all_handles = driver.window_handles
        for handle in all_handles:
            if handle != now_handle:
                driver.switch_to.window(handle)      
                url = driver.current_url
                statusCode =urllib.urlopen(url).getcode()
                self.assertEqual(statusCode,200,msg="page status error")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()