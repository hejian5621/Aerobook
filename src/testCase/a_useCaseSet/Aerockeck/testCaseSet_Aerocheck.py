# 尺寸信息--1D2D尺寸定义
import unittest,time,datetime
from assertpy import assert_that
from BeautifulReport import BeautifulReport
from src.testCase.b_testCaseStep.Aerocheck.TestCaseStep import UseCase_step
from ddt import ddt,data
from tool import Check_winControl
from utils.otherMethods.unittest_start_finish import Initializing,finish_clear
from utils.otherMethods.Get_TestCase import getTestCase

# 获取测试用例
moduleName="Aerocheck"  # 测试模块
list_dict_site,list_testPoint = getTestCase(moduleName).console()  # 获取测试用例
# 检查系统是否正在被测模块，如果不在，就点击进入
Check_winControl(moduleName).examine_LocatedModule()



"""测试用例集"""
@ddt
# @unittest.skip(u"暂时不执行")
class  test_UseCaseSet_Aerocheck(unittest.TestCase):
    """测试用例集"""


    def __init__(self, *args):
        unittest.TestCase.__init__(self, *args)
        global UseSet_n       # 用例集名称
        global useCase_sum    # 记录执行用例的次数，根据次数取出对应的用例
        global module_n       # 获取执行每一个模块的第一条
        global Use_attribute  # 操作控件的属性方法
        UseSet_n = None
        Use_attribute = None
        useCase_sum = 0
        module_n = 1
        self.actual_result = None  # 用例实际值
        self.expect_result=None    # 用例预期值
        self.old_content=None      # 初始化信息窗口的数据
        self.dict_testCase=None    # 单个测试用例
        self.messageType=None      # 预期值出现的形式（警告弹窗、窗口信息、截图等）
        self.ProjectPath=None      # 项目所在路径
        self.UseCase_Number = None


    """ 执行测试用例步骤 """
    @data(*list_testPoint)  # 参数化参数用例，主要的用于用例的循环测试，并且把测试点放入测试报告
    def test_1(self, testCase):
        global Use_attribute  # 控件属性方法
        self.actual_result = UseCase_step(Use_attribute, self.dict_testCase).Perform_useCase_Steps()
        self.dict_testCase["实际值"] = self.actual_result  # 实际值放入字典



    """每次执行测试用例前都做的操作"""
    def setUp(self):
        """
        每次执行测试用例前都做的操作
        :return:
        """
        global Use_attribute  # 控件属性方法
        global UseSet_n  # 用例集名称
        global  useCase_sum   # 全局参数，记录执行用例的次数
        global  module_n      # 全局参数，获取执行没一个模块的第一条
        global UseCase_Number

        self.dict_testCase=list_dict_site[useCase_sum]   # 取出单个的测试用例
        print("moduleName:",moduleName)
        self.dict_testCase["测试模块"]=moduleName
        dictSet = {"全局参数": module_n, "全局用例集名称": UseSet_n,"控件属性已经操作方法": Use_attribute}
        module_n,UseSet_n, self.ProjectPath, self.old_content, Use_attribute = Initializing().controller(dictSet,self.dict_testCase)
        self.dict_testCase["信息窗口之前的文本"]=self.old_content
        self.dict_testCase["被测程序文件地址"] = self.ProjectPath
        self.dict_testCase["用例步骤执行前时间"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        UseCase_Number=self.dict_testCase["用例编号"]
        tested_Module = self.dict_testCase["模块唯一标识"]
        print("\047[1;33m $$$《模块“%r”开始测试，执行用例：%r》$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\047[0m"%(tested_Module,UseCase_Number))
        useCase_sum = useCase_sum + 1


    """用例执行完成收尾操作"""
    @BeautifulReport.add_test_img("test_1")   # 如果用例执行失败，就把用例失败的截图放入测试报告中
    def tearDown(self):
        """用例执行完成收尾操作"""
        global UseCase_Number
        print("用例执行完成开始执行收尾操作")
        print("1111")
        self.expect_result, self.actual_result = finish_clear().controller(self.dict_testCase)  # 当每条用例执行完毕，执行收尾工作
        """实际值跟预期值对比（文本对比）"""
        print("实际值跟预期值对比")
        assert_that(self.expect_result).is_equal_to(self.actual_result)  # 断言实际值个预期值
        """ 收尾，如果有警告弹框就关掉"""
        print("\047[1;33m $$$《执行用例“%r”执行结束》$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\047[0m"%UseCase_Number)
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
