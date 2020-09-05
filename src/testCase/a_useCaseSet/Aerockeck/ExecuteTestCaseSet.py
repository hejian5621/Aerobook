# 铺层库优化工作栏

import unittest,time
from assertpy import assert_that
from BeautifulReport import BeautifulReport
from src.testCase.b_testCaseStep.Aerocheck.TestCaseStep import LaminateOptimize_execute,\
    Laminatedata_execute,sizeInfo_1DXls_execute,solveCalculation_execute,editWorkingCondition_execute,\
    compositeMaterial,CompoundStrengthCheck,loaddatabase_popUp_execute
from ddt import ddt,data
from src.utils.commonality.ExcelFile import read_excel
from config.relative_location import  path
from src.utils.otherMethods.dataFormatConversion import FormatConversion
from tool import instrument,folderFile_dispose,Check_winControl
from src.utils.otherMethods.actual import Information_Win
from src.utils.otherMethods.initialize import execute_useCase_initialize


"""铺层信息--铺层库优化工作栏测试用例"""
@ddt
@unittest.skip(u"无条件跳过此用例")
class Test_LaminateOptimize(unittest.TestCase):
    """铺层库优化工作栏测试用例"""



    def setUp(self):
        print("测试开始")


    def tearDown(self):
        print("测试结束")





    # 测试用例Excel文件的相关信息
    site1 = [{"详细地址": r"src\testCase\c_useCase_file\Aerocheck\铺层信息\铺层库优化工具.xlsx", "表单名称": "最大铺层数", "初始行": 1},
             {"详细地址": r"src\testCase\c_useCase_file\Aerocheck\铺层信息\铺层库优化工具.xlsx", "表单名称": "最小铺层数", "初始行": 1},
             {"详细地址": r"src\testCase\c_useCase_file\Aerocheck\铺层信息\铺层库优化工具.xlsx", "表单名称": "铺层比", "初始行": 1},
             {"详细地址": r"src\testCase\c_useCase_file\Aerocheck\铺层信息\铺层库优化工具.xlsx", "表单名称": "容差比", "初始行": 1},
             {"详细地址": r"src\testCase\c_useCase_file\Aerocheck\铺层信息\铺层库优化工具.xlsx", "表单名称": "单层厚度", "初始行": 1},
             {"详细地址": r"src\testCase\c_useCase_file\Aerocheck\铺层信息\铺层库优化工具.xlsx", "表单名称": "弹性模量E11(MPa)", "初始行": 1},
             {"详细地址": r"src\testCase\c_useCase_file\Aerocheck\铺层信息\铺层库优化工具.xlsx", "表单名称": "弹性模量E22（MPa）", "初始行": 1},
             {"详细地址": r"src\testCase\c_useCase_file\Aerocheck\铺层信息\铺层库优化工具.xlsx", "表单名称": "泊松比v12", "初始行": 1},
             {"详细地址": r"src\testCase\c_useCase_file\Aerocheck\铺层信息\铺层库优化工具.xlsx", "表单名称": "剪切模量G12（MPa）", "初始行": 1},
             {"详细地址": r"src\testCase\c_useCase_file\Aerocheck\铺层信息\铺层库优化工具.xlsx", "表单名称": "层合板长度a(mm)", "初始行": 1},
             {"详细地址": r"src\testCase\c_useCase_file\Aerocheck\铺层信息\铺层库优化工具.xlsx", "表单名称": "层合板宽度b(mm)", "初始行": 1},
             {"详细地址": r"src\testCase\c_useCase_file\Aerocheck\铺层信息\铺层库优化工具.xlsx", "表单名称": "Mat8材料ID", "初始行": 1},
             {"详细地址": r"src\testCase\c_useCase_file\Aerocheck\铺层信息\铺层库优化工具.xlsx", "表单名称": "数据库名称", "初始行": 1},
             {"详细地址": r"src\testCase\c_useCase_file\Aerocheck\铺层信息\铺层库优化工具.xlsx", "表单名称": "路径文本框", "初始行": 1},
             {"详细地址": r"src\testCase\c_useCase_file\Aerocheck\铺层信息\铺层库优化工具.xlsx", "表单名称": "Mat8材料ID", "初始行": 1},
             {"详细地址": r"src\testCase\c_useCase_file\Aerocheck\铺层信息\铺层库优化工具.xlsx", "表单名称": "保存为铺层数据库和保存为Excel勾选框", "初始行": 1}
             ]
    list_dicts=[]
    for site in site1:
        dicts1 = read_excel(site).readExcel_testCase()  # 读取测试用例
        ar_testdicts=FormatConversion().RemoveSubscript(dicts1)
        list_dicts=list_dicts+ar_testdicts
    @unittest.skip(u"无条件跳过此用例")
    @data(*list_dicts)    # 参数化参数用例
    def test_1(self,testdicts):
        """铺层库优化工作栏，最大铺层数文本框测试用例"""
        expect_result=testdicts["预期结果提示信息"]  # 取出预期值
        actual_result=LaminateOptimize_execute().textbox(testdicts)  #调用测试步骤
        # 断言测试结果
        assert_that(expect_result).is_equal_to(actual_result)


"""铺层信息--铺层数据库制作工具弹窗"""
@ddt
@unittest.skip(u"无条件跳过此用例")
class Test_Laminatedata(unittest.TestCase):
        """铺层数据库制作"""
        global number
        number = 1


        def setUp(self):
            """用例执行前的初始化
               1、首先把需要的文件和模型复制一份出来
            """
            global number;  global source;global source1
            dlg_windows=None
            print("测试开始")
            # if number == 1:
            #     instrument().delFile()
            #     # 复制模板文件，并返回复制的地址
            #     source=instrument().copyFile()
            #     number =number+1
            source=r"F:\Aerobook\src\testCase\projectFile\automateFile"

        def tearDown(self):
            """用例执行完后收尾
                           1、首先把复制的文件夹删除
            """
            # 判断选择铺层Excel文件文本框控件是否存在，如果存在向该文本框输入数据
            Check_winControl("铺层数据库制作工具","关闭").popUp_Whether_close()
            print("测试结束")



        # 测试用例Excel文件的相关信息
        site1 = [{"详细地址": r"src\testCase\c_useCase_file\Aerocheck\铺层信息\铺层库制作工具弹窗.xlsx", "表单名称": "铺层库制作弹窗", "初始行": 1},
                 {"详细地址": r"src\testCase\c_useCase_file\Aerocheck\铺层信息\铺层库制作工具弹窗.xlsx", "表单名称": "选择铺层Excel文件", "初始行": 1},
                 {"详细地址": r"src\testCase\c_useCase_file\Aerocheck\铺层信息\铺层库制作工具弹窗.xlsx", "表单名称": "铺层数据保存路径文本框", "初始行": 1}]
        # site1 =[{"详细地址": r"src\testCase\c_useCase_file\Aerocheck\铺层信息\铺层库制作工具弹窗.xlsx", "表单名称": "测试", "初始行": 1}]
        list_dicts = []
        if len(site1)>0:
            for site in site1:
                dicts1 = read_excel(site).readExcel_testCase()  # 读取测试用例
                ar_testdicts = FormatConversion().RemoveSubscript(dicts1)
                list_dicts = list_dicts + ar_testdicts
        else:
            list_dicts=site1
        @unittest.skip(u"无条件跳过此用例")
        @data(*list_dicts)  # 参数化参数用例
        def test_1(self, testdicts):
            """铺层数据库制作工具弹框"""
            global source
            UseCaseNumber=testdicts["用例编号"]
            print("开始执行用例：",UseCaseNumber)
            testdicts["被测程序文件地址"]=source
            expect1_binrowseButton = testdicts["选择铺层Excel文件浏览按钮对应文本框预期"]
            expect2_binrowseButton = testdicts["铺层数据保存路径浏览对应文本框预期"]
            expect3_result = testdicts["预期结果提示信息"]  # 取出预期值
            actual_result,actual_editlist = Laminatedata_execute(testdicts).SelectFile()  # 调用测试步骤
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


"""尺寸信息--一维单元尺寸定义（模板）"""
@ddt
@unittest.skip(u"无条件跳过此用例")
class Test_sizeInfo_1DXls(unittest.TestCase):
        """尺寸信息--一维单元尺寸定义（模板）"""

        def setUp(self):
            global source;    global old_content
            global messageType ;global actual_result
            global UseCaseNumber ;global expect3_result
            # 初始化变量
            source=None;old_content=None;messageType=None
            actual_result=None; UseCaseNumber=None ;expect3_result=None
            print("测试开始")
            source = r"F:\Aerobook\src\testCase\projectFile\automateFile"
            # 用例开始获取信息窗口对于的html里的内容
            old_content = Information_Win().acquire_HTML_TXT(source)





        def tearDown(self):
            """用例执行完后收尾"""
            global source;   global old_content
            global messageType;   global actual_result
            global UseCaseNumber;  global expect3_result
            # 断言测试结果
            # 如果是对比信息窗口里的内容，就获取最新的内容
            if messageType == "信息窗口":
                actual_result = FormatConversion().GetLatestData(actual_result, old_content)
            if type(actual_result)==list:  # 实际值如果是列表，就转化成字符串
                actual_result = ' '.join(actual_result)
            if actual_result:
                # 去掉实际值跟预期值，前后的空格
                expect3_result = expect3_result.strip()
                actual_result = actual_result.strip()
            print("实际值：", actual_result)
            print("预期值：", expect3_result)
            # 最后的测试结果
            assert_that(expect3_result).is_equal_to(actual_result)
            print("测试结束")



        # 测试用例Excel文件的相关信息
        site1 = [{"详细地址": r"src\testCase\c_useCase_file\Aerocheck\尺寸信息\一维单元尺寸定义（模板）.xlsx",
                  "表单名称": "一维单元尺寸定义复合材料（模板）", "初始行": 1},
                 {"详细地址": r"src\testCase\c_useCase_file\Aerocheck\尺寸信息\一维单元尺寸定义（模板）.xlsx",
                  "表单名称": "一维单元尺寸定义金属材料（模板）", "初始行": 1}]
        # site1 =[{"详细地址": r"src\testCase\c_useCase_file\Aerocheck\尺寸信息\一维单元尺寸定义（模板）.xlsx", "表单名称": "测试", "初始行": 1}]
        list_dicts = []
        if len(site1)>0:
            for site in site1:
                dicts1 = read_excel(site).readExcel_testCase()  # 读取测试用例
                ar_testdicts = FormatConversion().RemoveSubscript(dicts1)
                list_dicts = list_dicts + ar_testdicts
        else:
            list_dicts=site1
        @data(*list_dicts)  # 参数化参数用例
        @unittest.skip(u"无条件跳过此用例")
        def test_1(self, testdicts):
            """尺寸信息--一维单元尺寸定义（模板）"""
            global source;     global old_content
            global messageType;  global actual_result
            global UseCaseNumber;  global expect3_result
            # 获取变量信息
            messageType = testdicts["提示信息类型"]
            UseCaseNumber = testdicts["用例编号"]
            testdicts["被测程序文件地址"] = source
            expect3_result = testdicts["预期结果提示信息"]  # 取出预期值
            print("开始执行用例：", UseCaseNumber)
            actual_result= sizeInfo_1DXls_execute(testdicts).SelectFile()  # 调用测试步骤





        # 测试用例Excel文件的相关信息
        site2 = [{"详细地址": r"src\testCase\c_useCase_file\Aerocheck\尺寸信息\二维单元尺寸定义（模板）.xlsx",
                  "表单名称": "二维单元尺寸定义复合材料（模板）", "初始行": 1},
                 {"详细地址": r"src\testCase\c_useCase_file\Aerocheck\尺寸信息\二维单元尺寸定义（模板）.xlsx",
                  "表单名称": "二维单元尺寸定义金属材料（模板）", "初始行": 1}]
        # site2 =[{"详细地址": r"src\testCase\c_useCase_file\Aerocheck\尺寸信息\二维单元尺寸定义（模板）.xlsx", "表单名称": "测试", "初始行": 1}]
        list_dicts2 = []
        if len(site1)>0:
            for site in site2:
                dicts2 = read_excel(site).readExcel_testCase()  # 读取测试用例
                ar_testdicts2 = FormatConversion().RemoveSubscript(dicts2)
                list_dicts2 = list_dicts2 + ar_testdicts2
        else:
            list_dicts2=site2
        @data(*list_dicts2)  # 参数化参数用例
        @unittest.skip(u"无条件跳过此用例")
        def test_2(self, testdicts):
            """尺寸信息--二维单元尺寸定义（模板）"""
            global source;    global old_content
            global messageType;   global actual_result
            global UseCaseNumber;   global expect3_result
            UseCaseNumber = testdicts["用例编号"]
            expect3_result = testdicts["预期结果提示信息"]  # 取出预期值
            messageType = testdicts["提示信息类型"]
            testdicts["被测程序文件地址"] = source
            print("开始执行用例：", UseCaseNumber)
            actual_result = sizeInfo_1DXls_execute(testdicts).SelectFile()  # 调用测试步骤



"""求解计算--求解计算"""
@ddt
@unittest.skip(u"无条件跳过此用例")
class Test_solveCalculation(unittest.TestCase):
        """求解计算--求解计算"""

        def setUp(self):
            global source;    global old_content
            global messageType ;global actual_result
            global UseCaseNumber ;global expect3_result
            # 初始化变量
            source=None;old_content=None;messageType=None
            actual_result=None; UseCaseNumber=None ;expect3_result=None
            print("测试开始")
            source = r"F:\Aerobook\src\testCase\projectFile\automateFile"
            # 用例开始获取信息窗口对于的html里的内容
            old_content = Information_Win().acquire_HTML_TXT(source)
            list_filePath=["hwsolver.mesg","os.bat","run.vbs","update_Htail.h3d","update_Htail.html",
                           "update_Htail.mvw","update_Htail.out","update_Htail.pch","update_Htail.res",
                           "update_Htail.stat","update_Htail_frames.html","update_Htail_menu.html"]
            folderFile_dispose(source).delfile(list_filePath)
            # 用例执行之前清楚项目文件夹里的部分文件





        def tearDown(self):
            """用例执行完后收尾"""
            global source;   global old_content
            global messageType;   global actual_result
            global UseCaseNumber;  global expect3_result
            # 收尾，判断有没有弹窗没有关闭，如果有就关闭
            Check_winControl("警告", "OK").popUp_Whether_close()
            # 测试结果处理
            if messageType == "信息窗口":    # 如果是对比信息窗口里的内容，就获取最新的内容
                actual_result = FormatConversion().GetLatestData(actual_result, old_content)
            if type(actual_result)==list:  # 实际值如果是列表，就转化成字符串
                actual_result = ' '.join(actual_result)
            if actual_result:   # 当实际值不为空的情况下
                # 把实际值字符串根据换行符\n转化成列表，并去掉列表中的所有的空格
                actual_result = FormatConversion().takeOut_space(actual_result)
                expect3_result = FormatConversion().takeOut_space(expect3_result)
            print("实际值：", actual_result)
            print("预期值：", expect3_result)
            # 断言测试结果
            assert_that(expect3_result).is_equal_to(actual_result)
            print("测试结束")



        # 测试用例Excel文件的相关信息
        site1 = [{"详细地址": r"src\testCase\c_useCase_file\Aerocheck\求解计算\自动化求解计算.xlsx",
                  "表单名称": "属性更新选择路径", "初始行": 1},
                 {"详细地址": r"src\testCase\c_useCase_file\Aerocheck\求解计算\自动化求解计算.xlsx",
                  "表单名称": "载荷提取选择路径", "初始行": 1}]
        # site1 =[{"详细地址": r"src\testCase\c_useCase_file\Aerocheck\求解计算\自动化求解计算.xlsx","表单名称": "测试", "初始行": 1}]
        list_dicts = []
        if len(site1)>0:
            for site in site1:
                dicts1 = read_excel(site).readExcel_testCase()  # 读取测试用例
                ar_testdicts = FormatConversion().RemoveSubscript(dicts1)
                list_dicts = list_dicts + ar_testdicts
        else:
            list_dicts=site1
        @data(*list_dicts)  # 参数化参数用例
        @unittest.skip(u"无条件跳过此用例")
        def test_1(self, testdicts):
            """求解计算--求解计算--文本框"""
            global source;     global old_content
            global messageType;  global actual_result
            global UseCaseNumber;  global expect3_result
            # 获取变量信息
            messageType = testdicts["提示信息类型"]
            UseCaseNumber = testdicts["用例编号"]
            testdicts["被测程序文件地址"] = source
            expect3_result = testdicts["预期结果提示信息"]  # 取出预期值
            print("开始执行用例：", UseCaseNumber)
            actual_result= solveCalculation_execute(testdicts).SelectFile()  # 调用测试步骤
            #如有警告弹窗就关掉警告弹窗



"""载荷信息--载荷数据库制作工具弹窗"""
@ddt
# @unittest.skip(u"无条件跳过此用例")
class Test_loaddatabase_popUp(unittest.TestCase):
        """载荷信息--载荷数据库制作工具弹窗"""
        global number
        number = 1


        def setUp(self):
            """用例执行前的初始化
               1、首先把需要的文件和模型复制一份出来
            """
            global number;  global source;global source1
            dlg_windows=None
            print("测试开始")
            # if number == 1:
            #     instrument().delFile()
            #     # 复制模板文件，并返回复制的地址
            #     source=instrument().copyFile()
            #     number =number+1
            source=r"F:\Aerobook\src\testCase\projectFile\automateFile"

        def tearDown(self):
            """用例执行完后收尾
                           1、首先把复制的文件夹删除
            """
            # 判断选择铺层Excel文件文本框控件是否存在，如果存在向该文本框输入数据
            Check_winControl("铺层数据库制作工具", "关闭").popUp_Whether_close()
            print("测试结束")



        # 测试用例Excel文件的相关信息
        # site1 = [{"详细地址": r"src\testCase\c_useCase_file\Aerocheck\载荷信息\自动化载荷数据库制作工具弹窗.xlsx", "表单名称": "载荷数据库制作弹窗", "初始行": 1},
        #          {"详细地址": r"src\testCase\c_useCase_file\Aerocheck\载荷信息\自动化载荷数据库制作工具弹窗.xlsx", "表单名称": "选择载荷文件", "初始行": 1},
        #          {"详细地址": r"src\testCase\c_useCase_file\Aerocheck\载荷信息\自动化载荷数据库制作工具弹窗.xlsx", "表单名称": "载荷数据库保存路径", "初始行": 1}]
        site1 =[{"详细地址": r"src\testCase\c_useCase_file\Aerocheck\载荷信息\自动化载荷数据库制作工具弹窗.xlsx", "表单名称": "测试", "初始行": 1}]
        list_dicts = []
        if len(site1)>0:
            for site in site1:
                dicts1 = read_excel(site).readExcel_testCase()  # 读取测试用例
                ar_testdicts = FormatConversion().RemoveSubscript(dicts1)
                list_dicts = list_dicts + ar_testdicts
        else:
            list_dicts=site1
        # @unittest.skip(u"无条件跳过此用例")
        @data(*list_dicts)  # 参数化参数用例
        def test_1(self, testdicts):
            """载荷信息--载荷数据库制作工具弹窗"""
            global source
            UseCaseNumber=testdicts["用例编号"]
            print("开始执行用例：",UseCaseNumber)
            testdicts["被测程序文件地址"]=source
            expect1_binrowseButton = testdicts["选择铺层Excel文件浏览按钮对应文本框预期"]
            expect2_binrowseButton = testdicts["铺层数据保存路径浏览对应文本框预期"]
            expect3_result = testdicts["预期结果提示信息"]  # 取出预期值
            actual_result,actual_editlist = loaddatabase_popUp_execute(testdicts).SelectFile()  # 调用测试步骤
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




"""载荷信息--编辑工况"""
@ddt
@unittest.skip(u"无条件跳过此用例")
class Test_editWorkingCondition(unittest.TestCase):
        """载荷信息--编辑工况"""
        global number
        number = 1

        def setUp(self):
            global source;    global old_content ;global number
            global messageType ;global actual_result
            global UseCaseNumber ;global expect3_result
            # 初始化变量
            source=None;old_content=None;messageType=None
            actual_result=None; UseCaseNumber=None ;expect3_result=None
            print("测试开始")
            source = r"F:\Aerobook\src\testCase\projectFile\automateFile"
            Check_winControl("编辑工况", "关闭").popUp_Whether_close()
            if number==1:
                # 清除所有的包络工况
                execute_useCase_initialize().clear_editWorkingCondition()
            number =number+1
            Check_winControl("编辑工况", "关闭").popUp_Whether_close()






        def tearDown(self):
            """用例执行完后收尾"""
            global source;   global old_content
            global messageType;   global actual_result
            global UseCaseNumber;  global expect3_result
            # 收尾，判断有没有弹窗没有关闭，如果有就关闭
            Check_winControl("警告", "OK").popUp_Whether_close()
            Check_winControl("编辑工况", "关闭").popUp_Whether_close()
            # 处理测试结果
            if messageType == "信息窗口":    # 如果是对比信息窗口里的内容，就获取最新的内容
                actual_result = FormatConversion().GetLatestData(actual_result, old_content)
            if type(actual_result)==list:  # 实际值如果是列表，就转化成字符串
                actual_result = ' '.join(actual_result)
            if actual_result:   # 当实际值不为空的情况下
                # 把实际值字符串根据换行符\n转化成列表，并去掉列表中的所有的空格
                actual_result = FormatConversion().takeOut_space(actual_result)
                expect3_result = FormatConversion().takeOut_space(expect3_result)
            print("实际值：", actual_result)
            print("预期值：", expect3_result)
            #  # 断言测试结果
            assert_that(expect3_result).is_equal_to(actual_result)
            print("测试结束")






        # 测试用例Excel文件的相关信息

        site1 = [{"详细地址": r"src\testCase\c_useCase_file\Aerocheck\载荷信息\自动化编辑工况.xlsx",
                  "表单名称": "新建", "初始行": 1},
                 {"详细地址":  r"src\testCase\c_useCase_file\Aerocheck\载荷信息\自动化编辑工况.xlsx",
                  "表单名称": "重命名", "初始行": 1}]
        # site1 =[{"详细地址": r"src\testCase\c_useCase_file\Aerocheck\载荷信息\自动化编辑工况.xlsx","表单名称": "测试1", "初始行": 1}]

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
            """载荷信息--编辑工况"""
            global source;     global old_content
            global messageType;  global actual_result
            global UseCaseNumber;  global expect3_result
            # 获取变量信息
            messageType = testdicts["提示信息类型"]
            UseCaseNumber = testdicts["用例编号"]
            testdicts["被测程序文件地址"] = source
            expect3_result = testdicts["预期结果提示信息"]  # 取出预期值
            print("开始执行用例：", UseCaseNumber)
            actual_result= editWorkingCondition_execute(testdicts).SelectFile()  # 调用测试步骤
            print("actual_result:",actual_result)




"""材料信息--定义复合材料参数"""
@ddt
@unittest.skip(u"无条件跳过此用例")
class Test_compositeMaterial(unittest.TestCase):
        """材料信息--定义复合材料参数"""
        global number
        number = 1

        def setUp(self):
            global source;    global old_content ;global number
            global messageType ;global actual_result
            global UseCaseNumber ;global expect3_result
            from src.utils.otherMethods.initialize import module_initialize
            from tool import WindowTop
            # 被系统置顶
            WindowTop.EnumWindows("Aerobook v1.0.4")
            # 初始化变量
            source=None;old_content=None;messageType=None
            actual_result=None; UseCaseNumber=None ;expect3_result=None
            print("测试开始")
            source = r"F:\Aerobook\src\testCase\projectFile\automateFile"
            # # 如果编辑工况弹窗没有关闭，就关闭
            if number==1:
                # 清除所有的许用值曲线
                execute_useCase_initialize().clear_AllowableCurve()
            number =number+1







        def tearDown(self):
            """用例执行完后收尾"""
            global source;   global old_content
            global messageType;   global actual_result
            global UseCaseNumber;  global expect3_result
            # 被测窗口置顶
            # 收尾，判断有没有弹窗没有关闭，如果有就关闭
            Check_winControl("警告", "OK").popUp_Whether_close()
            Check_winControl("编辑工况", "关闭").popUp_Whether_close()
            # 处理测试结果
            if messageType == "信息窗口":    # 如果是对比信息窗口里的内容，就获取最新的内容
                actual_result = FormatConversion().GetLatestData(actual_result, old_content)
            if type(actual_result)==list:  # 实际值如果是列表，就转化成字符串
                actual_result = ' '.join(actual_result)
            if actual_result:   # 当实际值不为空的情况下
                # 把实际值字符串根据换行符\n转化成列表，并去掉列表中的所有的空格
                actual_result = FormatConversion().takeOut_space(actual_result)
                expect3_result = FormatConversion().takeOut_space(expect3_result)
            print("实际值：", actual_result)
            print("预期值：", expect3_result)
            #  # 断言测试结果
            assert_that(expect3_result).is_equal_to(actual_result)
            print("测试结束")



        # 测试用例Excel文件的相关信息
        site1 = [{"详细地址": r"src\testCase\c_useCase_file\Aerocheck\材料信息\自动化定义许用值.xlsx","表单名称": "其他", "初始行": 1}]
        # site1 =[{"详细地址": r"src\testCase\c_useCase_file\Aerocheck\材料信息\自动化定义许用值.xlsx","表单名称": "测试", "初始行": 1}]
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
            """载荷信息--编辑工况"""
            global source;     global old_content
            global messageType;  global actual_result
            global UseCaseNumber;  global expect3_result
            # 获取变量信息
            messageType = testdicts["预期值信息类型"]
            UseCaseNumber = testdicts["用例编号"]
            testdicts["被测程序文件地址"] = source
            expect3_result = testdicts["预期结果提示信息"]  # 取出预期值
            print("开始执行用例：", UseCaseNumber)
            actual_result= compositeMaterial(testdicts).SelectFile()  # 调用测试步骤
            print("actual_result:",actual_result)


"""复材结构强度校核--复合材料强度校核"""
@ddt
@unittest.skip(u"无条件跳过此用例")
class Test_CompoundStrengthCheck(unittest.TestCase):
        """复材结构强度校核--复合材料强度校核"""
        global number
        number = 1

        def setUp(self):
            global source;    global old_content ;global number
            global messageType ;global actual_result
            global UseCaseNumber ;global expect3_result
            from src.utils.otherMethods.initialize import module_initialize
            from tool import WindowTop
            # 被系统置顶
            WindowTop.EnumWindows("Aerobook v1.0.4")
            # 初始化变量
            source=None;old_content=None;messageType=None
            actual_result=None; UseCaseNumber=None ;expect3_result=None
            print("测试开始")
            source = r"F:\Aerobook\src\testCase\projectFile\automateFile"
            # 用例开始获取信息窗口对于的html里的内容
            old_content = Information_Win().acquire_HTML_TXT(source)

            # # 如果编辑工况弹窗没有关闭，就关闭
            # if number==1:
            #     # 清除所有的许用值曲线
            #     module_initialize().clear_AllowableCurve()
            # number =number+1







        def tearDown(self):
            """用例执行完后收尾"""
            global source;   global old_content
            global messageType;   global actual_result
            global UseCaseNumber;  global expect3_result
            # 收尾，判断有没有弹窗没有关闭，如果有就关闭
            Check_winControl("警告", "OK").popUp_Whether_close()
            # 处理测试结果
            if messageType == "信息窗口":    # 如果是对比信息窗口里的内容，就获取最新的内容
                actual_result = FormatConversion().GetLatestData(actual_result, old_content)
            if type(actual_result)==list:  # 实际值如果是列表，就转化成字符串
                actual_result = ' '.join(actual_result)
            if actual_result:   # 当实际值不为空的情况下
                # 把实际值字符串根据换行符\n转化成列表，并去掉列表中的所有的空格
                actual_result = FormatConversion().takeOut_space(actual_result)
                expect3_result = FormatConversion().takeOut_space(expect3_result)
            print("实际值：", actual_result)
            print("预期值：", expect3_result)
            #  # 断言测试结果
            assert_that(expect3_result).is_equal_to(actual_result)
            print("测试结束")


        #
        # # 测试用例Excel文件的相关信息
        # # site1 = [{"详细地址": r"src\testCase\c_useCase_file\Aerocheck\复材结构强度校核\自动化二维复合材料强度校核.xlsx","表单名称": "其他", "初始行": 1}]
        # site1 =[{"详细地址": r"src\testCase\c_useCase_file\Aerocheck\复材结构强度校核\自动化二维复合材料强度校核.xlsx","表单名称": "测试", "初始行": 1}]
        # list_dicts1 = []
        # if len(site1)>0:
        #     for site in site1:
        #         dicts1 = read_excel(site).readExcel_testCase()  # 读取测试用例
        #         ar_testdicts1 = FormatConversion().RemoveSubscript(dicts1)
        #         list_dicts1 = list_dicts1 + ar_testdicts1
        # else:
        #     list_dicts1=site1
        #
        # @unittest.skip(u"无条件跳过此用例")
        # @data(*list_dicts1)  # 参数化参数用例
        # def test_1(self, testdicts):
        #     """复材结构强度校核--复合材料强度校核"""
        #     global source;     global old_content
        #     global messageType;  global actual_result
        #     global UseCaseNumber;  global expect3_result
        #     # 获取变量信息
        #     messageType = testdicts["预期值信息类型"]
        #     UseCaseNumber = testdicts["用例编号"]
        #     testdicts["被测程序文件地址"] = source
        #     expect3_result = testdicts["预期结果提示信息"]  # 取出预期值
        #     print("开始执行用例：", UseCaseNumber)
        #     actual_result= CompoundStrengthCheck(testdicts).二D_flow_test()  # 调用测试步骤
        #     print("actual_result:",actual_result)




        # 测试用例Excel文件的相关信息
        # site2 = [{"详细地址": r"src\testCase\c_useCase_file\Aerocheck\复材结构强度校核\自动化一维复合材料强度校核.xlsx","表单名称": "其他", "初始行": 1}]
        site2 = [
            {"详细地址": r"src\testCase\c_useCase_file\Aerocheck\复材结构强度校核\自动化一维复合材料强度校核.xlsx", "表单名称": "测试", "初始行": 1}]
        list_dicts2 = []
        if len(site2) > 0:
            for site in site2:
                dicts2 = read_excel(site).readExcel_testCase()  # 读取测试用例
                ar_testdicts2 = FormatConversion().RemoveSubscript(dicts2)
                list_dicts2 = list_dicts2 + ar_testdicts2
        else:
            list_dicts2 = site2
        @data(*list_dicts2)  # 参数化参数用例
        def test_2(self, testdicts):
            """复材结构强度校核--复合材料强度校核"""
            global source;global old_content
            global messageType;global actual_result
            global UseCaseNumber;global expect3_result
            # 获取变量信息
            messageType = testdicts["预期值信息类型"]
            UseCaseNumber = testdicts["用例编号"]
            testdicts["被测程序文件地址"] = source
            expect3_result = testdicts["预期结果提示信息"]  # 取出预期值
            print("开始执行用例：", UseCaseNumber)
            actual_result = CompoundStrengthCheck(testdicts).一D_flow_test()  # 调用测试步骤
            print("actual_result:", actual_result)





if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test_LaminateOptimize))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test_Laminatedata))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test_sizeInfo_1DXls))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test_solveCalculation))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test_editWorkingCondition))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test_compositeMaterial))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test_CompoundStrengthCheck))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test_loaddatabase_popUp))
    file_name=time.strftime("%Y%m%d%H%M%S")+"铺层库优化测试报告"    # 测试报告名称
    relativeAddress = path.location()
    logPath = relativeAddress+"report//Aerocheck//laminateOptimize_testReport//" # 测试报告保存地址
    result = BeautifulReport(suite).report(filename=file_name,log_path=logPath,description="铺层库优化工作栏")
