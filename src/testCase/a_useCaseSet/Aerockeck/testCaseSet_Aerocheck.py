# 尺寸信息--1D2D尺寸定义
import unittest,time,datetime,sys
from assertpy import assert_that
from BeautifulReport import BeautifulReport
from src.testCase.b_testCaseStep.Aerocheck.TestCaseStep import UseCase_step
from ddt import ddt,data
from utils.otherMethods.unittest_start_finish import Initializing,finish_clear,handlingMethod
from utils.commonality.tool import UseCase_parameterization
from time import *




"""测试用例集"""
@ddt
# @unittest.skip(u"暂时不执行")
class  test_UseCaseSet_Aerocheck(unittest.TestCase):
    """测试用例集"""
    global list_dict_site


    """获取测试用例"""
    list_dict_site = UseCase_parameterization().parameterization_data()  # 读取测试用例
    print("\033[5;33m获取的测试用例：\033[0m", list_dict_site, __file__, sys._getframe().f_lineno)
    print("")




    def __init__(self, *args):
        unittest.TestCase.__init__(self, *args)
        """全局变量"""
        global UseSet_n       # 用例集名称
        global useCase_sum    # 记录执行用例的总次数，根据次数取出对应的用例
        global host_Module  # 记录主模块（Aerocheck、Fiberbook等）名称
        global Use_attribute #控件属性已经操作方法
        UseSet_n = None
        host_Module=None
        useCase_sum = -1
        Use_attribute = None
        """对象实例化"""
        self.actual_result = None  # 用例实际值
        self.expect_result=None    # 用例预期值
        self.old_content=None      # 初始化信息窗口的数据
        self.dict_testCase=None    # 单个测试用例
        self.messageType=None      # 预期值出现的形式（警告弹窗、窗口信息、截图等）
        self.ProjectPath=None      # 项目所在路径
        self.UseCase_Number = None



    """ 执行测试用例步骤 """
    @data(*list_dict_site)  # 参数化参数用例，主要的用于用例的循环测试，并且把测试点放入测试报告
    def test_1(self, testCase):
        global Use_attribute  # 控件属性已经操作方法
        self.actual_result = UseCase_step(Use_attribute, self.dict_testCase).Perform_useCase_Steps()
        self.dict_testCase["实际值"] = self.actual_result  # 实际值放入字典



    """每次执行测试用例前都做的操作"""
    def setUp(self):
        global UseSet_n       # 用例集名称
        global  useCase_sum   # 记录执行用例的总次数，根据次数取出对应的用例
        global  host_Module # 记录主模块（Aerocheck、Fiberbook等）名称
        global Use_attribute  # 控件属性已经操作方法
        useCase_sum = useCase_sum + 1
        # 取出参数
        self.dict_testCase=list_dict_site[useCase_sum]   # 取出单个的测试用例
        self.UseCase_Number = self.dict_testCase["用例编号"]
        tested_Module = self.dict_testCase["模块唯一标识"]
        print("")
        print("\033[5;33m$$$《“%r”模块开始测试，执行用例：%r》\033[0m" % (tested_Module, self.UseCase_Number), __file__, sys._getframe().f_lineno)
        print("")
        print("")
        """ 用例执行前具体的准备工作"""
        dictSet = {"全局用例集名称": UseSet_n,"控件属性已经操作方法": Use_attribute,"全局主模块名称":host_Module,"用例运行总次数":useCase_sum}
        pack_dict = Initializing().controller(dictSet,self.dict_testCase)
        print("控件属性已经操作方法",pack_dict["控件属性已经操作方法"])
        # 取出参数
        UseSet_n=pack_dict["全局子模块名称"]
        host_Module=pack_dict["全局主模块名称"]
        Use_attribute=pack_dict["控件属性已经操作方法"]
        self.dict_testCase["信息窗口之前的文本"]=pack_dict["信息窗口旧的数据"]
        self.dict_testCase["被测程序文件地址"] =pack_dict["项目保存路径"]
        self.dict_testCase["信息窗口最新的日期时间"] = pack_dict["信息窗口最新的日期时间"]
        self.dict_testCase["用例步骤执行前时间"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("\033[0;32;35m{{准备工作准备完毕}}\033[0;32;35m", __file__, sys._getframe().f_lineno)
        print("")
        print("")


    """用例执行完成收尾操作"""
    @BeautifulReport.add_test_img("test_1")   # 如果用例执行失败，就把用例失败的截图放入测试报告中
    def tearDown(self):
        """用例执行完成收尾操作"""
        self.expect_result, self.actual_result = finish_clear().controller(self.dict_testCase)  # 当每条用例执行完毕，执行收尾工作
        """实际值跟预期值对比（文本对比）"""
        print("\033[0;32;33m实际值跟预期值对比\033[0m", __file__, sys._getframe().f_lineno)
        assert_that(self.expect_result).is_equal_to(self.actual_result)  # 断言实际值个预期值
        """ 收尾，如果有警告弹框就关掉"""
        print("\033[0;31m$$$《执行用例“%r”执行结束》$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\033[0m" % self.UseCase_Number)
        print(" ")
        print(" ")
        print(" ")


    """用于测试报告中的截图"""
    def save_img(self, img_name):  # 错误截图
        """
        测试结果如果断言失败，测试报告必须读取该函数
        因为截图已经截取，所有此函数为空函数
        :param img_name:
        :return:
        """
        pass





if __name__ == '__main__':
    unittest.main()


# if __name__ == '__main__':
#     import unittest, time
#     from BeautifulReport import BeautifulReport
#     from config.relative_location import path
#     suite = unittest.TestSuite()
#     # 测试报告名称
#     file_name = time.strftime("%m%d%H%M%S") + "Aerobook测试报告"  # 测试报告名称
#     # 测试报告存放地址
#     relativeAddress = path.location()
#     logPath = relativeAddress + "report//Aerocheck//"  # 测试报告保存地址
#     # 用例名称
#     useCase_name = "Aerocheck测试报告"
#     suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_UseCaseSet_Aerocheck))
#     result = BeautifulReport(suite).report(filename=file_name,log_path=logPath,description=useCase_name)
