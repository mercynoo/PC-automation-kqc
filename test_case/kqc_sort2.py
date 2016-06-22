# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import unittest,re,os
import win32api
import win32con

class Sort(unittest.TestCase):
    '''平行进口排序'''
    def setUp(self):
        # chrome_driver = os.path.abspath(r"C:\Program Files (x86)\\Google\Chrome\\Application\chromedriver.exe")
        # os.environ["webdriver.chrome.driver"] = chrome_driver    
        # self.driver = webdriver.Chrome(chrome_driver)
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.base_url = "http://www.kuaiqiangche.com/"

    def test_sort2(self):
        driver = self.driver
        driver.get(self.base_url)
        sleep(0.1)
        driver.refresh()
        win32api.keybd_event(35,0,0,0)
        sleep(1)
        now_handle = driver.current_window_handle
        driver.find_element_by_xpath(".//*[@id='imported-cars']/div[1]/a").click()
        all_handles =driver.window_handles
        for handle in all_handles:
            if handle != now_handle:
                driver.switch_to.window(handle)
                #价格排序
                driver.find_element_by_xpath("html/body/div[2]/div[3]/ul/li[2]/a/span").click()
                price1 = driver.find_element_by_xpath("html/body/div[2]/div[4]/ul/li[1]/div[2]/div/span[1]/b").text
                price2 = driver.find_element_by_xpath("html/body/div[2]/div[4]/ul/li[9]/div[2]/div/span[1]/b").text
                if int(price1) < int(price2):
                    print "sort is correct"
                else:
                    print "sort is failed"
                sleep(1)
                driver.find_element_by_xpath("html/body/div[2]/div[3]/ul/li[2]/a/span").click()
                price3 = driver.find_element_by_xpath("html/body/div[2]/div[4]/ul/li[1]/div[2]/div/span[1]/b").text
                price4 = driver.find_element_by_xpath("html/body/div[2]/div[4]/ul/li[9]/div[2]/div/span[1]/b").text
                if int(price3) > int(price4):
                    print "sort is correct"
                else:
                    print "sort is failed"
                #优惠排序
                driver.find_element_by_xpath("html/body/div[2]/div[3]/ul/li[3]/a/span").click()
                sleep(0.5)
                discount1 = driver.find_element_by_xpath("html/body/div[2]/div[4]/ul/li[1]/div[2]/div/span[3]").text
                a = re.findall(r"[0-9]+.+[0-9]+",discount1)
                a1 = a[0]
                win32api.keybd_event(35,0,0,0)
                sleep(1)
                discount2 = driver.find_element_by_xpath("html/body/div[2]/div[4]/ul/li[9]/div[2]/div/span[3]").text
                b = re.findall(r"[0-9]+",discount2)
                b1 = b[0]
                if a1>b1:
                    print "sort is correct"
                else:
                    print "sort is failed"
                sleep(1)
                driver.find_element_by_xpath("html/body/div[2]/div[3]/ul/li[3]/a/span").click()
                discount3 = driver.find_element_by_xpath("html/body/div[2]/div[4]/ul/li[1]/div[2]/div/span[3]").text
                c = re.findall(r"[0-9]+",discount3)
                c1 = c[0]
                win32api.keybd_event(35,0,0,0)
                sleep(1)
                discount4 = driver.find_element_by_xpath("html/body/div[2]/div[4]/ul/li[9]/div[2]/div/span[3]").text
                d = re.findall(r"[0-9]+.+[0-9]+",discount4)
                d1 = d[0]
                if c1 < d1:
                    print "sort is correct"
                else:
                    print "sort is failed"

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
