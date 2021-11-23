from selenium import webdriver
from selenium.webdriver.support.ui import Select
from unittest import TestCase
import time


class HKRTEST(TestCase):

    def testlogSuccess(self):
        driver = webdriver.Chrome()

        driver.get("http://localhost:8080/HKR/")
        driver.maximize_window()
        expect="查询完成!"

        driver.find_element_by_link_text("教师登录").click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="loginname"]').send_keys("jason")
        driver.find_element_by_xpath('//*[@id="password"]').send_keys("admin")
        driver.find_element_by_xpath('//*[@id="submit"]').click()
        time.sleep(5)
        driver.find_element_by_link_text("历史操作日志").click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="J-history"]').click()
        time.sleep(4)
        driver.find_element_by_xpath('//*[@id="laydate_today"]').click()
        time.sleep(2)
        driver.find_element_by_xpath(' //*[@id="history"]/div/div/div[1]/table/tbody/tr/td[2]/a/span/span[1]').click()
        time.sleep(10)
        driver.find_element_by_xpath(' //*[@id="history"]/div/div/div[1]/table/tbody/tr/td[4]/a/span/span[1]').click()
        time.sleep(10)
        ele = driver.find_element_by_xpath(' //*[@id="history"]/div/div/div[3]/table/tbody/tr/td[1]/select')
        s = Select(ele)
        s.select_by_index(1)
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="history"]/div/div/div[3]/table/tbody/tr/td[10]/a/span/span[2]').click()
        time.sleep(5)

        title=driver.title

        if title !=expect:
            driver.save_screenshot("select.jpg")

        driver.quit()

        self.assertEqual(title,expect)



