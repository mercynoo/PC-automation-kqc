# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import unittest,re,urllib,os

class Navigation(unittest.TestCase):
    '''提车网点'''    
    def setUp(self):
        chrome_driver = os.path.abspath(r"C:\Program Files (x86)\\Google\Chrome\\Application\chromedriver.exe")
        os.environ["webdriver.chrome.driver"] = chrome_driver    
        self.driver = webdriver.Chrome(chrome_driver)
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.base_url = "http://www.kuaiqiangche.com/"

    def test_nav4(self):
        driver = self.driver
        driver.get(self.base_url)
        sleep(0.1)
        driver.refresh()
        driver.find_element_by_xpath(".//*[@id='header']/div[3]/div/div/ul/li[5]/a").click()
        url = driver.current_url
        self.assertEqual(url,"http://www.kuaiqiangche.com/shop",msg="failed")
        place = driver.find_element_by_xpath(".//*[@id='sites-wrap']/div[3]/div[1]").text
        self.assertEqual(place,u"湖南省",msg="page error")
        statusCode =urllib.urlopen(url).getcode()
        self.assertEqual(statusCode,200,msg="page status error")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
