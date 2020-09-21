# Aerobook主流程测试用例

import unittest,time
from assertpy import assert_that
from BeautifulReport import BeautifulReport
from src.testCase.b_testCaseStep.Aerocheck.TestCaseStep import UseCase_step
from ddt import ddt,data
from config.relative_location import  path
from utils.otherMethods.unittest_start_finish import Initializing,finish_clear
from utils.commonality.tool import UseCase_parameterization
from config.configurationFile import ProfileDataProcessing


"""铺层信息--铺层库优化工作栏测试用例"""
@ddt
# @unittest.skip(u"暂时不执行")
class Test_LaminateOptimize(unittest.TestCase):
    """铺层库优化工作栏测试用例"""
    global real_UseCase_Name

    def __init__(self, *args):
        unittest.TestCase.__init__(self, *args)
        global number
        global global_UseCase_Name     #   实时用例集名
        global testCase_attribute  # 控件属性的操作方法
        global_UseCase_Name = None
        testCase_attribute=None
        number = 0


    def setUp(self):
        """
        每次执行测试用例前都做的操作
        :return:
        """
        global ProjectPath  # 项目所在路径
        global old_content  # 在执行用例前信息窗口中的文本信息，用于确定信息窗口中最新的文本
        global messageType  # 预期值信息类型
        global actual_result  # 实际值
        global expect_result  # 预期结果
        global testCase_attribute  # 控件属性方法
        global global_UseCase_Name #   实时用例集名称
        global number
        print("测试开始")
        # 用例执行前，初始化测试结果相关的文件
        list_filePath = ["PlyLib_451.xlsx", "PlyLibDb_451.xlsx"]  # 在执行用例前需要删除的文件
        real_UseCase_Name = ProfileDataProcessing("TestCase_moduleName", "UseCaseName_1").config_File() # 执行该用例模块的标识
        dictSet = {"全局参数": number, "全局用例集名称": global_UseCase_Name, "当前用例集名称": real_UseCase_Name,
                   "删除文件名列表": list_filePath,
                   "控件属性已经操作方法":testCase_attribute}
        number,global_UseCase_Name,ProjectPath,old_content,testCase_attribute = Initializing().\
            controller(dictSet) # 铺层信息--铺层库优化工作栏测试用例





    def tearDown(self):
        global ProjectPath  # 项目所在路径
        global old_content  # 在执行用例前信息窗口中的文本信息，用于确定信息窗口中最新的文本
        global messageType  # 预期值信息类型
        global actual_result  # 实际值
        global expect_result  # 预期结果
        global testCase_attribute  # 控件属性方法
        dictSet={"预期值信息类型":messageType,"信息窗口之前的文本":old_content,"实际值":actual_result,
                 "预期值":expect_result,"关闭弹窗":[["警告", "OK"]]}
        expect_result,actual_result = finish_clear().controller(dictSet)  # 当每条用例执行完毕，执行收尾工作
        """实际值跟预期值对比（文本对比）"""
        assert_that(expect_result).is_equal_to(actual_result)  # 预期值跟实际值对比
        print("测试结束")




    # Name=["最大铺层数","最小铺层数","铺层比","容差比","单层厚度","弹性模量E11(MPa)","弹性模量E22（MPa）","泊松比v12","剪切模量G12（MPa）"
    #     ,"层合板长度a(mm)","层合板宽度b(mm)","Mat8材料ID","数据库名称","路径文本框","Mat8材料ID","保存为铺层数据库和保存为Excel勾选框"]
    Name =["测试"]
    real_UseCase_Name = ProfileDataProcessing("TestCase_moduleName", "UseCaseName_1").config_File()  # 执行该用例模块的标识
    list_dicts=UseCase_parameterization().parameterization_data(real_UseCase_Name, Name)    # 读取测试用例
    @data(*list_dicts)    # 参数化参数用例
    def test_1(self,testCase_dict):
        global ProjectPath  # 项目所在路径
        global old_content  # 在执行用例前信息窗口中的文本信息，用于确定信息窗口中最新的文本
        global messageType  # 预期值信息类型
        global actual_result  # 实际值
        global expect_result  # 预期结果
        global testCase_attribute  # 控件属性方法
        """取出Excel里面的值"""
        print("testCase_dict:",testCase_dict)
        testCase_dict["用例集名称"]=global_UseCase_Name
        UseCaseNumber = testCase_dict["用例编号"]
        expect_result = testCase_dict["预期结果文本信息"]  # 取出Excel文件中的预期值
        messageType = testCase_dict["预期值信息类型"]  # 取出提示信息载体类型
        testCase_dict["被测程序文件地址"] = ProjectPath
        print("开始执行用例：", UseCaseNumber)
        """测试用例步骤"""
        actual_result=UseCase_step(testCase_attribute,testCase_dict).\
            Perform_useCase_Steps()  #铺层信息--铺层库优化工作栏测试用例


"""铺层信息--铺层数据库制作工具弹窗"""
@ddt
@unittest.skip(u"暂时不执行")
class Test_LaminatedataPopup(unittest.TestCase):
        """铺层信息--铺层数据库制作工具弹窗"""
        global real_UseCase_Name

        def __init__(self, *args):
            unittest.TestCase.__init__(self, *args)
            global number
            global global_UseCase_Name
            global_UseCase_Name = None
            global testCase_attribute  # 实时用例集名称
            testCase_attribute = None
            number = 0

        def setUp(self):
            """
            每次执行测试用例前都做的操作
            :return:
            """
            global ProjectPath  # 项目所在路径
            global old_content  # 在执行用例前信息窗口中的文本信息，用于确定信息窗口中最新的文本
            global messageType  # 预期值信息类型
            global actual_result  # 实际值
            global expect_result  # 预期结果
            global testCase_attribute  # 控件属性方法
            global global_UseCase_Name  # 实时用例集名称
            global number
            real_UseCase_Name = ProfileDataProcessing("TestCase_moduleName",
                                                      "UseCaseName_2").config_File()  # 执行该用例模块的标识
            dictSet = {"全局参数": number, "全局用例集名称": global_UseCase_Name, "当前用例集名称": real_UseCase_Name
                       ,"关闭弹窗":[["铺层数据库制作工具", "关闭"]],"控件属性已经操作方法":testCase_attribute}
            number, global_UseCase_Name, ProjectPath, old_content, testCase_attribute = Initializing().controller(
                dictSet)



        def tearDown(self):
            """用例执行完后收尾
                           1、首先把复制的文件夹删除
            """
            global ProjectPath  # 项目所在路径
            global old_content  # 在执行用例前信息窗口中的文本信息，用于确定信息窗口中最新的文本
            global messageType  # 预期值信息类型
            global actual_result  # 实际值
            global expect_result  # 预期结果
            global testCase_attribute  # 控件属性方法
            """ 收尾，如果有警告弹框就关掉"""
            dictSet = {"预期值信息类型": messageType, "信息窗口之前的文本": old_content, "实际值": actual_result,
                       "预期值": expect_result, "关闭弹窗": [["警告", "OK"],["铺层数据库制作工具", "关闭"]]}
            expect_result,actual_result = finish_clear().controller(dictSet)
            """实际值跟预期值对比（文本对比）"""
            assert_that(expect_result).is_equal_to(actual_result)
            print("测试结束")





        Name = ["铺层库制作弹窗", "选择铺层Excel文件", "铺层数据保存路径文本框"]
        # Name = ["测试"]
        real_UseCase_Name = ProfileDataProcessing("TestCase_moduleName",
                                                  "UseCaseName_2").config_File()  # 执行该用例模块的标识
        list_dicts = UseCase_parameterization().parameterization_data(real_UseCase_Name, Name)
        @data(*list_dicts)  # 参数化参数用例
        def test_1(self, testCase_dict):
            """铺层数据库制作工具弹框"""
            global ProjectPath  # 项目所在路径
            global old_content  # 在执行用例前信息窗口中的文本信息，用于确定信息窗口中最新的文本
            global messageType  # 预期值信息类型
            global actual_result  # 实际值
            global expect_result  # 预期结果
            global testCase_attribute  # 控件属性方法
            global els  # 控件属性方法
            testCase_dict["用例集名称"] = global_UseCase_Name
            UseCaseNumber = testCase_dict["用例编号"]
            expect_result = testCase_dict["预期结果文本信息"]  # 取出Excel文件中的预期值
            messageType = testCase_dict["预期值信息类型"]  # 取出提示信息载体类型
            els = testCase_dict["其他"]  # 取出提示信息载体类型
            testCase_dict["被测程序文件地址"] = ProjectPath
            print("开始执行用例：", UseCaseNumber)
            """测试用例步骤"""
            actual_result=UseCase_step(testCase_attribute,testCase_dict).\
                Perform_useCase_Steps()  #铺层信息--铺层数据库制作工具弹窗


"""尺寸信息--一维二维单元尺寸定义（模板）"""
@ddt
@unittest.skip(u"暂时不执行")
class Test_sizeInfo_1D2DXls(unittest.TestCase):
        """尺寸信息--一维二维单元尺寸定义（模板）"""
        global real_UseCase_Name

        def __init__(self, *args):
            unittest.TestCase.__init__(self, *args)
            global number
            global global_UseCase_Name
            global_UseCase_Name = None
            global testCase_attribute  # 实时用例集名称
            testCase_attribute = None
            number = 0

        def setUp(self):
            """
            每次执行测试用例前都做的操作
            :return:
            """
            global ProjectPath  # 项目所在路径
            global old_content  # 在执行用例前信息窗口中的文本信息，用于确定信息窗口中最新的文本
            global messageType  # 预期值信息类型
            global actual_result  # 实际值
            global expect_result  # 预期结果
            global testCase_attribute  # 控件属性方法
            global global_UseCase_Name  # 实时用例集名称
            global number
            real_UseCase_Name = "尺寸信息--一维二维单元尺寸定义（模板）"
            dictSet = {"全局参数": number, "全局用例集名称": global_UseCase_Name, "当前用例集名称": real_UseCase_Name,
                       "控件属性已经操作方法":testCase_attribute}
            number, global_UseCase_Name, ProjectPath, old_content, testCase_attribute = Initializing().controller(
                dictSet)


        def tearDown(self):
            global ProjectPath  # 项目所在路径
            global old_content  # 在执行用例前信息窗口中的文本信息，用于确定信息窗口中最新的文本
            global messageType  # 预期值信息类型
            global actual_result  # 实际值
            global expect_result  # 预期结果
            global testCase_attribute  # 控件属性方法
            """ 收尾，如果有警告弹框就关掉"""
            dictSet = {"预期值信息类型": messageType, "信息窗口之前的文本": old_content, "实际值": actual_result,
                       "预期值": expect_result, "关闭弹窗": [["警告", "OK"]]}
            expect_result, actual_result = finish_clear().controller(dictSet)
            """实际值跟预期值对比（文本对比）"""
            assert_that(expect_result).is_equal_to(actual_result)
            print("测试结束")



        Name = ["一维单元尺寸定义复合材料（模板）", "一维单元尺寸定义金属材料（模板）", "二维单元尺寸定义金属材料（模板）","二维单元尺寸定义金属材料（模板）"]
        # Name =["测试"]
        real_UseCase_Name = "尺寸信息--一维二维单元尺寸定义（模板）"
        list_dicts = UseCase_parameterization().parameterization_data(real_UseCase_Name, Name)
        @data(*list_dicts)  # 参数化参数用例
        def test_1(self, testCase_dict):
            """尺寸信息--一维单元尺寸定义（模板）"""
            global ProjectPath  # 项目所在路径
            global old_content  # 在执行用例前信息窗口中的文本信息，用于确定信息窗口中最新的文本
            global messageType  # 预期值信息类型
            global actual_result  # 实际值
            global expect_result  # 预期结果
            global testCase_attribute  # 控件属性方法
            global els  # 控件属性方法
            testCase_dict["用例集名称"] = global_UseCase_Name
            UseCaseNumber = testCase_dict["用例编号"]
            expect_result = testCase_dict["预期结果文本信息"]  # 取出Excel文件中的预期值
            messageType = testCase_dict["预期值信息类型"]  # 取出提示信息载体类型
            els = testCase_dict["其他"]  # 取出提示信息载体类型
            testCase_dict["被测程序文件地址"] = ProjectPath
            print("开始执行用例：", UseCaseNumber)
            """测试用例步骤"""
            actual_result = UseCase_step(testCase_attribute, testCase_dict).\
                Perform_useCase_Steps() #尺寸信息--一维二维单元尺寸定义（模板）


"""求解计算--求解计算"""
@ddt
@unittest.skip(u"暂时不执行")
class Test_solveCalculation(unittest.TestCase):
        """求解计算--求解计算"""
        global real_UseCase_Name


        def __init__(self, *args):
            unittest.TestCase.__init__(self, *args)
            global number
            global global_UseCase_Name
            global_UseCase_Name = None
            global testCase_attribute  # 实时用例集名称
            testCase_attribute = None
            number = 0


        def setUp(self):
            global ProjectPath  # 项目所在路径
            global old_content  # 在执行用例前信息窗口中的文本信息，用于确定信息窗口中最新的文本
            global messageType  # 预期值信息类型
            global actual_result  # 实际值
            global expect_result  # 预期结果
            global testCase_attribute  # 控件属性方法
            global global_UseCase_Name  # 实时用例集名称
            global number
            real_UseCase_Name = "求解计算--求解计算"
            list_filePath = ["hwsolver.mesg", "os.bat", "run.vbs", "update_Htail.h3d", "update_Htail.html",
                             "update_Htail.mvw", "update_Htail.out", "update_Htail.pch", "update_Htail.res",
                             "update_Htail.stat", "update_Htail_frames.html", "update_Htail_menu.html"]
            real_UseCase_Name = "Test_solveCalculation"
            dictSet = {"全局参数": number, "全局用例集名称": global_UseCase_Name, "当前用例集名称": real_UseCase_Name
                , "删除文件名列表":list_filePath,"控件属性已经操作方法":testCase_attribute}
            number, global_UseCase_Name, ProjectPath, old_content, testCase_attribute = Initializing().controller(
                dictSet)


        def tearDown(self):
            """用例执行完后收尾"""
            global ProjectPath  # 项目所在路径
            global old_content  # 在执行用例前信息窗口中的文本信息，用于确定信息窗口中最新的文本
            global messageType  # 预期值信息类型
            global actual_result  # 实际值
            global expect_result  # 预期结果
            global testCase_attribute  # 控件属性方法
            """ 收尾，如果有警告弹框就关掉"""
            dictSet = {"预期值信息类型": messageType, "信息窗口之前的文本": old_content, "实际值": actual_result,
                       "预期值": expect_result, "关闭弹窗": [["警告", "OK"]]}
            expect_result, actual_result = finish_clear().controller(dictSet)
            """实际值跟预期值对比（文本对比）"""
            assert_that(expect_result).is_equal_to(actual_result)
            print("测试结束")



        Name = ["属性更新选择路径",  "载荷提取选择路径"]
        real_UseCase_Name = "求解计算--求解计算"
        list_dicts = UseCase_parameterization().parameterization_data(real_UseCase_Name, Name)
        @data(*list_dicts)  # 参数化参数用例
        # @unittest.skip(u"无条件跳过此用例")
        def test_1(self, testCase_dict):
            """求解计算--求解计算--文本框"""
            global ProjectPath  # 项目所在路径
            global old_content  # 在执行用例前信息窗口中的文本信息，用于确定信息窗口中最新的文本
            global messageType  # 预期值信息类型
            global actual_result  # 实际值
            global expect_result  # 预期结果
            global testCase_attribute  # 控件属性方法
            global els  # 控件属性方法
            testCase_dict["用例集名称"] = global_UseCase_Name
            UseCaseNumber = testCase_dict["用例编号"]
            expect_result = testCase_dict["预期结果文本信息"]  # 取出Excel文件中的预期值
            messageType = testCase_dict["预期值信息类型"]  # 取出提示信息载体类型
            els = testCase_dict["其他"]  # 取出提示信息载体类型
            testCase_dict["被测程序文件地址"] = ProjectPath
            print("开始执行用例：", UseCaseNumber)
            """测试用例步骤"""
            actual_result = UseCase_step(testCase_attribute, testCase_dict).\
                Perform_useCase_Steps()  # 求解计算--求解计算



"""载荷信息--载荷数据库制作工具弹窗"""
@ddt
@unittest.skip(u"暂时不执行")
class Test_loaddatabase_popUp(unittest.TestCase):
        """载荷信息--载荷数据库制作工具弹窗"""
        global real_UseCase_Name

        def __init__(self, *args):
            unittest.TestCase.__init__(self, *args)
            global number
            global global_UseCase_Name
            global_UseCase_Name = None
            global testCase_attribute  # 实时用例集名称
            testCase_attribute = None
            number = 0

        def setUp(self):
            """
            每次执行测试用例前都做的操作
            :return:
            """
            global ProjectPath  # 项目所在路径
            global old_content  # 在执行用例前信息窗口中的文本信息，用于确定信息窗口中最新的文本
            global messageType  # 预期值信息类型
            global actual_result  # 实际值
            global expect_result  # 预期结果
            global testCase_attribute  # 控件属性方法
            global global_UseCase_Name  # 实时用例集名称
            global number
            real_UseCase_Name = "载荷信息--载荷数据库制作工具弹窗"
            dictSet = {"全局参数": number, "全局用例集名称": global_UseCase_Name, "当前用例集名称": real_UseCase_Name,
                       "关闭弹窗":[["铺层数据库制作工具", "关闭"]],"控件属性已经操作方法":testCase_attribute}
            number, global_UseCase_Name, ProjectPath, old_content, testCase_attribute = Initializing().controller(
                dictSet)



        def tearDown(self):
            """用例执行完后收尾
                           1、首先把复制的文件夹删除
            """
            global ProjectPath  # 项目所在路径
            global old_content  # 在执行用例前信息窗口中的文本信息，用于确定信息窗口中最新的文本
            global messageType  # 预期值信息类型
            global actual_result  # 实际值
            global expect_result  # 预期结果
            global testCase_attribute  # 控件属性方法
            """ 收尾，如果有警告弹框就关掉"""
            dictSet = {"预期值信息类型": messageType, "信息窗口之前的文本": old_content, "实际值": actual_result,
                       "预期值": expect_result, "关闭弹窗": [["警告", "OK"],["载荷数据库制作工具", "关闭"]]}
            expect_result, actual_result = finish_clear().controller(dictSet)
            """实际值跟预期值对比（文本对比）"""
            assert_that(expect_result).is_equal_to(actual_result)
            print("测试结束")




        Name = ["载荷数据库制作弹窗", "选择载荷文件","载荷数据库保存路径"]
        real_UseCase_Name = "载荷信息--载荷数据库制作工具弹窗"
        list_dicts = UseCase_parameterization().parameterization_data(real_UseCase_Name, Name)
        # @unittest.skip(u"无条件跳过此用例")
        @data(*list_dicts)  # 参数化参数用例
        def test_1(self, testCase_dict):
            """载荷信息--载荷数据库制作工具弹窗"""
            global ProjectPath  # 项目所在路径
            global old_content  # 在执行用例前信息窗口中的文本信息，用于确定信息窗口中最新的文本
            global messageType  # 预期值信息类型
            global actual_result  # 实际值
            global expect_result  # 预期结果
            global testCase_attribute  # 控件属性方法
            global els  # 控件属性方法
            testCase_dict["用例集名称"] = global_UseCase_Name
            UseCaseNumber = testCase_dict["用例编号"]
            expect_result = testCase_dict["预期结果文本信息"]  # 取出Excel文件中的预期值
            messageType = testCase_dict["预期值信息类型"]  # 取出提示信息载体类型
            els = testCase_dict["其他"]  # 取出提示信息载体类型
            testCase_dict["被测程序文件地址"] = ProjectPath
            print("开始执行用例：", UseCaseNumber)
            """测试用例步骤"""
            actual_result = UseCase_step(testCase_attribute, testCase_dict).\
                Perform_useCase_Steps()  # 载荷信息--载荷数据库制作工具弹窗


"""载荷信息--编辑工况"""
@ddt
@unittest.skip(u"暂时不执行")
class Test_editWorkingCondition(unittest.TestCase):
        """载荷信息--编辑工况"""
        global real_UseCase_Name


        def __init__(self, *args):
            unittest.TestCase.__init__(self, *args)
            global ProjectPath  # 项目所在路径
            global old_content  # 在执行用例前信息窗口中的文本信息，用于确定信息窗口中最新的文本
            global messageType  # 预期值信息类型
            global actual_result  # 实际值
            global expect_result  # 预期结果
            global testCase_attribute  # 控件属性方法
            global global_UseCase_Name  # 实时用例集名称
            ProjectPath=None
            old_content=None
            messageType=None
            actual_result=None
            expect_result = None
            testCase_attribute = None
            global_UseCase_Name = None
            number = 0


        def setUp(self):
            global ProjectPath  # 项目所在路径
            global old_content  # 在执行用例前信息窗口中的文本信息，用于确定信息窗口中最新的文本
            global messageType  # 预期值信息类型
            global actual_result  # 实际值
            global expect_result  # 预期结果
            global testCase_attribute  # 控件属性方法
            global global_UseCase_Name  # 实时用例集名称
            global number
            real_UseCase_Name = "载荷信息--编辑工况"
            dictSet = {"全局参数": number, "全局用例集名称": global_UseCase_Name, "当前用例集名称": real_UseCase_Name,
                       "关闭弹窗":["编辑工况", "关闭"],"控件属性已经操作方法":testCase_attribute}
            number, global_UseCase_Name,ProjectPath,old_content,testCase_attribute = Initializing().controller(dictSet)





        def tearDown(self):
            """用例执行完后收尾"""
            global ProjectPath  # 项目所在路径
            global old_content  # 在执行用例前信息窗口中的文本信息，用于确定信息窗口中最新的文本
            global messageType  # 预期值信息类型
            global actual_result  # 实际值
            global expect_result  # 预期结果
            global testCase_attribute  # 控件属性方法
            """ 收尾，如果有警告弹框就关掉"""
            dictSet = {"预期值信息类型": messageType, "信息窗口之前的文本": old_content, "实际值": actual_result,
                       "预期值": expect_result, "关闭弹窗": [["警告", "OK"], ["编辑工况", "关闭"]]}
            expect_result, actual_result = finish_clear().controller(dictSet)
            """实际值跟预期值对比（文本对比）"""
            assert_that(expect_result).is_equal_to(actual_result)
            print("测试结束")



        Name = ["新建", "重命名"]
        real_UseCase_Name = "载荷信息--编辑工况"
        list_dicts = UseCase_parameterization().parameterization_data(real_UseCase_Name, Name)
        @data(*list_dicts)  # 参数化参数用例
        def test_1(self, testCase_dict):
            """编辑工况"""
            global ProjectPath  # 项目所在路径
            global old_content  # 在执行用例前信息窗口中的文本信息，用于确定信息窗口中最新的文本
            global messageType  # 预期值信息类型
            global actual_result  # 实际值
            global expect_result  # 预期结果
            global testCase_attribute  # 控件属性方法
            global els  # 控件属性方法
            testCase_dict["用例集名称"] = global_UseCase_Name
            UseCaseNumber = testCase_dict["用例编号"]
            expect_result = testCase_dict["预期结果文本信息"]  # 取出Excel文件中的预期值
            messageType = testCase_dict["预期值信息类型"]  # 取出提示信息载体类型
            els = testCase_dict["其他"]  # 取出提示信息载体类型
            testCase_dict["被测程序文件地址"] = ProjectPath
            print("开始执行用例：", UseCaseNumber)
            """测试用例步骤"""
            actual_result = UseCase_step(testCase_attribute, testCase_dict).\
                Perform_useCase_Steps()  # 载荷信息--编辑工况


"""材料信息--定义复合材料参数"""
@ddt
@unittest.skip(u"暂时不执行")
class Test_compositeMaterial(unittest.TestCase):
        """材料信息--定义复合材料参数"""
        global real_UseCase_Name

        def __init__(self, *args):
            unittest.TestCase.__init__(self, *args)
            global number
            global global_UseCase_Name
            global_UseCase_Name = None
            global testCase_attribute  # 实时用例集名称
            testCase_attribute = None
            number = 0


        def setUp(self):
            global ProjectPath  # 项目所在路径
            global old_content  # 在执行用例前信息窗口中的文本信息，用于确定信息窗口中最新的文本
            global messageType  # 预期值信息类型
            global actual_result  # 实际值
            global expect_result  # 预期结果
            global testCase_attribute  # 控件属性方法
            global global_UseCase_Name  # 实时用例集名称
            global number
            real_UseCase_Name = "材料信息--定义复合材料参数"
            dictSet = {"全局参数": number, "全局用例集名称": global_UseCase_Name, "当前用例集名称": real_UseCase_Name,
                       "控件属性已经操作方法":testCase_attribute}
            number, global_UseCase_Name, ProjectPath,old_content,testCase_attribute = Initializing().controller(dictSet)




        def tearDown(self):
            """用例执行完后收尾"""
            global ProjectPath  # 项目所在路径
            global old_content  # 在执行用例前信息窗口中的文本信息，用于确定信息窗口中最新的文本
            global messageType  # 预期值信息类型
            global actual_result  # 实际值
            global expect_result  # 预期结果
            global testCase_attribute  # 控件属性方法
            """ 收尾，如果有警告弹框就关掉"""
            dictSet = {"预期值信息类型": messageType, "信息窗口之前的文本": old_content, "实际值": actual_result,
                       "预期值": expect_result, "关闭弹窗": [["警告", "OK"]]}
            expect_result, actual_result = finish_clear().controller(dictSet)
            """实际值跟预期值对比（文本对比）"""
            assert_that(expect_result).is_equal_to(actual_result)
            print("测试结束")


        # Name = ["其他"]
        Name = ["测试"]
        real_UseCase_Name = "材料信息--定义复合材料参数"
        list_dicts = UseCase_parameterization().parameterization_data(real_UseCase_Name, Name)
        @data(*list_dicts)  # 参数化参数用例
        def test_1(self, testCase_dict):
            """载荷信息--编辑工况"""
            global ProjectPath  # 项目所在路径
            global old_content  # 在执行用例前信息窗口中的文本信息，用于确定信息窗口中最新的文本
            global messageType  # 预期值信息类型
            global actual_result  # 实际值
            global expect_result  # 预期结果
            global testCase_attribute  # 控件属性方法
            global els  # 控件属性方法
            testCase_dict["用例集名称"] = global_UseCase_Name
            print("testCase_dict:", testCase_dict)
            print("testCase_attribute:", testCase_attribute)
            UseCaseNumber = testCase_dict["用例编号"]
            expect_result = testCase_dict["预期结果文本信息"]  # 取出Excel文件中的预期值
            messageType = testCase_dict["预期值信息类型"]  # 取出提示信息载体类型
            els = testCase_dict["其他"]  # 取出提示信息载体类型
            testCase_dict["被测程序文件地址"] = ProjectPath
            print("开始执行用例：", UseCaseNumber)
            actual_result = UseCase_step(testCase_attribute, testCase_dict).Perform_useCase_Steps_nest()  # 调用测试步骤



"""复材结构强度校核--复合材料强度校核1D"""
@ddt
@unittest.skip(u"暂时不执行")
class Test_CompoundStrengthCheck1D(unittest.TestCase):
        """复材结构强度校核--复合材料强度校核"""
        global real_UseCase_Name
        global_UseCase_Name = None

        def __init__(self, *args):
            unittest.TestCase.__init__(self, *args)
            global ProjectPath  # 项目所在路径
            global old_content  # 在执行用例前信息窗口中的文本信息，用于确定信息窗口中最新的文本
            global messageType  # 预期值信息类型
            global actual_result  # 实际值
            global expect_result  # 预期结果
            global testCase_attribute  # 控件属性方法
            global global_UseCase_Name  # 实时用例集名称
            ProjectPath = None
            old_content = None
            messageType = None
            actual_result = None
            expect_result = None
            testCase_attribute = None
            global_UseCase_Name = None
            number = 0


        def setUp(self):
            global ProjectPath  # 项目所在路径
            global old_content  # 在执行用例前信息窗口中的文本信息，用于确定信息窗口中最新的文本
            global messageType  # 预期值信息类型
            global actual_result  # 实际值
            global expect_result  # 预期结果
            global testCase_attribute  # 控件属性方法
            global global_UseCase_Name  # 实时用例集名称
            global real_UseCase_Name
            global number
            real_UseCase_Name = "复材结构强度校核--复合材料强度校核1D"
            dictSet = {"全局参数": number, "全局用例集名称": global_UseCase_Name, "当前用例集名称": real_UseCase_Name,
                       "控件属性已经操作方法":testCase_attribute}
            number, global_UseCase_Name, ProjectPath,old_content,testCase_attribute = Initializing().controller(dictSet)



        def tearDown(self):
            """用例执行完后收尾"""
            global ProjectPath  # 项目所在路径
            global old_content  # 在执行用例前信息窗口中的文本信息，用于确定信息窗口中最新的文本
            global messageType  # 预期值信息类型
            global actual_result  # 实际值
            global expect_result  # 预期结果
            global testCase_attribute  # 控件属性方法
            """ 收尾，如果有警告弹框就关掉"""
            dictSet = {"预期值信息类型": messageType, "信息窗口之前的文本": old_content, "实际值": actual_result,
                       "预期值": expect_result, "关闭弹窗": [["警告", "OK"]]}
            expect_result, actual_result = finish_clear().controller(dictSet)
            """实际值跟预期值对比（文本对比）"""
            assert_that(expect_result).is_equal_to(actual_result)
            print("测试结束")


        Name = ["其他"]
        print("执行")
        real_UseCase_Name = "复材结构强度校核--复合材料强度校核1D"
        list_dicts = UseCase_parameterization().parameterization_data(real_UseCase_Name, Name)
        @data(*list_dicts)  # 参数化参数用例
        def test_1(self, testCase_dict):
            """复材结构强度校核--复合材料强度校核"""
            global ProjectPath  # 项目所在路径
            global old_content  # 在执行用例前信息窗口中的文本信息，用于确定信息窗口中最新的文本
            global messageType  # 预期值信息类型
            global actual_result  # 实际值
            global expect_result  # 预期结果
            global testCase_attribute  # 控件属性方法
            global els  # 控件属性方法
            testCase_dict["用例集名称"] = global_UseCase_Name
            print("testCase_dict:", testCase_dict)
            print("testCase_attribute:", testCase_attribute)
            UseCaseNumber = testCase_dict["用例编号"]
            expect_result = testCase_dict["预期结果文本信息"]  # 取出Excel文件中的预期值
            messageType = testCase_dict["预期值信息类型"]  # 取出提示信息载体类型
            els = testCase_dict["其他"]  # 取出提示信息载体类型
            testCase_dict["被测程序文件地址"] = ProjectPath
            print("开始执行用例：", UseCaseNumber)
            actual_result = UseCase_step(testCase_attribute, testCase_dict).\
                Perform_useCase_Steps()  # 复材结构强度校核--复合材料强度校核


"""复材结构强度校核--复合材料强度校核2D"""
@ddt
@unittest.skip(u"暂时不执行")
class Test_CompoundStrengthCheck2D(unittest.TestCase):
        """复材结构强度校核--复合材料强度校核"""
        global real_UseCase_Name


        def __init__(self, *args):
            unittest.TestCase.__init__(self, *args)
            global ProjectPath  # 项目所在路径
            global old_content  # 在执行用例前信息窗口中的文本信息，用于确定信息窗口中最新的文本
            global messageType  # 预期值信息类型
            global actual_result  # 实际值
            global expect_result  # 预期结果
            global testCase_attribute  # 控件属性方法
            global global_UseCase_Name  # 实时用例集名称
            ProjectPath = None
            old_content = None
            messageType = None
            actual_result = None
            expect_result = None
            testCase_attribute = None
            global_UseCase_Name = None
            number = 0


        def setUp(self):
            global ProjectPath  # 项目所在路径
            global old_content  # 在执行用例前信息窗口中的文本信息，用于确定信息窗口中最新的文本
            global messageType  # 预期值信息类型
            global actual_result  # 实际值
            global expect_result  # 预期结果
            global testCase_attribute  # 控件属性方法
            global global_UseCase_Name  # 实时用例集名称
            global number
            real_UseCase_Name = "复材结构强度校核--复合材料强度校核2D"
            dictSet = {"全局参数": number, "全局用例集名称": global_UseCase_Name, "当前用例集名称": real_UseCase_Name,
                       "控件属性已经操作方法":testCase_attribute}
            number, global_UseCase_Name, ProjectPath,old_content,testCase_attribute = Initializing().controller(dictSet)



        def tearDown(self):
            """用例执行完后收尾"""
            global ProjectPath  # 项目所在路径
            global old_content  # 在执行用例前信息窗口中的文本信息，用于确定信息窗口中最新的文本
            global messageType  # 预期值信息类型
            global actual_result  # 实际值
            global expect_result  # 预期结果
            global testCase_attribute  # 控件属性方法
            """ 收尾，如果有警告弹框就关掉"""
            dictSet = {"预期值信息类型": messageType, "信息窗口之前的文本": old_content, "实际值": actual_result,
                       "预期值": expect_result, "关闭弹窗": [["警告", "OK"]]}
            expect_result, actual_result = finish_clear().controller(dictSet)
            """实际值跟预期值对比（文本对比）"""
            assert_that(expect_result).is_equal_to(actual_result)
            print("测试结束")


        # Name = ["其他"]
        Name = ["测试"]
        real_UseCase_Name = "复材结构强度校核--复合材料强度校核2D"
        list_dicts = UseCase_parameterization().parameterization_data(real_UseCase_Name, Name)
        @data(*list_dicts)  # 参数化参数用例
        def test_1(self, testCase_dict):
            """复材结构强度校核--复合材料强度校核"""
            global ProjectPath  # 项目所在路径
            global old_content  # 在执行用例前信息窗口中的文本信息，用于确定信息窗口中最新的文本
            global messageType  # 预期值信息类型
            global actual_result  # 实际值
            global expect_result  # 预期结果
            global testCase_attribute  # 控件属性方法
            global els  # 控件属性方法
            testCase_dict["用例集名称"] = global_UseCase_Name
            print("testCase_dict:", testCase_dict)
            print("testCase_attribute:", testCase_attribute)
            UseCaseNumber = testCase_dict["用例编号"]
            expect_result = testCase_dict["预期结果文本信息"]  # 取出Excel文件中的预期值
            messageType = testCase_dict["预期值信息类型"]  # 取出提示信息载体类型
            els = testCase_dict["其他"]  # 取出提示信息载体类型
            testCase_dict["被测程序文件地址"] = ProjectPath
            print("开始执行用例：", UseCaseNumber)
            actual_result = UseCase_step(testCase_attribute, testCase_dict).\
                Perform_useCase_Steps()  # 复材结构强度校核--复合材料强度校核



if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test_LaminateOptimize))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test_LaminatedataPopup))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test_sizeInfo_1D2DXls))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test_loaddatabase_popUp))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test_solveCalculation))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test_editWorkingCondition))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test_compositeMaterial))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test_CompoundStrengthCheck1D))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test_CompoundStrengthCheck2D))
    file_name=time.strftime("%Y%m%d%H%M%S")+"Aerocheck主流程测试报告"    # 测试报告名称
    relativeAddress = path.location()
    logPath = relativeAddress+"report//Aerocheck//laminateOptimize_testReport//" # 测试报告保存地址
    result = BeautifulReport(suite).report(filename=file_name,log_path=logPath,description="铺层库优化工作栏")
