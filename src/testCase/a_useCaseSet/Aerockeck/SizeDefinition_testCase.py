# 尺寸信息--1D2D尺寸定义
import unittest,time
from assertpy import assert_that
from BeautifulReport import BeautifulReport
from src.testCase.b_testCaseStep.Aerocheck.TestCaseStep import UseCase_step
from ddt import ddt,data
from config.relative_location import  path
from utils.otherMethods.unittest_start_finish import Initializing,finish_clear
from utils.commonality.tool import UseCase_parameterization


"""尺寸信息--1D单元尺寸定义"""
@ddt
@unittest.skip(u"暂时不执行")
class SizeDefinition_1D(unittest.TestCase):
    """尺寸信息--1D单元尺寸定义"""
    global real_UseCase_Name


    def __init__(self, *args):
        unittest.TestCase.__init__(self, *args)
        global number
        global global_UseCase_Name  # 实时用例集名
        global testCase_attribute  # 控件属性的操作方法
        global actual_result  # 实际值
        global_UseCase_Name = None
        testCase_attribute = None
        actual_result=None
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
        print("测试开始")
        # 用例执行前，初始化测试结果相关的文件
        real_UseCase_Name = "尺寸信息--1D单元尺寸定义"  # 执行该用例模块的标识
        dictSet = {"全局参数": number, "全局用例集名称": global_UseCase_Name, "当前用例集名称": real_UseCase_Name,
                   "控件属性已经操作方法": testCase_attribute}
        number, global_UseCase_Name, ProjectPath, old_content, testCase_attribute = Initializing(). \
            controller(dictSet)  # 铺层信息--铺层库优化工作栏测试用例


    def tearDown(self):
        global ProjectPath  # 项目所在路径
        global old_content  # 在执行用例前信息窗口中的文本信息，用于确定信息窗口中最新的文本
        global messageType  # 预期值信息类型
        global actual_result  # 实际值
        global expect_result  # 预期结果
        global testCase_attribute  # 控件属性方法
        dictSet = {"预期值信息类型": messageType, "信息窗口之前的文本": old_content, "实际值": actual_result,
                   "预期值": expect_result, "关闭弹窗": [["警告", "OK"]]}
        expect_result, actual_result = finish_clear().controller(dictSet)  # 当每条用例执行完毕，执行收尾工作
        """实际值跟预期值对比（文本对比）"""
        assert_that(expect_result).is_equal_to(actual_result)  # 预期值跟实际值对比
        print("测试结束")


    # Name=["一维单元尺寸定义截面形状T型"]
    Name = ["测试"]
    real_UseCase_Name = "尺寸信息--1D单元尺寸定义"
    list_dicts = UseCase_parameterization().parameterization_data(real_UseCase_Name, Name)  # 读取测试用例
    @data(*list_dicts)  # 参数化参数用例
    def test_1(self, testCase_dict):
        global ProjectPath  # 项目所在路径
        global old_content  # 在执行用例前信息窗口中的文本信息，用于确定信息窗口中最新的文本
        global messageType  # 预期值信息类型
        global actual_result  # 实际值
        global expect_result  # 预期结果
        global testCase_attribute  # 控件属性方法
        """取出Excel里面的值"""
        print("testCase_dict:", testCase_dict)
        testCase_dict["用例集名称"] = global_UseCase_Name
        UseCaseNumber = testCase_dict["用例编号"]
        expect_result = testCase_dict["预期结果文本信息"]  # 取出Excel文件中的预期值
        messageType = testCase_dict["预期值信息类型"]  # 取出提示信息载体类型
        testCase_dict["被测程序文件地址"] = ProjectPath
        print("开始执行用例：", UseCaseNumber)
        """测试用例步骤"""
        actual_result = UseCase_step(testCase_attribute, testCase_dict). \
            Perform_useCase_Steps()  # 尺寸信息--1D单元尺寸定义




"""尺寸信息--2D单元尺寸定义"""
@ddt
# @unittest.skip(u"暂时不执行")
class SizeDefinition_2D(unittest.TestCase):
    """尺寸信息--2D单元尺寸定义"""
    global real_UseCase_Name


    def __init__(self, *args):
        unittest.TestCase.__init__(self, *args)
        global number
        global global_UseCase_Name  # 实时用例集名
        global testCase_attribute  # 控件属性的操作方法
        global actual_result  # 实际值
        global_UseCase_Name = None
        testCase_attribute = None
        actual_result=None
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
        print("测试开始")
        # 用例执行前，初始化测试结果相关的文件
        real_UseCase_Name = "尺寸信息--2D单元尺寸定义"  # 执行该用例模块的标识
        dictSet = {"全局参数": number, "全局用例集名称": global_UseCase_Name, "当前用例集名称": real_UseCase_Name,
                   "控件属性已经操作方法": testCase_attribute}
        number, global_UseCase_Name, ProjectPath, old_content, testCase_attribute = Initializing(). \
            controller(dictSet)  # 铺层信息--铺层库优化工作栏测试用例


    def tearDown(self):
        global ProjectPath  # 项目所在路径
        global old_content  # 在执行用例前信息窗口中的文本信息，用于确定信息窗口中最新的文本
        global messageType  # 预期值信息类型
        global actual_result  # 实际值
        global expect_result  # 预期结果
        global testCase_attribute  # 控件属性方法
        dictSet = {"预期值信息类型": messageType, "信息窗口之前的文本": old_content, "实际值": actual_result,
                   "预期值": expect_result, "关闭弹窗": [["警告", "OK"]]}
        expect_result, actual_result = finish_clear().controller(dictSet)  # 当每条用例执行完毕，执行收尾工作
        """实际值跟预期值对比（文本对比）"""
        assert_that(expect_result).is_equal_to(actual_result)  # 预期值跟实际值对比
        print("测试结束")


    # Name=["一维单元尺寸定义截面形状T型"]
    Name = ["测试"]
    real_UseCase_Name = "尺寸信息--2D单元尺寸定义"
    list_dicts = UseCase_parameterization().parameterization_data(real_UseCase_Name, Name)  # 读取测试用例
    @data(*list_dicts)  # 参数化参数用例
    def test_1(self, testCase_dict):
        global ProjectPath  # 项目所在路径
        global old_content  # 在执行用例前信息窗口中的文本信息，用于确定信息窗口中最新的文本
        global messageType  # 预期值信息类型
        global actual_result  # 实际值
        global expect_result  # 预期结果
        global testCase_attribute  # 控件属性方法
        """取出Excel里面的值"""
        print("testCase_dict:", testCase_dict)
        testCase_dict["用例集名称"] = global_UseCase_Name
        UseCaseNumber = testCase_dict["用例编号"]
        expect_result = testCase_dict["预期结果文本信息"]  # 取出Excel文件中的预期值
        messageType = testCase_dict["预期值信息类型"]  # 取出提示信息载体类型
        testCase_dict["被测程序文件地址"] = ProjectPath
        print("开始执行用例：", UseCaseNumber)
        """测试用例步骤"""
        actual_result = UseCase_step(testCase_attribute, testCase_dict). \
            Perform_useCase_Steps()  # 尺寸信息--2D单元尺寸定义


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(SizeDefinition_1D))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(SizeDefinition_2D))
    file_name=time.strftime("%Y%m%d%H%M%S")+"Aerocheck尺寸信息1D2D单元尺寸定义"    # 测试报告名称
    relativeAddress = path.location()
    logPath = relativeAddress+"report//Aerocheck//laminateOptimize_testReport//" # 测试报告保存地址
    result = BeautifulReport(suite).report(filename=file_name,log_path=logPath,description="铺层库优化工作栏")