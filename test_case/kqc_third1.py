# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import unittest,re,os

class Third(unittest.TestCase):
    '''第一个链接'''    
    def setUp(self):
        chrome_driver = os.path.abspath(r"C:\Program Files (x86)\\Google\Chrome\\Application\chromedriver.exe")
        os.environ["webdriver.chrome.driver"] = chrome_driver    
        self.driver = webdriver.Chrome(chrome_driver)
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.base_url = "http://www.kuaiqiangche.com/"
   
    def test_third1(self):
        driver = self.driver
        driver.get(self.base_url)
        sleep(0.1)
        driver.refresh()
        now_handle = driver.current_window_handle
        ele = driver.find_element_by_xpath(".//*[@id='auto-insurance']/div[1]/a")
        ActionChains(driver).move_to_element(ele).click().perform() 
        sleep(0.1)       
        all_handles =driver.window_handles
        for handle in all_handles:
            if handle != now_handle:
                driver.switch_to.window(handle)
                url = driver.current_url
                self.assertEqual(url,"http://www.kuaiqiangche.com/topics/detail/loan0",msg="url is incorrect")
                we = driver.find_element_by_xpath(".//*[@id='footer']/div[2]/div/div[1]/div/div[3]/h3").text
                self.assertEqual(we,u"关于我们",msg="page is error")               

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
