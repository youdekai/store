from selenium import webdriver
import time

driver = webdriver.Chrome()
# 京东

# driver.get("https://www.jd.com")
#
# driver.maximize_window()
#
# driver.find_element_by_xpath("//*[@type='text']").send_keys("iphone13")
# driver.find_element_by_xpath("//*[@clstag='h|keycount|head|search_a']").click()
# time.sleep(10)
# driver.find_element_by_xpath('//*[@id="J_goodsList"]/ul/li[3]/div/div[1]/a/img').click()
#
# data = driver.window_handles
# driver.switch_to.window(data[1])
# driver.find_element_by_xpath("//*[@id='InitCartUrl']").click()
# time.sleep(5)
# driver.close()

# 苏宁易购

# driver.get("https://www.suning.com")
#
# driver.maximize_window()
#
# driver.find_element_by_xpath('//*[@id="searchKeywords"]').send_keys("iPhone 13")
# driver.find_element_by_xpath('//*[@id="searchSubmit"]').click()
#
# time.sleep(10)
# driver.find_element_by_xpath(' //*[@id="0000000000-12314319135"]/div/div/div[2]/div[2]/a').click()
# data=driver.window_handles
# driver.switch_to.window(data[1])
# driver.find_element_by_xpath(' //*[@id="addCart"]').click()
# time.sleep(5)
# driver.find_element_by_xpath(' /html/body/div[38]/div/div[2]/div/div[1]/a').click()
# time.sleep(10)
# driver.find_element_by_xpath(' //*[@id="cart-wrapper"]/div[3]/div/div/div[2]/div[2]/a').click()
# time.sleep(5)
# driver.find_element_by_xpath(' //*[@id="cart-wrapper"]/div[3]/div/div/div[2]/div[2]/a').click()
# driver.close()

# 哔哩哔哩

driver.get("https://www.bilibili.com/")

driver.maximize_window()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="internationalHeader"]/div[1]/div/div[3]/div[2]/span[1]/div/span/div').click()
data = driver.window_handles
driver.switch_to.window(data[1])
driver.find_element_by_xpath(' //*[@id="login-username"]').send_keys("13836774810")
time.sleep(2)
driver.find_element_by_xpath('//*[@id="login-passwd"]').send_keys('yangxue20001023')
driver.find_element_by_xpath(' //*[@id="geetest-wrap"]/div/div[5]/a[1]').click()
time.sleep(40)
driver.find_element_by_xpath(' //*[@id="nav_searchform"]/input').send_keys("鬼畜视频")
driver.find_element_by_xpath('//*[@id="nav_searchform"]/div').click()
time.sleep(15)
data1 = driver.window_handles
driver.switch_to.window(data1[2])
driver.find_element_by_xpath('//*[@id="all-list"]/div[1]/div[2]/ul/li[1]/div/div[1]/a').click()
time.sleep(10)
data2 = driver.window_handles
driver.switch_to.window(data2[3])
driver.close()
