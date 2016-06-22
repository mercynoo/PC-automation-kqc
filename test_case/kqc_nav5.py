# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import unittest,re,os

class Navigation(unittest.TestCase):
    '''快比价'''   
    def setUp(self):
        # chrome_driver = os.path.abspath(r"C:\Program Files (x86)\\Google\Chrome\\Application\chromedriver.exe")
        # os.environ["webdriver.chrome.driver"] = chrome_driver    
        # self.driver = webdriver.Chrome(chrome_driver)
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.base_url = "http://www.kuaiqiangche.com/"

    def test_nav5(self):
        driver = self.driver
        driver.get(self.base_url)
        sleep(0.1)
        driver.refresh()
        big1 = driver.find_element_by_xpath(".//*[@id='header']/div[3]/div/div/ul/li[2]/a")
        ActionChains(driver).move_to_element(big1).click().perform()
        driver.find_element_by_xpath(".//*[@id='header']/div[3]/div/div/ul/li[2]/ul/li[1]/a").click()
        sleep(1)
        url1 = driver.current_url
        self.assertEqual(url1,"http://www.kuaiqiangche.com/topics/detail/30",msg="failed")
        judge = driver.find_element_by_xpath(".//*[@id='footer']/div[2]/div/div[1]/div[1]/div[3]/h3").text
        self.assertEqual(judge,u"关于我们",msg="the page is failed")
        driver.back()
        sleep(1)
        driver.refresh()
        big2 = driver.find_element_by_xpath(".//*[@id='header']/div[3]/div/div/ul/li[2]/a")
        ActionChains(driver).move_to_element(big2).click().perform()
        driver.find_element_by_xpath(".//*[@id='header']/div[3]/div/div/ul/li[2]/ul/li[2]/a").click()
        url2 = driver.current_url
        self.assertEqual(url2,"http://www.kuaiqiangche.com/topics/detail/34",msg="failed")
        self.assertEqual(judge,u"关于我们",msg="the page is failed")
               
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
