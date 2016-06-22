# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import unittest,re,os,xlrd,requests,json
from xlrd import open_workbook
from xlutils.copy import copy
from xlwt import easyxf

class Buy(unittest.TestCase):
    '''买车'''
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.base_url = "http://www.kuaiqiangche.com/detail/1234"

    def test_pay1(self):
        driver = self.driver
        driver.get(self.base_url)
        sleep(0.1)
        driver.find_element_by_link_text(u"登录").click()
        driver.find_element_by_css_selector("input.login-input.login-tel").clear()
        driver.find_element_by_css_selector("input.login-input.login-tel").send_keys("13071832065")
        driver.find_element_by_css_selector("input.login-input.login-code").clear()
        driver.find_element_by_css_selector("input.login-input.login-code").send_keys("1111" +Keys.RETURN)
        sleep(1)
        #填写信息
        driver.find_element_by_xpath("html/body/div[2]/div/div[2]/div[2]/div[3]/div/div").click()
        driver.find_element_by_xpath("html/body/div[2]/div/div[2]/div[2]/div[4]/div[1]/div/div/i").click()
        driver.find_element_by_xpath("html/body/ul[2]/li[1]").click()
        driver.find_element_by_xpath("html/body/ul[3]/li[1]").click()
        sleep(0.1)
        driver.find_element_by_xpath("html/body/div[2]/div/div[2]/div[2]/div[5]/button[2]").click()
        sleep(0.1)
        driver.find_element_by_xpath("html/body/div[2]/div/div[2]/div[2]/div[7]/button[1]").click()
        #订单详情页
        driver.find_element_by_xpath(".//*[@id='name']").send_keys(u"测试")
        driver.find_element_by_xpath(".//*[@id='idNumber']").send_keys("411526199301214811")
        driver.find_element_by_xpath(".//*[@id='phone']").send_keys("13071832065")
        sleep(1)
        driver.find_element_by_name("id_img0").send_keys("D:\\new_web\\1.png")
        driver.find_element_by_name("id_img1").send_keys("D:\\new_web\\2.png")
        sleep(0.5)
        driver.find_element_by_xpath(".//*[@id='user-notes']").send_keys("test for pay")
        driver.find_element_by_xpath(".//*[@id='commit']").click()
        sleep(1)
        ale = driver.find_element_by_xpath("html/body/div[5]/div[2]/div/p[1]").text
        self.assertEqual(ale,u"订单已提交成功")
        driver.find_element_by_xpath("html/body/div[5]/div[2]/div/button").click()
        sleep(1)
        confirm = driver.find_element_by_xpath(".//*[@id='order-brief']/div[2]/div[3]/div[1]").text
        self.assertEqual(confirm,u"等待客服确认",msg="return failed")
        num = driver.find_elements_by_xpath(".//*[@id='order-brief']/div[1]/div[2]/span")
        #调用接口修改订单状态
        need = num[0].text
        url = "http://api.sale.kuaiqiangche.com/order/change_sta"
        data = {'ordersn': need,'state':1}
        r = requests.post(url,params=data)
        print r.json()
        # #存入订单到excel方便删除
        # excel = r'D:\order.xls'
        # rb = open_workbook(excel,formatting_info=True)
        # wb = copy(rb)
        # sheet = wb.get_sheet(0)
        # data = xlrd.open_workbook(excel)
        # table = data.sheets()[0]
        # nrows = table.nrows
        # print nrows
        # a = nrows
        # sheet.write(a,0,need)
        # os.remove(excel)
        # wb.save(excel)
        # #继续支付
        driver.refresh()
        driver.find_element_by_xpath(".//*[@id='order-brief']/div[2]/div[4]/a[1]").click()
        #选择支付宝
        now_handle = driver.current_window_handle
        driver.find_element_by_xpath(".//*[@id='pay-way']/div[2]/div[1]/i[2]/img").click()
        driver.find_element_by_xpath("html/body/div[2]/div[3]/div").click()
        sleep(1)
        #跳转到支付宝页面
        all_handles = driver.window_handles
        for handle in all_handles:
            if handle != now_handle:
                driver.switch_to.window(handle)
                driver.find_element_by_xpath(".//*[@id='J_tip_qr']/a").click()
                sleep(1)
                driver.find_element_by_xpath(".//*[@id='J_tLoginId']").send_keys("xxxxxx")#账号
                sleep(1)
                driver.find_element_by_xpath(".//*[@id='payPasswd_rsainput']").clear()
                sleep(1)
                driver.find_element_by_xpath(".//*[@id='payPasswd_rsainput']").send_keys("xxx")#支付密码
                driver.find_element_by_id("payPasswd_rsainput").send_keys(Keys.RETURN)
                sleep(10)
                driver.find_element_by_css_selector(".sixDigitPassword").send_keys("xxxxx")#支付密码
                sleep(1)
                driver.find_element_by_id("J_authSubmit").click()
                sleep(5)
                tip = driver.find_element_by_xpath("html/body/div[2]/div[2]").text
                self.assertEqual(tip,u"订单支付成功",msg="your buy is failed")
        #删除订单的接口
        urldelete = "http://api.sale.kuaiqiangche.com/order/delete"
        data = {'ordersn': need}
        req = requests.post(urldelete,params=data)
        print req.json()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
