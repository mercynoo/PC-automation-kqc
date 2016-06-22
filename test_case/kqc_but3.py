# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
import unittest,re,os

class Button(unittest.TestCase):
    '''底部找车按钮'''
    def setUp(self):
        chrome_driver = os.path.abspath(r"C:\Program Files (x86)\\Google\Chrome\\Application\chromedriver.exe")
        os.environ["webdriver.chrome.driver"] = chrome_driver    
        self.driver = webdriver.Chrome(chrome_driver)
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.base_url = "http://www.kuaiqiangche.com/"

    def test_but3(self):
        driver = self.driver
        driver.get(self.base_url)
        sleep(0.1)
        driver.refresh()
        driver.find_element_by_id("attention").clear()
        driver.find_element_by_id("attention").send_keys(u"测试")
        driver.find_element_by_id("phone").clear()
        driver.find_element_by_id("phone").send_keys("13071832065")
        driver.find_element_by_id("sendAttention").click()
        sleep(0.1)
        mess = driver.find_element_by_xpath("html/body/div[6]").text
        self.assertEqual(mess,u"操作成功",msg="send failed")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
