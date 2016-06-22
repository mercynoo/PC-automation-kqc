# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
import unittest,re,os

class Button(unittest.TestCase):
    '''右侧最后那个按钮'''
    def setUp(self):
        chrome_driver = os.path.abspath(r"C:\Program Files (x86)\\Google\Chrome\\Application\chromedriver.exe")
        os.environ["webdriver.chrome.driver"] = chrome_driver    
        self.driver = webdriver.Chrome(chrome_driver)
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.base_url = "http://www.kuaiqiangche.com/"

    def test_but2(self):
        driver = self.driver
        driver.get(self.base_url)
        sleep(0.1)
        driver.refresh()
        driver.find_element_by_xpath("html/body/ul/li[4]").click()
        sleep(1)
        driver.find_element_by_css_selector("textarea").clear()
        driver.find_element_by_css_selector("textarea").send_keys(u"测试")
        sleep(1)
        driver.find_element_by_xpath("html/body/div[6]/div[2]/div/input").send_keys("13071832065")
        driver.find_element_by_xpath("html/body/div[6]/div[2]/div/button").click()
        sleep(0.1)
        mess = driver.find_element_by_xpath("html/body/div[8]").text
        self.assertEqual(mess,u"吐槽成功,感谢吐槽",msg="send failed")
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
