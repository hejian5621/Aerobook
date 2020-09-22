# 铺层库优化工作栏

import unittest, time
from assertpy import assert_that
from GenerateTestReports import BeautifulReport
from src.testCase.b_testCaseStep.Aerocheck.TestCaseStep import execute_step
from ddt import ddt, data
from src.utils.commonality.ExcelFile import read_excel
from config.relative_location import path
from src.utils.otherMethods.dataFormatConversion import FormatConversion
import pytest


@ddt
@unittest.skip(u"无条件跳过此用例")
class Test_LaminateOptimize(unittest.TestCase):
    """铺层库优化工作栏测试用例"""

    def setUp(self):
        print("测试开始")

    def tearDown(self):
        print("测试结束")



    def test_1(self):
        """铺层库优化工作栏，最大铺层数文本框测试用例"""
        expect_result=1
        actual_result=2
        # 断言测试结果
        assert_that(expect_result).is_equal_to(actual_result)

    def test_2(self):
        """铺层库优化工作栏，最大铺层数文本框测试用例"""
        expect_result=2
        actual_result=2
        # 断言测试结果
        assert_that(expect_result).is_equal_to(actual_result)


@ddt
class Test_Laminatedata(unittest.TestCase):

    def setUp(self):
        print("测试开始")

    def tearDown(self):
        print("测试结束")

    def test_1(self):
        """铺层库优化工作栏，最大铺层数文本框测试用例"""
        expect_result = 1
        actual_result = 2
        # 断言测试结果
        assert_that(expect_result).is_equal_to(actual_result)

    def test_2(self):
        """铺层库优化工作栏，最大铺层数文本框测试用例"""
        expect_result = 2
        actual_result = 2
        # 断言测试结果
        assert_that(expect_result).is_equal_to(actual_result)




if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test_LaminateOptimize))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test_Laminatedata))
    file_name = time.strftime("%Y%m%d%H%M%S") + "铺层库优化测试报告"  # 测试报告名称
    relativeAddress = path.location()
    logPath = relativeAddress + "report//Aerocheck//laminateOptimize_testReport//"  # 测试报告保存地址
    result = BeautifulReport(suite).report(filename=file_name, log_path=logPath, description="铺层库优化工作栏")
