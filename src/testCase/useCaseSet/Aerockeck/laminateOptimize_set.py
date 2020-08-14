# 铺层库优化工作栏

import unittest
from assertpy import assert_that
from BeautifulReport import BeautifulReport
from src.testCase.testCaseStep.Aerocheck.laminateOptimize_step import execute_step
from ddt import ddt,data
from src.utils.commonality.ExcelFile import read_excel

@ddt
class Test_UseCaseSet(unittest.TestCase):
    """测试类"""





    def setUp(self):
        # open_module().menu_laminateOptimize("铺层信息->铺层库优化")
        print("测试开始")


    def tearDown(self):
        """
        :return:
        """
        print("测试结束")


    site = {"详细地址": "src\\testCase\\useCase_file\\Aerocheck\\铺层库优化工具.xlsx",
            "表单名称": "最小铺层数", "初始行": 1}
    ar_testdicts = read_excel(site).readExcel_testCase()
    @data(*ar_testdicts)
    def test_1tearDown(self,testdicts):
        """
        文本框参数testdicts
        """
        expect_result=testdicts["预期结果提示信息"]  # 取出预期值
        actual_result=execute_step().textbox(testdicts)  #调用测试步骤
        # 断言测试结果
        print("预期结果：",expect_result)
        print("实际结果:",actual_result)
        assert_that(expect_result).is_equal_to(actual_result)
        












if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test_UseCaseSet))
    # 测试报告参数
    logPath = "F://Aerobook//report//Aerocheck//laminateOptimize_testReport" # 测试报告保存地址
    result = BeautifulReport(suite).report(filename="铺层库优化测试报告",log_path=logPath,description="expect_result")
