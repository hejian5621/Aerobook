# 尺寸信息--1D2D尺寸定义
import unittest,time
from assertpy import assert_that
from BeautifulReport import BeautifulReport
from src.testCase.b_testCaseStep.Aerocheck.TestCaseStep import UseCase_step
from ddt import ddt,data
from config.relative_location import  path
from utils.otherMethods.unittest_start_finish import Initializing,finish_clear
from utils.commonality.tool import UseCase_parameterization



"""数据初始化"""
# # 用于控制被测模块的测试，字典的键为模块名称，嵌套的列表为表名称
# list_dicti_argument=[
#     {"铺层信息--铺层库优化":["最大铺层数","最小铺层数","铺层比","容差比","单层厚度","弹性模量E11(MPa)","弹性模量E22（MPa）","泊松比v12","剪切模量G12（MPa）",
#                        "层合板长度a(mm)","层合板宽度b(mm)","Mat8材料ID","数据库名称","路径文本框","Mat8材料ID","保存为铺层数据库和保存为Excel勾选框"]},
#     {"铺层信息--铺层数据库制作工具":["铺层库制作弹窗", "选择铺层Excel文件", "铺层数据保存路径文本框"]},
#     {"尺寸信息--一维单元尺寸定义": ["一维单元尺寸定义截面形状T型"]},
#     {"尺寸信息--二维单元尺寸定义": ["二维单元尺寸定义"]},
#     {"尺寸信息--一维单元尺寸定义（模板）":["铺层库制作弹窗", "选择铺层Excel文件", "铺层数据保存路径文本框"]},
#     {"尺寸信息--二维单元尺寸定义（模板）":["一维单元尺寸定义复合材料（模板）", "一维单元尺寸定义金属材料（模板）", "二维单元尺寸定义金属材料（模板）","二维单元尺寸定义金属材料（模板）"]},
#     {"求解计算--求解计算":["属性更新选择路径",  "载荷提取选择路径"]},
#     {"载荷信息--载荷数据库制作工具": ["载荷数据库制作弹窗", "选择载荷文件","载荷数据库保存路径"]},
#     {"载荷信息--编辑工况": ["新建", "重命名"]},
#     {"材料信息--定义复合材料参数": ["其他"]},
#     {"复材结构强度校核--复合材料强度校核1D": ["其他"]},
#     {"复材结构强度校核--复合材料强度校核2D": ["其他"]},
#     {"紧固件强度校核--紧固件信息输入": ["测试"]},
#     {"紧固件强度校核--紧固件参数设置": ["其他"]},
#     {"紧固件强度校核--紧固件强度校核": ["其他"]},
#     {"紧固件优化--紧固件参数优化": ["其他"]},
#     {"材料信息--定义金属材料参数": ["其他"]},
#     {"金属结构强度校核--金属一维单元强度校核": ["其他"]},
#     {"金属结构强度校核--金属二维单元强度校核": ["其他"]},
#     {"金属结构强度校核--金属加筋板强度校核": ["其他"]}
# ]

# list_dicti_argument=[
#     {"铺层信息--铺层库优化": ["最大铺层数"]},
#     {"铺层信息--铺层数据库制作工具": ["铺层库制作弹窗"]},
#     {"尺寸信息--一维单元尺寸定义": ["一维单元尺寸定义截面形状T型"]},
#     {"尺寸信息--二维单元尺寸定义": ["二维单元尺寸定义"]},
#     {"尺寸信息--一维单元尺寸定义（模板）": ["一维单元尺寸定义复合材料（模板）"]},
#     {"尺寸信息--二维单元尺寸定义（模板）": ["二维单元尺寸定义复合材料（模板）"]},
#     {"求解计算--求解计算": ["属性更新选择路径", "载荷提取选择路径"]},
#     {"载荷信息--载荷数据库制作工具": ["载荷数据库制作弹窗"]},
#     {"载荷信息--编辑工况": ["新建"]},
#     {"材料信息--定义复合材料参数": ["其他"]},
#     {"复材结构强度校核--复合材料强度校核1D": ["其他"]},
#     {"复材结构强度校核--复合材料强度校核2D": ["其他"]},
#     {"紧固件强度校核--紧固件信息输入": ["测试"]},
#     {"紧固件强度校核--紧固件参数设置": ["其他"]},
#     {"紧固件强度校核--紧固件强度校核": ["其他"]},
#     {"紧固件优化--紧固件参数优化": ["其他"]}
#     {"材料信息--定义金属材料参数": ["其他"]}
#     {"金属结构强度校核--金属一维单元强度校核": ["其他"]},
#     {"金属结构强度校核--金属二维单元强度校核": ["其他"]},
#     {"金属结构强度校核--金属加筋板强度校核": ["其他"]}
# ]


list_dicti_argument=[
        {"铺层信息--铺层库优化": ["测试"]},
        {"铺层信息--铺层数据库制作工具": ["铺层库制作弹窗"]}
]

list_dict_site,list_testPoint = UseCase_parameterization().parameterization_data(list_dicti_argument)  # 读取测试用例



"""测试用例集"""
@ddt
# @unittest.skip(u"暂时不执行")
class  test_UseCaseSet(unittest.TestCase):
    """紧固件强度校核--紧固件参数输入"""
    global real_UseCase_Name


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



    def setUp(self):
        """
        每次执行测试用例前都做的操作
        :return:
        """
        global messageType  # 预期值信息类型
        global Use_attribute  # 控件属性方法
        global UseSet_n  # 用例集名称
        global  useCase_sum   # 全局参数，记录执行用例的次数
        global  module_n      # 全局参数，获取执行没一个模块的第一条
        print("测试开始")
        self.dict_testCase=list_dict_site[useCase_sum]   # 取出单个的测试用例
        module_uniqueName = self.dict_testCase["模块唯一标识"]  # 被测模块的唯一标识
        dictSet = {"全局参数": module_n, "全局用例集名称": UseSet_n, "当前用例集名称": module_uniqueName,
                   "控件属性已经操作方法": Use_attribute}
        module_n,UseSet_n, self.ProjectPath, self.old_content, Use_attribute = Initializing().controller(dictSet)
        self.expect_result = self.dict_testCase["预期结果文本信息"]  # 取出Excel文件中的预期值
        self.messageType = self.dict_testCase["预期值信息类型"]  # 取出提示类型
        self.dict_testCase["被测程序文件地址"] = self.ProjectPath
        self.dict_testCase["用例集名称"] = module_uniqueName
        print("开始执行用例：", self.dict_testCase["用例编号"])
        useCase_sum = useCase_sum + 1





    def tearDown(self):
        print("用例执行完成开始执行收尾操作")
        dictSet = {"预期值信息类型": self.messageType, "信息窗口之前的文本": self.old_content, "实际值": self.actual_result,
                   "预期值": self.expect_result}
        self.expect_result, self.actual_result = finish_clear().controller(dictSet)  # 当每条用例执行完毕，执行收尾工作
        print(" ")
        """实际值跟预期值对比（文本对比）"""
        print("实际值跟预期值对比")
        assert_that(self.expect_result).is_equal_to(self.actual_result)  # 预期值跟实际值对比
        print("测试结束")
        print(" ")



    @data(*list_testPoint)  # 参数化参数用例
    def test_1(self, testCase):
        global Use_attribute  # 控件属性方法
        global dict_testCase  # 单个的测试用例
        # 执行测试用例步骤
        self.actual_result = UseCase_step(Use_attribute, self.dict_testCase).Perform_useCase_Steps()





if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_UseCaseSet))
    file_name=time.strftime("%Y%m%d%H%M%S")+"Aerocheck测试报告"    # 测试报告名称
    relativeAddress = path.location()
    logPath = relativeAddress+"report//Aerocheck//laminateOptimize_testReport//" # 测试报告保存地址
    result = BeautifulReport(suite).report(filename=file_name,log_path=logPath,description="铺层库优化工作栏")