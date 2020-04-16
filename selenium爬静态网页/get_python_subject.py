# coding:utf-8

from selenium import webdriver

driver = webdriver.Chrome(r'E:\webdriver\chromedriver.exe')
url= 'https://www.cnblogs.com/wupeiqi/p/9078770.html'
# url = 'https://www.baidu.com'
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(2)


part_ones = driver.find_elements_by_xpath('//*[@id="cnblogs_post_body"]/ol[1]/li')
for part_one in part_ones:
     print(part_one.text())

driver.quit()
