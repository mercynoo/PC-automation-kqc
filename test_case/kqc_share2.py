# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
import unittest,re,os,urllib

class Share(unittest.TestCase):
    '''车辆详情页面空间的分享'''
    def setUp(self):
        # chrome_driver = os.path.abspath(r"C:\Program Files (x86)\\Google\Chrome\\Application\chromedriver.exe")
        # os.environ["webdriver.chrome.driver"] = chrome_driver    
        # self.driver = webdriver.Chrome(chrome_driver)
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.base_url = "http://www.kuaiqiangche.com/detail/8"

    def test_share2(self):
        driver = self.driver
        driver.get(self.base_url)
        sleep(0.1)
        #判断联动
        driver.find_element_by_xpath("html/body/div[2]/div/div[2]/div[2]/div[2]/div[2]").click()
        try:
            driver.find_element_by_xpath("//*[@id='banner-slider']/div/div[1]/ul/li[3]/a/img").is_displayed()
        except:
            print "未找到图片元素"
        else:
            print "图片元素存在"
        #判断计算器是否出现
        driver.find_element_by_css_selector(".car-price-calculator").click()
        cal = driver.find_element_by_xpath(".//*[@id='calculator']/div[1]/span[1]").text
        self.assertEqual(cal,u"购车计算器",msg="calculator is normal")
        driver.find_element_by_css_selector("div.calculator-close").click()
        now_handle = driver.current_window_handle
        driver.find_element_by_xpath("html/body/div[2]/div/div[2]/div[1]/div[3]/div[3]").click()                
        all_handles = driver.window_handles
        for handle in all_handles:
            if handle != now_handle:
                driver.switch_to.window(handle)
                url = driver.current_url
                statusCode =urllib.urlopen(url).getcode()
                self.assertEqual(statusCode,200,msg="page status error")
                
    def tearDown(self):
        self.driver.quit()
        
if __name__ == "__main__":
    unittest.main()