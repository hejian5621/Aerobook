# 铺层数据库制作
# 尺寸信息--1D2D尺寸定义

from  BeautifulReport import BeautifulReport

from config.relative_location import  path
from demo.testReport_screenshot.testReport_screenshot1 import save


# 铺层库优化工作栏
from ddt import ddt,data
import unittest
import os,shutil,win32con,time,os,sys




list1=[]

# 获取用例
useCase1=[{"测试点":"1","所测模块":"2","c":"3"}]
useCase2=[{"测试点":"7","所测模块":"8","c":"9"},{"测试点":"10","所测模块":"11","c":"12"}]
# useCase3=[{"测试点":"13","所测模块":"14","c":"15"},{"测试点":"16","所测模块":"17","c":"18"}]


list_dict_site = useCase1+useCase2

# 取出每个用例的测试点

for dict_site in list_dict_site:
    dict={}
    dict["测试点"]=dict_site["测试点"]
    list1.append(dict)




@ddt
class Test_test(unittest.TestCase):
        """铺层数据库制作"""

        global list_dicts
        global number
        global number11
        number = 0
        number11=None

        def __init__(self,*args):
            unittest.TestCase.__init__(self, *args)
            global  number
            global global_UseCase_Name
            global_UseCase_Name=None


        def save_img(self, img_name):  # 错误截图方法，这个必须先定义好
            """
                传入一个img_name, 并存储到默认的文件路径下
            :param img_name:
            :return:
            """
            pass



        def setUp(self):
            """用例执行前的初始化
               1、首先把需要的文件和模型复制一份出来
            """
            global  number ;global  global_UseCase_Name
            global number11
            # 取出测试模块
            # dict_site=list_dict_site [number]
            number11 = "tearDown" + str(number)
            print("测试开始")


        # @BeautifulReport.add_test_img(str(number1))
        @BeautifulReport.add_test_img(number11)
        def tearDown(self):
            """用例执行完后收尾
                           1、首先把复制的文件夹删除
            """
            global number11
            global number
            print("调用")

            Test_test().save_img(number11)
            self.assertEqual("保存设置", "保存设")
            # 截图需用到的装饰器，在用例里面调用前面定义的save_img方法
            print("测试结束")




        @data(*list1)  # 参数化参数用例

        def test_case_1(self,s):  # 用例错误截图示例
            time.sleep(1)
            print("s:", s)







        # @data(*list1 )  # 参数化参数用例
        # def test_1(self,list2):
        #     global number
        #     print(list2["测试点"])
        #     time.sleep(2)








if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test_test))
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test_test111))
    file_name=time.strftime("%Y%m%d%H%M%S")+"铺层库优化测试报告"    # 测试报告名称
    relativeAddress = path.location()
    logPath = relativeAddress+"report//Aerocheck//" # 测试报告保存地址
    result = BeautifulReport(suite).report(filename=file_name,log_path=logPath,description="铺层库优化工作栏")

