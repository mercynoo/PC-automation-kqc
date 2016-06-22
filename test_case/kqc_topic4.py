# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains  
import unittest,re,urllib,os
import win32api
import win32con

class Topic(unittest.TestCase):
    '''第四个专题'''   
    def setUp(self):
        chrome_driver = os.path.abspath(r"C:\Program Files (x86)\\Google\Chrome\\Application\chromedriver.exe")
        os.environ["webdriver.chrome.driver"] = chrome_driver    
        self.driver = webdriver.Chrome(chrome_driver)
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.base_url = "http://www.kuaiqiangche.com/"

    def test_topic4(self):
        driver = self.driver
        driver.get(self.base_url)
        sleep(0.1)
        driver.refresh()
        win32api.keybd_event(34,0,0,0)
        sleep(1)    
        now_handle = driver.current_window_handle
        ele = driver.find_element_by_xpath(".//*[@id='activity-list']/div[1]/a/img")
        ActionChains(driver).move_to_element(ele).click().perform() 
        all_handles =driver.window_handles
        for handle in all_handles:
            if handle != now_handle:
                driver.switch_to.window(handle)
                judge = driver.find_element_by_xpath(".//*[@id='footer']/div[2]/div/div[1]/div[1]/div[3]/h3").text
                self.assertEqual(judge,u"关于我们",msg="this page is incorrect")
                new_handle = driver.current_window_handle        
                driver.find_element_by_xpath("html/body/div[2]/div/div[4]/div/a").click()#SUV大乱斗
                sleep(1)
                new_all_handle = driver.window_handles
                for handlenew in new_all_handle:
                    if handlenew != new_handle and handlenew != now_handle:
                        driver.switch_to.window(handlenew)
                        url = driver.current_url
                        statusCode =urllib.urlopen(url).getcode()
                        self.assertEqual(statusCode,200,msg="page status error")
                        
      
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
