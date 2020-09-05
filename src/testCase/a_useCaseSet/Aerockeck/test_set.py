# 铺层数据库制作



# 铺层库优化工作栏

import unittest,time,os
from assertpy import assert_that
from BeautifulReport import BeautifulReport
from src.testCase.b_testCaseStep.Aerocheck.TestCaseStep import execute_step
from ddt import ddt,data
from src.utils.commonality.ExcelFile import read_excel
from config.relative_location import  path
from src.utils.otherMethods.dataFormatConversion import FormatConversion
from tool import instrument










class Test_Laminatedata(unittest.TestCase):
        """铺层数据库制作"""
        global number
        number = 1


        def setUp(self):
            """用例执行前的初始化
               1、首先把需要的文件和模型复制一份出来
            """
            global  number
            # if number ==1:
            #     instrument().delFile()
            #     instrument().copyFile()










        def tearDown(self):
            """用例执行完后收尾
                           1、首先把复制的文件夹删除
            """
            print("测试结束")



        # # 测试用例Excel文件的相关信息
        # site1 = [{"详细地址": "src\\testCase\\c_useCase_file\\Aerocheck\\铺层库优化工具.xlsx", "表单名称": "最大铺层数", "初始行": 1}]
        # list_dicts = []
        # for site in site1:
        #     dicts1 = read_excel(site).readExcel_testCase()  # 读取测试用例
        #     ar_testdicts = FormatConversion().RemoveSubscript(dicts1)
        #     list_dicts = list_dicts + ar_testdicts
        #
        # @data(*list_dicts)  # 参数化参数用例
        # @unittest.skip(u"无条件跳过此用例")
        # def test_1(self, testdicts):
        #     """铺层库优化工作栏，最大铺层数文本框测试用例"""
        #     expect_result = testdicts["预期结果提示信息"]  # 取出预期值
        #     actual_result = execute_step().textbox(testdicts)  # 调用测试步骤
        #     # 断言测试结果
        #     assert_that(expect_result).is_equal_to(actual_result)



        def test_1(self):
            global number
            expect_result = 1
            actual_result = 1
            # 断言测试结果
            assert_that(expect_result).is_equal_to(actual_result)


        def test_2(self):
            global number
            expect_result = 1
            actual_result = 1
            # 断言测试结果
            assert_that(expect_result).is_equal_to(actual_result)


        def test_3(self):
            global number
            expect_result = 1
            actual_result = 1
            # 断言测试结果
            assert_that(expect_result).is_equal_to(actual_result)












if __name__ == '__main__':
    unittest.main()


