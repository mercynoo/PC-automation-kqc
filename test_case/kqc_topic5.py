# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
import unittest,re,urllib,os
from selenium.webdriver.common.action_chains import ActionChains  
import win32api
import win32con

class Topic(unittest.TestCase):
    '''第五个专题'''   
    def setUp(self):
        chrome_driver = os.path.abspath(r"C:\Program Files (x86)\\Google\Chrome\\Application\chromedriver.exe")
        os.environ["webdriver.chrome.driver"] = chrome_driver    
        self.driver = webdriver.Chrome(chrome_driver)
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.base_url = "http://www.kuaiqiangche.com/"

    def test_topic5(self):
        driver = self.driver
        driver.get(self.base_url)
        sleep(0.1)
        driver.refresh()
        win32api.keybd_event(34,0,0,0)
        sleep(1)    
        now_handle = driver.current_window_handle
        ele = driver.find_element_by_xpath(".//*[@id='activity-list']/div[2]/a/img")
        ActionChains(driver).move_to_element(ele).click().perform() 
        all_handles =driver.window_handles
        for handle in all_handles:
            if handle != now_handle:
                driver.switch_to.window(handle)
                judge = driver.find_element_by_xpath(".//*[@id='footer']/div[2]/div/div[1]/div[1]/div[3]/h3").text
                self.assertEqual(judge,u"关于我们",msg="this page is incorrect")
                new_handle = driver.current_window_handle        
                driver.find_element_by_xpath("html/body/div[2]/div/div[8]/div[1]/a").click()#天苍苍野茫茫
                sleep(1)
                new_all_handle = driver.window_handles
                for handlenew in new_all_handle:
                    if handlenew != new_handle and handlenew != now_handle:
                        driver.switch_to.window(handlenew)
                        url = driver.current_url
                        statusCode =urllib.urlopen(url).getcode()
                        self.assertEqual(statusCode,200,msg="page status error")
                        title = driver.find_element_by_xpath("html/body/div[2]/div/div[3]/div[2]/div[1]/span[2]/span[4]").text
                        self.assertEqual(title,u"提车日记",msg="this car is invisible")
      
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
