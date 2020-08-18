# 铺层库优化工作栏

import unittest,time
from assertpy import assert_that
from BeautifulReport import BeautifulReport
from src.testCase.testCaseStep.Aerocheck.laminateOptimize_step import LaminateOptimize_execute,Laminatedata_execute
from ddt import ddt,data
from src.utils.commonality.ExcelFile import read_excel
from config.relative_location import  path
from src.utils.otherMethods.DataFormatConversion import FormatConversion
from src.utils.otherMethods.Initialize import programInitialization





@ddt
@unittest.skip(u"无条件跳过此用例")
class Test_LaminateOptimize(unittest.TestCase):
    """铺层库优化工作栏测试用例"""



    def setUp(self):
        print("测试开始")


    def tearDown(self):
        print("测试结束")





    # # 测试用例Excel文件的相关信息
    # site1 = [{"详细地址": "src\\testCase\\useCase_file\\Aerocheck\\铺层库优化工具.xlsx", "表单名称": "最大铺层数", "初始行": 1},
    #          {"详细地址": "src\\testCase\\useCase_file\\Aerocheck\\铺层库优化工具.xlsx", "表单名称": "最小铺层数", "初始行": 1},
    #          {"详细地址": "src\\testCase\\useCase_file\\Aerocheck\\铺层库优化工具.xlsx", "表单名称": "铺层比", "初始行": 1},
    #          {"详细地址": "src\\testCase\\useCase_file\\Aerocheck\\铺层库优化工具.xlsx", "表单名称": "容差比", "初始行": 1},
    #          {"详细地址": "src\\testCase\\useCase_file\\Aerocheck\\铺层库优化工具.xlsx", "表单名称": "单层厚度", "初始行": 1},
    #          {"详细地址": "src\\testCase\\useCase_file\\Aerocheck\\铺层库优化工具.xlsx", "表单名称": "弹性模量E11(MPa)", "初始行": 1},
    #          {"详细地址": "src\\testCase\\useCase_file\\Aerocheck\\铺层库优化工具.xlsx", "表单名称": "弹性模量E22（MPa）", "初始行": 1},
    #          {"详细地址": "src\\testCase\\useCase_file\\Aerocheck\\铺层库优化工具.xlsx", "表单名称": "泊松比v12", "初始行": 1},
    #          {"详细地址": "src\\testCase\\useCase_file\\Aerocheck\\铺层库优化工具.xlsx", "表单名称": "剪切模量G12（MPa）", "初始行": 1},
    #          {"详细地址": "src\\testCase\\useCase_file\\Aerocheck\\铺层库优化工具.xlsx", "表单名称": "层合板长度a(mm)", "初始行": 1},
    #          {"详细地址": "src\\testCase\\useCase_file\\Aerocheck\\铺层库优化工具.xlsx", "表单名称": "层合板宽度b(mm)", "初始行": 1},
    #          {"详细地址": "src\\testCase\\useCase_file\\Aerocheck\\铺层库优化工具.xlsx", "表单名称": "Mat8材料ID", "初始行": 1},
    #          {"详细地址": "src\\testCase\\useCase_file\\Aerocheck\\铺层库优化工具.xlsx", "表单名称": "数据库名称", "初始行": 1},
    #          {"详细地址": "src\\testCase\\useCase_file\\Aerocheck\\铺层库优化工具.xlsx", "表单名称": "路径文本框", "初始行": 1},
    #          {"详细地址": "src\\testCase\\useCase_file\\Aerocheck\\铺层库优化工具.xlsx", "表单名称": "Mat8材料ID", "初始行": 1},
    #          {"详细地址": "src\\testCase\\useCase_file\\Aerocheck\\铺层库优化工具.xlsx", "表单名称": "保存为铺层数据库和保存为Excel勾选框", "初始行": 1}
    #          ]
    # list_dicts=[]
    # for site in site1:
    #     dicts1 = read_excel(site).readExcel_testCase()  # 读取测试用例
    #     ar_testdicts=FormatConversion().RemoveSubscript(dicts1)
    #     list_dicts=list_dicts+ar_testdicts
    # @data(*list_dicts)    # 参数化参数用例
    def test_1(self,testdicts):
        """铺层库优化工作栏，最大铺层数文本框测试用例"""
        expect_result=testdicts["预期结果提示信息"]  # 取出预期值
        actual_result=LaminateOptimize_execute().textbox(testdicts)  #调用测试步骤
        # 断言测试结果
        assert_that(expect_result).is_equal_to(actual_result)




@ddt
class Test_Laminatedata(unittest.TestCase):
        """铺层数据库制作"""
        global number
        number = 1


        def setUp(self):
            """用例执行前的初始化
               1、首先把需要的文件和模型复制一份出来
            """
            global number
            if number == 1:
                programInitialization().delFile()
                programInitialization().copyFile()


        def tearDown(self):
            """用例执行完后收尾
                           1、首先把复制的文件夹删除
            """
            global number
            number=number+1
            print("测试结束")



        # 测试用例Excel文件的相关信息
        site1 = [{"详细地址": "src\\testCase\\useCase_file\\Aerocheck\\铺层库制作工具弹窗.xlsx", "表单名称": "测试", "初始行": 1}]
        list_dicts = []
        if len(site1)>0:
            for site in site1:
                dicts1 = read_excel(site).readExcel_testCase()  # 读取测试用例
                ar_testdicts = FormatConversion().RemoveSubscript(dicts1)
                list_dicts = list_dicts + ar_testdicts
        else:
            list_dicts=site1
        @data(*list_dicts)  # 参数化参数用例
        def test_1(self, testdicts):
            """铺层数据库制作工具弹框"""
            expect_result = testdicts["预期结果提示信息"]  # 取出预期值
            actual_result = Laminatedata_execute().SelectFile(testdicts)  # 调用测试步骤
            # 断言测试结果
            assert_that(expect_result).is_equal_to(actual_result)







if __name__ == '__main__':
    suite = unittest.TestSuite()
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test_LaminateOptimize))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test_Laminatedata))
    file_name=time.strftime("%Y%m%d%H%M%S")+"铺层库优化测试报告"    # 测试报告名称
    relativeAddress = path.location()
    logPath = relativeAddress+"report//Aerocheck//laminateOptimize_testReport//" # 测试报告保存地址
    result = BeautifulReport(suite).report(filename=file_name,log_path=logPath,description="铺层库优化工作栏")
