# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import unittest,re,os

class Navigation(unittest.TestCase):
    '''帮助中心'''    
    def setUp(self):
        chrome_driver = os.path.abspath(r"C:\Program Files (x86)\\Google\Chrome\\Application\chromedriver.exe")
        os.environ["webdriver.chrome.driver"] = chrome_driver    
        self.driver = webdriver.Chrome(chrome_driver)
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.base_url = "http://www.kuaiqiangche.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_nav3(self):
        driver = self.driver
        driver.get(self.base_url)
        sleep(0.1)
        driver.refresh()
        driver.find_element_by_xpath(".//*[@id='header']/div[3]/div/div/ul/li[4]/a").click()
        url = driver.current_url
        self.assertEqual(url,"http://www.kuaiqiangche.com/help",msg="failed")
        title = driver.find_element_by_xpath("html/body/div[2]/div/div[1]/ul/li[4]/dl/dt").text
        self.assertEqual(title,u"关于我们",msg="page error")
        
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
