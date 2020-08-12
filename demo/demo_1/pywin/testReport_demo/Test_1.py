import unittest,time,os
from selenium import webdriver
from BeautifulReport import BeautifulReport
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
class test1(unittest.TestCase):
    def save_img(self, img_name):  #错误截图方法，这个必须先定义好
        """
            传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
        """
        self.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(r"G:\student_project\Hao\img"), img_name))    #os.path.abspath(r"G:\Test_Project\img")截图存放路径
    def setUp(self):
        print("开始测试")
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.baidu.com/")
    def tearDown(self):
        print("结束测试")
        self.driver.close()

    @BeautifulReport.add_test_img('test_case_1')     #装饰器，当你没有报错也要截图的话，那么你需要在用例里面调用save_img()方法
    def test_case_1(self):   #用例没有错截图示例
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,"//div[@id='u1']/a[@name='tj_settingicon' and @class='pf']")))
        ele=self.driver.find_element_by_xpath("//div[@id='u1']/a[@name='tj_settingicon' and @class='pf']")
        ActionChains(self.driver).move_to_element(ele).perform()
        self.driver.find_element_by_xpath('//a[@class="setpref"]').click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//a[text()="保存设置"]')))
        text_data=self.driver.find_element_by_xpath('//a[text()="保存设置"]').text
        self.save_img("test_case_1")   #没有报错也要截图的话，直接在这里调用方法就行了
        self.assertEqual("保存设置",text_data)
    @BeautifulReport.add_test_img('test_case_2')     #装饰器，当你用例错误了，那么会自动调用save_img截图方法，存到指定目录下
    def test_case_2(self):   #用例错误截图示例
        time.sleep(1)
        text_data = self.driver.find_element_by_xpath('//div[@id="u1"]/a').text
        self.assertEqual("新闻1", text_data)