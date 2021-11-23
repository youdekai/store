from selenium import webdriver
from selenium.webdriver.support.ui import Select
from unittest import TestCase
import time

class EnrollTest(TestCase):
    def testenrollSuccess(self):
        driver=webdriver.Chrome()

        driver.get("http://localhost:8080/HKR/")
        driver.maximize_window()
        expect="注册成功!请返回登录!"

        time.sleep(2)
        driver.find_element_by_link_text("新来的童鞋来这里注册一下哦").click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="loginname"]').send_keys("yxl")
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="msform"]/fieldset[1]/input[2]').send_keys("杨雪")
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="pwd"]').send_keys("12345678")
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="msform"]/fieldset[1]/input[4]').send_keys("12345678")
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="msform"]/fieldset[1]/input[5]').click()
        time.sleep(3)
        driver.find_element_by_xpath(' //*[@id="valid_age"]').send_keys("22")
        time.sleep(2)
        ele=driver.find_element_by_xpath('//*[@id="msform"]/fieldset[2]/select[1]')
        s=Select(ele)
        s.select_by_index(1)
        time.sleep(2)
        ele1=driver.find_element_by_xpath(' //*[@id="classname"]')
        s1=Select(ele1)
        s1.select_by_index(2)
        time.sleep(2)
        driver.find_element_by_xpath(' //*[@id="msform"]/fieldset[2]/input[3]').click()
        time.sleep(3)
        driver.find_element_by_xpath(' //*[@id="reg_mail"]').send_keys("6804887693@qq.com")
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="reg_phone"]').send_keys("13758996300")
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="msform"]/fieldset[3]/textarea').send_keys("北京市昌平区沙河镇沙阳路")
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="btn_reg"]').click()
        time.sleep(5)

        result=driver.find_element_by_link_text("注册成功!请返回登录!").text
        driver.quit()
        self.assertEqual(result,expect)
