# 铺层库优化工作栏

import unittest
from assertpy import assert_that
import time, os
from BeautifulReport import BeautifulReport
from parameterized.parameterized import parameterized
from src.utils.otherMethods.dataFormatConversion import FormatConversion
from src.testCase.b_testCaseStep.Aerocheck.TestCaseStep import execute_step
from ddt import ddt, data, unpack, file_data
import numpy as np


@ddt
class Test_UseCaseSet(unittest.TestCase):
    """测试类"""

    # # 测试数据参数化
    # tableName = "铺层库优化工具.xlsx"  # Excel表格名称
    # frmName = "最大铺层数"  # 表单名称
    # site = "src\\testCase\\c_useCase_file\\Aerocheck\\"
    # detailedAddress = site + tableName  # 测试用例详细的地址





    def setUp(self):
        # open_module().menu_laminateOptimize("铺层信息->铺层库优化")
        print("测试开始")

        # ar_testdicts = {'用例编号': 'pckyh001',
        #                 'title': '1、最大铺层数文本框中输入为空；\n2、其余文本框都正常输入；\n3、“保存为铺层数据库”和“保存为Excel文件”单选框都勾选。',
        #                 '所在模块': '铺层信息->铺层库优化', '最大铺层数': '', '最小铺层数': '默认', '铺层比一': '默认', '铺层比二': '默认',
        #                 '铺层比三': '默认', '容差比': '默认', '单层厚度': '默认', '弹性模量E11': '默认', '弹性模量E22': '默认', '泊松比v12': '默认',
        #                 '剪切模量G12': '默认', '层合板长度': '默认', '层合板宽度': '默认', 'Mat8材料ID': '1', '数据库名称': '默认',
        #                 '保存为铺层数据库': '1', '保存为Excel文件': '1', '路径': "C:\\Users\Administrator\Desktop\aro\aro2",
        #                 '求解': '点击', "关闭": '默认', '预期': '最大铺层数文本框输入不能为空！', "预期结果行数": "1", "预期结果提示信息": "铺层库自动生成中",
        #                 "求解等待时间": "3"}



    def tearDown(self):
        """
        :return:
        """
        print("测试结束")

    # ar_testdicts = FormatConversion().ParameterizedFormat(detailedAddress, frmName)  # 获取测试用例
    # ar_testdicts = {'用例编号': 'pckyh001', 'title': '1、最大铺层数文本框中输入为空；\n2、其余文本框都正常输入；\n3、“保存为铺层数据库”和“保存为Excel文件”单选框都勾选。',
    #                   '所在模块': '铺层信息->铺层库优化', '最大铺层数': '', '最小铺层数': '默认', '铺层比一': '默认', '铺层比二': '默认',
    #                   '铺层比三': '默认', '容差比': '默认', '单层厚度': '默认', '弹性模量E11': '默认', '弹性模量E22': '默认', '泊松比v12': '默认',
    #                   '剪切模量G12': '默认', '层合板长度': '默认', '层合板宽度': '默认', 'Mat8材料ID': '1', '数据库名称': '默认',
    #                   '保存为铺层数据库': '1', '保存为Excel文件': '1', '路径': "C:\\Users\Administrator\Desktop\aro\aro2",
    #                   '求解': '点击', "关闭": '默认', '预期': '最大铺层数文本框输入不能为空！', "预期结果行数": "1", "预期结果提示信息": "铺层库自动生成中",
    #                   "求解等待时间": "3"}

    ar_testdicts=[{"测试点":"2"},{"测试点":"3"}]


    # @data({'title':"1"},{"title":"2"})
    @data(*ar_testdicts)
    def test_1tearDown(self, testdicts):
        """
        文本框参数
        """
        print("testdicts12:",testdicts)
        # assert_that(5).is_equal_to(6)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test_UseCaseSet))
    # 测试报告参数
    logPath = "F://Aerobook//report//Aerocheck//laminateOptimize_testReport"  # 测试报告保存地址
    result = BeautifulReport(suite).report(filename="铺层库优化测试报告", log_path=logPath, description="expect_result")
