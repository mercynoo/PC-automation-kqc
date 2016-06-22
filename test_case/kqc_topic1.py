# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
import unittest,re,urllib,os

class Topic(unittest.TestCase):
    '''第一个专题'''    
    def setUp(self):
        chrome_driver = os.path.abspath(r"C:\Program Files (x86)\\Google\Chrome\\Application\chromedriver.exe")
        os.environ["webdriver.chrome.driver"] = chrome_driver    
        self.driver = webdriver.Chrome(chrome_driver)
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.base_url = "http://www.kuaiqiangche.com/"
    
    def test_topic1(self):
        driver = self.driver
        driver.get(self.base_url)
        sleep(0.1)
        driver.refresh()
        driver.find_element_by_xpath(".//*[@id='banner-slider']/div/div/ul/li/a/img").click()
        now_handle = driver.current_window_handle
        driver.find_element_by_xpath("html/body/div[2]/div/div[3]/div[1]/a").click()
        all_handles =driver.window_handles
        for handle in all_handles:
            if handle != now_handle:
                driver.switch_to.window(handle)
                url = driver.current_url
                statusCode = urllib.urlopen(url).getcode()
                self.assertEqual(statusCode,200,msg="page status error")
                title = driver.find_element_by_xpath("html/body/div[2]/div/div[3]/div[2]/div[1]/span[2]/span[2]").text
                self.assertEqual(title,u"参数配置",msg="your click is failed")
                
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
