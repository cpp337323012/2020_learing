# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import unittest
from selenium.webdriver.chrome.options import Options


class Baidu(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass
        # cls.driver = webdriver.Firefox()
        # cls.driver.implicitly_wait(30)
        # cls.base_url = "http://www.baidu.com"
        # cls.verificationErrors = []
        # cls.accept_next_alter = True
        # cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        # cls.driver.quit()
        pass

    def add_img(self):
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def setUp(self):
        self.imgs = []
        self.addCleanup(self.cleanup)
        # self.driver = webdriver.Chrome()  # 不开启静默模式
        chrome_options = Options()
        chrome_options.add_argument('--headless')  # 无界面
        chrome_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在报错问题
        chrome_options.add_argument('--disable-gpu')   # 禁用GPU硬件加速。如果软件渲染器没有就位，则GPU进程将不会启动。chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--window-size=1920,1080')  # 设置当前窗口的宽度和高度
        self.driver = webdriver.Chrome('chromedriver', options=chrome_options)
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com"
        self.verificationErrors = []
        self.accept_next_alter = True
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def cleanup(self):
        pass

    # 百度设置用例
    # @unittest.skip('暂时不执行')
    def test02_baidu_set(self):
        u"""设置页面搜索结果为50条"""
        driver = self.driver
        # 进入搜索设置页
        driver.get(self.base_url+"/")
        self.add_img()
        time.sleep(4)
        sup = driver.find_element_by_link_text("设置")
        ActionChains(driver).move_to_element(sup).perform()
        self.add_img()
        driver.find_element_by_class_name("setpref").click()
        self.add_img()

        # 设置每页搜索结果为50条
        m = driver.find_element_by_id("nr")
        m.find_element_by_xpath("//option[@value='50']").click()
        time.sleep(2)
        self.add_img()

        # 保存设置信息
        driver.find_element_by_class_name("prefpanelgo").click()
        time.sleep(3)
        a = driver.switch_to.alert.text
        if a == '已经记录下您的使用偏好':
            pass
        else:
            print('未找到提示框【已经记录下您的使用偏好】')
            return False
        time.sleep(2)
        # driver.switch_to_alert.accept()
        driver.switch_to.alert.accept()
        # driver.switch_to_alert.accept()
        time.sleep(1)
        self.add_img()

    # 百度搜索用例
    # @unittest.skip('暂时不执行')
    def test01_baidu_search(self):
        u"""百度搜索"""
        driver = self.driver
        driver.get(self.base_url+"/")
        self.add_img()
        driver.find_element_by_id("kw").send_keys("selenium webdriver")
        self.add_img()
        driver.find_element_by_id("su").click()
        time.sleep(2)
        self.add_img()

    # 搜索恢复默认设置
    # @unittest.skip('暂时不执行')
    def test03_baidu_reset(self):
        u"""恢复默认设置"""
        driver = self.driver
        driver.get(self.base_url+"/")
        time.sleep(2)
        self.add_img()
        elem = driver.find_element_by_id('u1')
        move = elem.find_element_by_class_name('pf')
        # move = driver.find_element_by_class_name("setpref")
        # move = driver.find_element_by_xpath("/html/body/div[1]/div[6]/a[1]")
        # driver.execute_script('$(arguments[0]).click()',move)
        ActionChains(driver).move_to_element(move).perform()
        self.add_img()
        driver.find_element_by_class_name("setpref").click()
        self.add_img()
        driver.find_element_by_class_name("prefpanelrestore").click()
        time.sleep(3)
        # self.add_img()
        a = driver.switch_to.alert.text
        if a == '已经恢复默认设置':
            pass
        else:
            print('未找到提示框【已经恢复默认设置】')
            return False
        time.sleep(2)
        driver.switch_to.alert.accept()
        self.add_img()


if __name__ == "__main__":
    unittest.main()