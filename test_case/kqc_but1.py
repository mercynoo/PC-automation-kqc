# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
import unittest,re,os

class Button(unittest.TestCase):
    '''右侧第一个按钮'''
    def setUp(self):
        chrome_driver = os.path.abspath(r"C:\Program Files (x86)\\Google\Chrome\\Application\chromedriver.exe")
        os.environ["webdriver.chrome.driver"] = chrome_driver    
        self.driver = webdriver.Chrome(chrome_driver)
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.base_url = "http://www.kuaiqiangche.com/"

    def test_but1(self):
        driver = self.driver
        driver.get(self.base_url)
        sleep(0.1)
        driver.refresh()
        now_handle = driver.current_window_handle
        driver.find_element_by_xpath("html/body/ul/li[1]").click()
        sleep(5)
        all_handles =driver.window_handles
        for handle in all_handles:
            if handle != now_handle:
                driver.switch_to.window(handle)
                driver.find_element_by_id("txtMsg").clear()
                driver.find_element_by_id("txtMsg").send_keys("test")
                driver.find_element_by_id("btnSend").click()
                sleep(1)
                content = driver.find_element_by_xpath(".//*[@id='content']/dl/dd/div/span").text
                self.assertEqual(content,u"您好，有什么可以帮您的么?")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
