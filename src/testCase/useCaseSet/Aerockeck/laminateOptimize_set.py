# 铺层库优化工作栏

import unittest,time
from assertpy import assert_that
from BeautifulReport import BeautifulReport
from src.testCase.testCaseStep.Aerocheck.laminateOptimize_step import LaminateOptimize_execute,Laminatedata_execute
from ddt import ddt,data
from src.utils.commonality.ExcelFile import read_excel
from config.relative_location import  path
from src.utils.otherMethods.dataFormatConversion import FormatConversion
from src.utils.commonality.tool import instrument





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
            global number;  global source;global source1;global dlg_windows
            dlg_windows=None
            if number == 1:
                instrument().delFile()
                # 复制模板文件，并返回复制的地址
                source=instrument().copyFile()
                number =number+1

        def tearDown(self):
            """用例执行完后收尾
                           1、首先把复制的文件夹删除
            """
            global dlg_windows
            # 判断选择铺层Excel文件文本框控件是否存在，如果存在向该文本框输入数据
            parWin_Dicti={"窗口标题":"铺层数据库制作工具","关闭窗口控件名称":"关闭","关闭窗口控件操作方法":"click"}
            edit_box1 = instrument().popUp_Whether_close(parWin_Dicti)
            print("测试结束")



        # 测试用例Excel文件的相关信息
        site1 = [{"详细地址": "src\\testCase\\useCase_file\\Aerocheck\\铺层库制作工具弹窗.xlsx", "表单名称": "铺层库制作弹窗", "初始行": 1},
                 {"详细地址": "src\\testCase\\useCase_file\\Aerocheck\\铺层库制作工具弹窗.xlsx", "表单名称": "选择铺层Excel文件", "初始行": 1},
                 {"详细地址": "src\\testCase\\useCase_file\\Aerocheck\\铺层库制作工具弹窗.xlsx", "表单名称": "铺层数据保存路径文本框", "初始行": 1}]
        # site1 =[{"详细地址": "src\\testCase\\useCase_file\\Aerocheck\\铺层库制作工具弹窗.xlsx", "表单名称": "测试", "初始行": 1}]
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
            global source; global dlg_windows
            UseCaseNumber=testdicts["用例编号"]
            print("开始执行用例：",UseCaseNumber)
            testdicts["被测程序文件地址"]=source
            expect1_binrowseButton = testdicts["选择铺层Excel文件浏览按钮对应文本框预期"]
            expect2_binrowseButton = testdicts["铺层数据保存路径浏览对应文本框预期"]
            expect3_result = testdicts["预期结果提示信息"]  # 取出预期值
            actual_result,actual_editlist,dlg_windows = Laminatedata_execute().SelectFile(testdicts)  # 调用测试步骤
            # 断言测试结果
            # 点击浏览按钮，并且选择路径或者文件后的预期跟实际比较
            if expect1_binrowseButton=="默认" and expect2_binrowseButton=="默认":
                actual1, actual2, expect1, expect2 = FormatConversion().SelectFile(testdicts,actual_editlist,source)
                assert_that(expect1).is_equal_to(actual1)
                assert_that(actual2).is_equal_to(expect2)
            # 去掉实际值跟预期值，前后的空格
            atLast_expect3_result= expect3_result.strip()
            atLast_actual_result = actual_result.strip()
            # 最后的测试结果
            assert_that(atLast_expect3_result).is_equal_to(atLast_actual_result)







if __name__ == '__main__':
    suite = unittest.TestSuite()
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test_LaminateOptimize))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test_Laminatedata))
    file_name=time.strftime("%Y%m%d%H%M%S")+"铺层库优化测试报告"    # 测试报告名称
    relativeAddress = path.location()
    logPath = relativeAddress+"report//Aerocheck//laminateOptimize_testReport//" # 测试报告保存地址
    result = BeautifulReport(suite).report(filename=file_name,log_path=logPath,description="铺层库优化工作栏")
