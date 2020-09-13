# 铺层库优化工作栏
import unittest,time
from assertpy import assert_that
from BeautifulReport import BeautifulReport
from src.testCase.b_testCaseStep.Aerocheck.TestCaseStep import LaminateOptimize_execute,\
    Laminatedata_execute,sizeInfo_1D2DXlsTemplate_execute,solveCalculation_execute,editWorkingCondition_execute,\
    compositeMaterial,CompoundStrengthCheck,loaddatabase_popUp_execute
from ddt import ddt,data
from src.utils.commonality.ExcelFile import read_excel
from config.relative_location import  path
from src.utils.otherMethods.dataFormatConversion import FormatConversion
from tool import instrument,folderFile_dispose,Check_winControl
from src.utils.otherMethods.actual import Information_Win
from src.utils.otherMethods.initialize import execute_useCase_initialize
from config.configurationFile import ProfileDataProcessing
from tool import WindowTop



"""铺层信息--铺层库优化工作栏测试用例"""
@ddt
@unittest.skip(u"无条件跳过此用例")
class Test_LaminateOptimize(unittest.TestCase):
    """铺层库优化工作栏测试用例"""


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
        global number
        number=1
        actual_result=None
        expect_result=None
        messageType=None
        # 被测系统置顶
        WindowTop.EnumWindows("Aerobook v1.0.4")
        # 获取项目所在路径
        ProjectPath = ProfileDataProcessing("commonality", "ProjectSave_path").config_File()
        # 用例在执行前，首先获取信息窗口的文本信息，用于获取最新的信息窗口文本信息
        old_content = Information_Win().acquire_HTML_TXT(ProjectPath)
        # 用例执行前，初始化测试结果相关的文件
        list_filePath = ["PlyLib_451.xlsx", "PlyLibDb_451.xlsx"]
        folderFile_dispose(ProjectPath).delfile(list_filePath)
        # 在用例执行第一次获取控件操作方法
        # 在用例执行第一次，获取控件属性已经操作方法
        if number==1:
            site1 = {"详细地址": r"src\testCase\c_useCase_file\Aerocheck\铺层信息\自动化铺层库优化.xlsx",
                     "表单名称": "控件属性已经操作方法", "初始行": 1,"初始列": 1}
            testCase_attribute = read_excel(site1).readExcel_ControlProperties()  # 读取测试用例
        number=number+1





    def tearDown(self):
        global ProjectPath  # 项目所在路径
        global old_content  # 在执行用例前信息窗口中的文本信息，用于确定信息窗口中最新的文本
        global messageType  # 预期值信息类型
        global actual_result  # 实际值
        global expect_result  # 预期结果
        global testCase_attribute  # 控件属性方法
        print("测试开始")
        """ 收尾，如果有警告弹框就关掉"""
        Check_winControl("警告", "OK").popUp_Whether_close()
        """取出Excel里面的值"""
        """处理预期结果或实际结果，用以实际结果和预期结果文本对比"""
        if messageType == "信息窗口":    # 如果预期值在信息窗口，就通过以下方法获取最新的信息窗口文本信息
            actual_result = FormatConversion().GetLatestData(actual_result, old_content)
        # 格式化实际值跟预期值
        if type(actual_result) == list:  # 实际值如果是列表，就转化成字符串
            actual_result = ' '.join(actual_result)
        if actual_result:       # 如果实际值不为空
            expect_result = expect_result.strip()   # 去掉预期值，前后的空格
            actual_result  = actual_result.strip()     # 去掉实际值，前后的空格
        """实际值跟预期值对比（文本对比）"""
        assert_that(expect_result).is_equal_to(actual_result)
        print("测试结束")


    # 测试用例Excel文件的相关信息
    site1 = [{"详细地址": r"src\testCase\c_useCase_file\Aerocheck\铺层信息\自动化铺层库优化.xlsx", "表单名称": "最大铺层数", "初始行": 1,"初始列":1},
             {"详细地址": r"src\testCase\c_useCase_file\Aerocheck\铺层信息\自动化铺层库优化.xlsx", "表单名称": "最小铺层数", "初始行": 1,"初始列":1},
             {"详细地址": r"src\testCase\c_useCase_file\Aerocheck\铺层信息\自动化铺层库优化.xlsx", "表单名称": "铺层比", "初始行": 1,"初始列":1},
             {"详细地址": r"src\testCase\c_useCase_file\Aerocheck\铺层信息\自动化铺层库优化.xlsx", "表单名称": "容差比", "初始行": 1,"初始列":1},
             {"详细地址": r"src\testCase\c_useCase_file\Aerocheck\铺层信息\自动化铺层库优化.xlsx", "表单名称": "单层厚度", "初始行": 1,"初始列":1},
             {"详细地址": r"src\testCase\c_useCase_file\Aerocheck\铺层信息\自动化铺层库优化.xlsx", "表单名称": "弹性模量E11(MPa)", "初始行": 1,"初始列":1},
             {"详细地址": r"src\testCase\c_useCase_file\Aerocheck\铺层信息\自动化铺层库优化.xlsx", "表单名称": "弹性模量E22（MPa）", "初始行": 1,"初始列":1},
             {"详细地址": r"src\testCase\c_useCase_file\Aerocheck\铺层信息\自动化铺层库优化.xlsx", "表单名称": "泊松比v12", "初始行": 1,"初始列":1},
             {"详细地址": r"src\testCase\c_useCase_file\Aerocheck\铺层信息\自动化铺层库优化.xlsx", "表单名称": "剪切模量G12（MPa）", "初始行": 1,"初始列":1},
             {"详细地址": r"src\testCase\c_useCase_file\Aerocheck\铺层信息\自动化铺层库优化.xlsx", "表单名称": "层合板长度a(mm)", "初始行": 1,"初始列":1},
             {"详细地址": r"src\testCase\c_useCase_file\Aerocheck\铺层信息\自动化铺层库优化.xlsx", "表单名称": "层合板宽度b(mm)", "初始行": 1,"初始列":1},
             {"详细地址": r"src\testCase\c_useCase_file\Aerocheck\铺层信息\自动化铺层库优化.xlsx", "表单名称": "Mat8材料ID", "初始行": 1,"初始列":1},
             {"详细地址": r"src\testCase\c_useCase_file\Aerocheck\铺层信息\自动化铺层库优化.xlsx", "表单名称": "数据库名称", "初始行": 1,"初始列":1},
             {"详细地址": r"src\testCase\c_useCase_file\Aerocheck\铺层信息\自动化铺层库优化.xlsx", "表单名称": "路径文本框", "初始行": 1,"初始列":1},
             {"详细地址": r"src\testCase\c_useCase_file\Aerocheck\铺层信息\自动化铺层库优化.xlsx", "表单名称": "Mat8材料ID", "初始行": 1,"初始列":1},
             {"详细地址": r"src\testCase\c_useCase_file\Aerocheck\铺层信息\自动化铺层库优化.xlsx", "表单名称": "保存为铺层数据库和保存为Excel勾选框", "初始行": 1,"初始列":1}
             ]
    # site1 =[{"详细地址": r"src\testCase\c_useCase_file\Aerocheck\铺层信息\自动化铺层库优化.xlsx", "表单名称": "最大铺层数", "初始行": 1,"初始列":1}]
    list_dicts=[]
    for site in site1:
        dicts1 = read_excel(site).readExcel_testCase()  # 读取测试用例
        ar_testdicts=FormatConversion().RemoveSubscript(dicts1)
        list_dicts=list_dicts+ar_testdicts
    @data(*list_dicts)    # 参数化参数用例
    def test_1(self,testCase_dict):
        global ProjectPath  # 项目所在路径
        global old_content  # 在执行用例前信息窗口中的文本信息，用于确定信息窗口中最新的文本
        global messageType  # 预期值信息类型
        global actual_result  # 实际值
        global expect_result  # 预期结果
        global testCase_attribute  # 控件属性方法
        """取出Excel里面的值"""
        UseCaseNumber = testCase_dict["用例编号"]
        expect_result = testCase_dict["预期结果文本信息"]  # 取出Excel文件中的预期值
        messageType = testCase_dict["预期值信息类型"]  # 取出提示信息载体类型
        testCase_dict["被测程序文件地址"] = ProjectPath
        print("开始执行用例：", UseCaseNumber)
        """测试用例步骤"""
        actual_result=LaminateOptimize_execute(testCase_attribute,testCase_dict).textbox()  #调用测试步骤


"""铺层信息--铺层数据库制作工具弹窗"""
@ddt
@unittest.skip(u"无条件跳过此用例")
class Test_LaminatedataPopup(unittest.TestCase):
        """铺层信息--铺层数据库制作工具弹窗"""


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
            global number
            number = 1
            actual_result = None
            expect_result = None
            messageType = None
            print("测试开始")
            # 被测系统置顶
            WindowTop.EnumWindows("Aerobook v1.0.4")
            Check_winControl("铺层数据库制作工具", "关闭").popUp_Whether_close()
            # 获取项目所在路径
            ProjectPath = ProfileDataProcessing("commonality", "ProjectSave_path").config_File()
            # 用例在执行前，首先获取信息窗口的文本信息，用于获取最新的信息窗口文本信息
            old_content = Information_Win().acquire_HTML_TXT(ProjectPath)
            # 在用例执行第一次获取控件操作方法
            # 在用例执行第一次，获取控件属性已经操作方法
            if number == 1:
                site1 = {"详细地址": r"src\testCase\c_useCase_file\Aerocheck\铺层信息\自动化铺层库制作工具弹窗.xlsx",
                         "表单名称": "控件属性已经操作方法", "初始行": 1, "初始列": 1}
                testCase_attribute = read_excel(site1).readExcel_ControlProperties()  # 读取测试用例
            number = number + 1



        def tearDown(self):
            """用例执行完后收尾
                           1、首先把复制的文件夹删除
            """
            # 判断选择铺层Excel文件文本框控件是否存在，如果存在向该文本框输入数据
            print("测试结束")
            global ProjectPath  # 项目所在路径
            global old_content  # 在执行用例前信息窗口中的文本信息，用于确定信息窗口中最新的文本
            global messageType  # 预期值信息类型
            global actual_result  # 实际值
            global expect_result  # 预期结果
            global testCase_attribute  # 控件属性方法
            print("测试结束")
            if els:
                # 用例执行前，初始化测试结果相关的文件
                list_filePath = ["plylib.db"]
                folderFile_dispose(ProjectPath).delfile(list_filePath)
            """ 收尾，如果有警告弹框就关掉"""
            Check_winControl("警告", "OK").popUp_Whether_close()
            Check_winControl("铺层数据库制作工具", "关闭").popUp_Whether_close()
            """取出Excel里面的值"""
            """处理预期结果或实际结果，用以实际结果和预期结果文本对比"""
            if messageType == "信息窗口":  # 如果预期值在信息窗口，就通过以下方法获取最新的信息窗口文本信息
                actual_result = FormatConversion().GetLatestData(actual_result, old_content)
            # 格式化实际值跟预期值
            if type(actual_result) == list:  # 实际值如果是列表，就转化成字符串
                actual_result = ' '.join(actual_result)
            if actual_result:  # 如果实际值不为空
                expect_result = expect_result.strip()  # 去掉预期值，前后的空格
                actual_result = actual_result.strip()  # 去掉实际值，前后的空格
            """实际值跟预期值对比（文本对比）"""
            assert_that(expect_result).is_equal_to(actual_result)
            print("测试结束")



        # 测试用例Excel文件的相关信息
        site1 = [{"详细地址": r"src\testCase\c_useCase_file\Aerocheck\铺层信息\自动化铺层库制作工具弹窗.xlsx",
                  "表单名称": "铺层库制作弹窗", "初始行": 1,"初始列":1},
                 {"详细地址": r"src\testCase\c_useCase_file\Aerocheck\铺层信息\自动化铺层库制作工具弹窗.xlsx",
                  "表单名称": "选择铺层Excel文件", "初始行": 1,"初始列":1},
                 {"详细地址": r"src\testCase\c_useCase_file\Aerocheck\铺层信息\自动化铺层库制作工具弹窗.xlsx",
                  "表单名称": "铺层数据保存路径文本框", "初始行": 1,"初始列":1}]
        # site1 =[{"详细地址": r"src\testCase\c_useCase_file\Aerocheck\铺层信息\自动化铺层库制作工具弹窗.xlsx",
        # "表单名称": "测试", "初始行": 1,"初始列":1}]
        list_dicts = []
        if len(site1)>0:
            for site in site1:
                dicts1 = read_excel(site).readExcel_testCase()  # 读取测试用例
                ar_testdicts = FormatConversion().RemoveSubscript(dicts1)
                list_dicts = list_dicts + ar_testdicts
        else:
            list_dicts=site1
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
            print("testCase_dict:",testCase_dict)
            print("testCase_attribute:", testCase_attribute)
            UseCaseNumber = testCase_dict["用例编号"]
            expect_result = testCase_dict["预期结果文本信息"]  # 取出Excel文件中的预期值
            messageType = testCase_dict["预期值信息类型"]  # 取出提示信息载体类型
            els = testCase_dict["其他"]  # 取出提示信息载体类型
            testCase_dict["被测程序文件地址"] = ProjectPath
            print("开始执行用例：", UseCaseNumber)
            """测试用例步骤"""
            actual_result = Laminatedata_execute(testCase_attribute, testCase_dict).SelectFile()  # 调用测试步骤


"""尺寸信息--一维二维单元尺寸定义（模板）"""
@ddt
@unittest.skip(u"无条件跳过此用例")
class Test_sizeInfo_1D2DXls(unittest.TestCase):
        """尺寸信息--一维二维单元尺寸定义（模板）"""

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
            global number
            number = 1
            actual_result = None
            expect_result = None
            messageType = None
            print("开始测试")
            # 被测系统置顶
            WindowTop.EnumWindows("Aerobook v1.0.4")
            # 获取项目所在路径
            ProjectPath = ProfileDataProcessing("commonality", "ProjectSave_path").config_File()
            # 用例在执行前，首先获取信息窗口的文本信息，用于获取最新的信息窗口文本信息
            old_content = Information_Win().acquire_HTML_TXT(ProjectPath)
            # 在用例执行第一次获取控件操作方法F:\Aerobook\src\testCase\c_useCase_file\Aerocheck\尺寸信息\自动化一维二维单元尺寸定义（模板）.xlsx
            # 在用例执行第一次，获取控件属性已经操作方法
            if number == 1:
                site1 = {"详细地址": r"src\testCase\c_useCase_file\Aerocheck\尺寸信息\自动化一维二维单元尺寸定义（模板）.xlsx",
                         "表单名称": "控件属性已经操作方法", "初始行": 1, "初始列": 1}
                testCase_attribute = read_excel(site1).readExcel_ControlProperties()  # 读取测试用例
            number = number + 1


        def tearDown(self):
            global ProjectPath  # 项目所在路径
            global old_content  # 在执行用例前信息窗口中的文本信息，用于确定信息窗口中最新的文本
            global messageType  # 预期值信息类型
            global actual_result  # 实际值
            global expect_result  # 预期结果
            global testCase_attribute  # 控件属性方法
            print("测试结束")
            """ 收尾，如果有警告弹框就关掉"""
            Check_winControl("警告", "OK").popUp_Whether_close()
            """取出Excel里面的值"""
            """处理预期结果或实际结果，用以实际结果和预期结果文本对比"""
            if messageType == "信息窗口":  # 如果预期值在信息窗口，就通过以下方法获取最新的信息窗口文本信息
                actual_result = FormatConversion().GetLatestData(actual_result, old_content)
            # 格式化实际值跟预期值
            if type(actual_result) == list:  # 实际值如果是列表，就转化成字符串
                actual_result = ' '.join(actual_result)
            if actual_result:  # 如果实际值不为空
                expect_result = expect_result.strip()  # 去掉预期值，前后的空格
                actual_result = actual_result.strip()  # 去掉实际值，前后的空格
            """实际值跟预期值对比（文本对比）"""
            assert_that(expect_result).is_equal_to(actual_result)
            print("测试结束")



        # 测试用例Excel文件的相关信息
        # site1 = [{"详细地址": r"src\testCase\c_useCase_file\Aerocheck\尺寸信息\自动化一维二维单元尺寸定义（模板）.xlsx",
        #           "表单名称": "一维单元尺寸定义复合材料（模板）", "初始行": 1,"初始列":1},
        #          {"详细地址": r"src\testCase\c_useCase_file\Aerocheck\尺寸信息\自动化一维二维单元尺寸定义（模板）.xlsx",
        #           "表单名称": "一维单元尺寸定义金属材料（模板）", "初始行": 1,"初始列":1},
        #          {"详细地址": r"src\testCase\c_useCase_file\Aerocheck\尺寸信息\自动化一维二维单元尺寸定义（模板）.xlsx",
        #           "表单名称": "二维单元尺寸定义金属材料（模板）", "初始行": 1, "初始列": 1},
        #          {"详细地址": r"src\testCase\c_useCase_file\Aerocheck\尺寸信息\自动化一维二维单元尺寸定义（模板）.xlsx",
        #           "表单名称": "二维单元尺寸定义金属材料（模板）", "初始行": 1, "初始列": 1}
        #          ]
        site1 =[{"详细地址": r"src\testCase\c_useCase_file\Aerocheck\尺寸信息\自动化一维二维单元尺寸定义（模板）.xlsx",
                          "表单名称": "二维单元尺寸定义金属材料（模板）", "初始行": 1, "初始列": 1}]
        list_dicts = []
        if len(site1)>0:
            for site in site1:
                dicts1 = read_excel(site).readExcel_testCase()  # 读取测试用例
                ar_testdicts = FormatConversion().RemoveSubscript(dicts1)
                list_dicts = list_dicts + ar_testdicts
        else:
            list_dicts=site1
        @data(*list_dicts)  # 参数化参数用例
        # @unittest.skip(u"无条件跳过此用例")
        def test_1(self, testCase_dict):
            """尺寸信息--一维单元尺寸定义（模板）"""
            global ProjectPath  # 项目所在路径
            global old_content  # 在执行用例前信息窗口中的文本信息，用于确定信息窗口中最新的文本
            global messageType  # 预期值信息类型
            global actual_result  # 实际值
            global expect_result  # 预期结果
            global testCase_attribute  # 控件属性方法
            global els  # 控件属性方法
            print("testCase_dict:", testCase_dict)
            print("testCase_attribute:", testCase_attribute)
            UseCaseNumber = testCase_dict["用例编号"]
            expect_result = testCase_dict["预期结果文本信息"]  # 取出Excel文件中的预期值
            messageType = testCase_dict["预期值信息类型"]  # 取出提示信息载体类型
            els = testCase_dict["其他"]  # 取出提示信息载体类型
            testCase_dict["被测程序文件地址"] = ProjectPath
            print("开始执行用例：", UseCaseNumber)
            """测试用例步骤"""
            actual_result = sizeInfo_1D2DXlsTemplate_execute(testCase_attribute, testCase_dict).SelectFile()  # 调用测试步骤


"""求解计算--求解计算"""
@ddt
@unittest.skip(u"无条件跳过此用例")
class Test_solveCalculation(unittest.TestCase):
        """求解计算--求解计算"""

        def setUp(self):
            # 用例执行之前清楚项目文件夹里的部分文件
            global ProjectPath  # 项目所在路径
            global old_content  # 在执行用例前信息窗口中的文本信息，用于确定信息窗口中最新的文本
            global messageType  # 预期值信息类型
            global actual_result  # 实际值
            global expect_result  # 预期结果
            global testCase_attribute  # 控件属性方法
            global number
            number = 1
            actual_result = None
            expect_result = None
            messageType = None
            print("开始测试")
            # 被测系统置顶
            WindowTop.EnumWindows("Aerobook v1.0.4")
            # 获取项目所在路径
            ProjectPath = ProfileDataProcessing("commonality", "ProjectSave_path").config_File()
            # 用例在执行前，首先获取信息窗口的文本信息，用于获取最新的信息窗口文本信息
            old_content = Information_Win().acquire_HTML_TXT(ProjectPath)
            # 在用例执行第一次获取控件操作方法
            # 在用例执行第一次，获取控件属性已经操作方法
            if number == 1:
                site1 = {"详细地址": r"src\testCase\c_useCase_file\Aerocheck\求解计算\自动化求解计算.xlsx",
                         "表单名称": "控件属性已经操作方法", "初始行": 1, "初始列": 1}
                testCase_attribute = read_excel(site1).readExcel_ControlProperties()  # 读取测试用例
            number = number + 1
            # 用例执行前删除部分文件
            list_filePath = ["hwsolver.mesg", "os.bat", "run.vbs", "update_Htail.h3d", "update_Htail.html",
                             "update_Htail.mvw", "update_Htail.out", "update_Htail.pch", "update_Htail.res",
                             "update_Htail.stat", "update_Htail_frames.html", "update_Htail_menu.html"]
            folderFile_dispose(ProjectPath).delfile(list_filePath)


        def tearDown(self):
            """用例执行完后收尾"""
            global ProjectPath  # 项目所在路径
            global old_content  # 在执行用例前信息窗口中的文本信息，用于确定信息窗口中最新的文本
            global messageType  # 预期值信息类型
            global actual_result  # 实际值
            global expect_result  # 预期结果
            global testCase_attribute  # 控件属性方法
            print("测试结束")
            """ 收尾，如果有警告弹框就关掉"""
            Check_winControl("警告", "OK").popUp_Whether_close()
            """取出Excel里面的值"""
            """处理预期结果或实际结果，用以实际结果和预期结果文本对比"""
            if messageType == "信息窗口":  # 如果预期值在信息窗口，就通过以下方法获取最新的信息窗口文本信息
                actual_result = FormatConversion().GetLatestData(actual_result, old_content)
            # 格式化实际值跟预期值
            if type(actual_result) == list:  # 实际值如果是列表，就转化成字符串
                actual_result = ' '.join(actual_result)
            if actual_result:  # 如果实际值不为空
                expect_result = expect_result.strip()  # 去掉预期值，前后的空格
                actual_result = actual_result.strip()  # 去掉实际值，前后的空格
            """实际值跟预期值对比（文本对比）"""
            assert_that(expect_result).is_equal_to(actual_result)
            print("测试结束")


        # 测试用例Excel文件的相关信息
        site1 = [{"详细地址": r"src\testCase\c_useCase_file\Aerocheck\求解计算\自动化求解计算.xlsx",
                  "表单名称": "属性更新选择路径", "初始行": 1,"初始列":1},
                 {"详细地址": r"src\testCase\c_useCase_file\Aerocheck\求解计算\自动化求解计算.xlsx",
                  "表单名称": "载荷提取选择路径", "初始行": 1,"初始列":1}]
        # site1 =[{"详细地址": r"src\testCase\c_useCase_file\Aerocheck\求解计算\自动化求解计算.xlsx","表单名称": "测试", "初始行": 1,"初始列":1}]
        list_dicts = []
        if len(site1)>0:
            for site in site1:
                dicts1 = read_excel(site).readExcel_testCase()  # 读取测试用例
                ar_testdicts = FormatConversion().RemoveSubscript(dicts1)
                list_dicts = list_dicts + ar_testdicts
        else:
            list_dicts=site1
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
            print("testCase_dict:", testCase_dict)
            print("testCase_attribute:", testCase_attribute)
            UseCaseNumber = testCase_dict["用例编号"]
            expect_result = testCase_dict["预期结果文本信息"]  # 取出Excel文件中的预期值
            messageType = testCase_dict["预期值信息类型"]  # 取出提示信息载体类型
            els = testCase_dict["其他"]  # 取出提示信息载体类型
            testCase_dict["被测程序文件地址"] = ProjectPath
            print("开始执行用例：", UseCaseNumber)
            """测试用例步骤"""
            actual_result = solveCalculation_execute(testCase_attribute, testCase_dict).SelectFile()  # 调用测试步骤



"""载荷信息--载荷数据库制作工具弹窗"""
@ddt
@unittest.skip(u"无条件跳过此用例")
class Test_loaddatabase_popUp(unittest.TestCase):
        """载荷信息--载荷数据库制作工具弹窗"""
        global number
        number = 1

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
            global number
            number = 1
            actual_result = None
            expect_result = None
            messageType = None
            print("测试开始")
            # 被测系统置顶
            WindowTop.EnumWindows("Aerobook v1.0.4")
            Check_winControl("铺层数据库制作工具", "关闭").popUp_Whether_close()
            # 获取项目所在路径
            ProjectPath = ProfileDataProcessing("commonality", "ProjectSave_path").config_File()
            # 用例在执行前，首先获取信息窗口的文本信息，用于获取最新的信息窗口文本信息
            old_content = Information_Win().acquire_HTML_TXT(ProjectPath)
            # 在用例执行第一次获取控件操作方法
            # 在用例执行第一次，获取控件属性已经操作方法
            if number == 1:
                site1 = {"详细地址": r"src\testCase\c_useCase_file\Aerocheck\载荷信息\自动化载荷数据库制作工具弹窗.xlsx",
                         "表单名称": "控件属性已经操作方法", "初始行": 1, "初始列": 1}
                testCase_attribute = read_excel(site1).readExcel_ControlProperties()  # 读取测试用例
            number = number + 1


        def tearDown(self):
            """用例执行完后收尾
                           1、首先把复制的文件夹删除
            """
            # 判断选择铺层Excel文件文本框控件是否存在，如果存在向该文本框输入数据
            print("测试结束")
            global ProjectPath  # 项目所在路径
            global old_content  # 在执行用例前信息窗口中的文本信息，用于确定信息窗口中最新的文本
            global messageType  # 预期值信息类型
            global actual_result  # 实际值
            global expect_result  # 预期结果
            global testCase_attribute  # 控件属性方法
            print("测试结束")
            """ 收尾，如果有警告弹框就关掉"""
            Check_winControl("警告", "OK").popUp_Whether_close()
            Check_winControl("载荷数据库制作工具", "关闭").popUp_Whether_close()
            """取出Excel里面的值"""
            """处理预期结果或实际结果，用以实际结果和预期结果文本对比"""
            if messageType == "信息窗口":  # 如果预期值在信息窗口，就通过以下方法获取最新的信息窗口文本信息
                actual_result = FormatConversion().GetLatestData(actual_result, old_content)
            # 格式化实际值跟预期值
            if type(actual_result) == list:  # 实际值如果是列表，就转化成字符串
                actual_result = ' '.join(actual_result)
            if actual_result:  # 如果实际值不为空
                expect_result = expect_result.strip()  # 去掉预期值，前后的空格
                actual_result = actual_result.strip()  # 去掉实际值，前后的空格
            """实际值跟预期值对比（文本对比）"""
            assert_that(expect_result).is_equal_to(actual_result)
            print("测试结束")



        # 测试用例Excel文件的相关信息
        site1 = [{"详细地址": r"src\testCase\c_useCase_file\Aerocheck\载荷信息\自动化载荷数据库制作工具弹窗.xlsx", "表单名称": "载荷数据库制作弹窗", "初始行": 1,"初始列":1},
                 {"详细地址": r"src\testCase\c_useCase_file\Aerocheck\载荷信息\自动化载荷数据库制作工具弹窗.xlsx", "表单名称": "选择载荷文件", "初始行": 1,"初始列":1},
                 {"详细地址": r"src\testCase\c_useCase_file\Aerocheck\载荷信息\自动化载荷数据库制作工具弹窗.xlsx", "表单名称": "载荷数据库保存路径", "初始行": 1,"初始列":1}]
        # site1 =[{"详细地址": r"src\testCase\c_useCase_file\Aerocheck\载荷信息\自动化载荷数据库制作工具弹窗.xlsx", "表单名称": "测试", "初始行": 1,"初始列":1}]
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
        def test_1(self, testCase_dict):
            """载荷信息--载荷数据库制作工具弹窗"""
            global ProjectPath  # 项目所在路径
            global old_content  # 在执行用例前信息窗口中的文本信息，用于确定信息窗口中最新的文本
            global messageType  # 预期值信息类型
            global actual_result  # 实际值
            global expect_result  # 预期结果
            global testCase_attribute  # 控件属性方法
            global els  # 控件属性方法
            print("testCase_dict:", testCase_dict)
            print("testCase_attribute:", testCase_attribute)
            UseCaseNumber = testCase_dict["用例编号"]
            expect_result = testCase_dict["预期结果文本信息"]  # 取出Excel文件中的预期值
            messageType = testCase_dict["预期值信息类型"]  # 取出提示信息载体类型
            els = testCase_dict["其他"]  # 取出提示信息载体类型
            testCase_dict["被测程序文件地址"] = ProjectPath
            print("开始执行用例：", UseCaseNumber)
            """测试用例步骤"""
            actual_result = loaddatabase_popUp_execute(testCase_attribute, testCase_dict).SelectFile()  # 调用测试步骤


"""载荷信息--编辑工况"""
@ddt
@unittest.skip(u"无条件跳过此用例")
class Test_editWorkingCondition(unittest.TestCase):
        """载荷信息--编辑工况"""
        global number
        number = 1

        def setUp(self):
            global ProjectPath  # 项目所在路径
            global old_content  # 在执行用例前信息窗口中的文本信息，用于确定信息窗口中最新的文本
            global messageType  # 预期值信息类型
            global actual_result  # 实际值
            global expect_result  # 预期结果
            global testCase_attribute  # 控件属性方法
            global number
            number = 1
            actual_result = None
            expect_result = None
            messageType = None
            print("测试开始")
            # 被测系统置顶
            WindowTop.EnumWindows("Aerobook v1.0.4")
            # 获取项目所在路径
            ProjectPath = ProfileDataProcessing("commonality", "ProjectSave_path").config_File()
            # 用例在执行前，首先获取信息窗口的文本信息，用于获取最新的信息窗口文本信息
            old_content = Information_Win().acquire_HTML_TXT(ProjectPath)
            # 在用例执行第一次获取控件操作方法
            # 在用例执行第一次，获取控件属性已经操作方法
            Check_winControl("编辑工况", "关闭").popUp_Whether_close()
            if number == 1:
                site1 = {"详细地址": r"src\testCase\c_useCase_file\Aerocheck\载荷信息\自动化编辑工况.xlsx",
                         "表单名称": "控件属性已经操作方法", "初始行": 1, "初始列": 1}
                testCase_attribute = read_excel(site1).readExcel_ControlProperties()  # 读取测试用例
                # 清除所有的包络工况
                execute_useCase_initialize().clear_editWorkingCondition()
            Check_winControl("编辑工况", "关闭").popUp_Whether_close()
            number = number + 1






        def tearDown(self):
            """用例执行完后收尾"""
            global ProjectPath  # 项目所在路径
            global old_content  # 在执行用例前信息窗口中的文本信息，用于确定信息窗口中最新的文本
            global messageType  # 预期值信息类型
            global actual_result  # 实际值
            global expect_result  # 预期结果
            global testCase_attribute  # 控件属性方法
            # 收尾，判断有没有弹窗没有关闭，如果有就关闭
            Check_winControl("警告", "OK").popUp_Whether_close()
            Check_winControl("编辑工况", "关闭").popUp_Whether_close()
            """取出Excel里面的值"""
            """处理预期结果或实际结果，用以实际结果和预期结果文本对比"""
            if messageType == "信息窗口":  # 如果预期值在信息窗口，就通过以下方法获取最新的信息窗口文本信息
                actual_result = FormatConversion().GetLatestData(actual_result, old_content)
            # 格式化实际值跟预期值
            if type(actual_result) == list:  # 实际值如果是列表，就转化成字符串
                actual_result = ' '.join(actual_result)
            if actual_result:  # 如果实际值不为空
                expect_result = expect_result.strip()  # 去掉预期值，前后的空格
                actual_result = actual_result.strip()  # 去掉实际值，前后的空格
            """实际值跟预期值对比（文本对比）"""
            assert_that(expect_result).is_equal_to(actual_result)
            print("测试结束")





        # 测试用例Excel文件的相关信息

        # site1 = [{"详细地址": r"src\testCase\c_useCase_file\Aerocheck\载荷信息\自动化编辑工况.xlsx",
        #           "表单名称": "新建", "初始行": 1,"初始列":1},
        #          {"详细地址":  r"src\testCase\c_useCase_file\Aerocheck\载荷信息\自动化编辑工况.xlsx",
        #           "表单名称": "重命名", "初始行": 1,"初始列":1}]
        site1 =[{"详细地址": r"src\testCase\c_useCase_file\Aerocheck\载荷信息\自动化编辑工况.xlsx","表单名称": "测试", "初始行": 1,"初始列":1}]
        list_dicts = []
        if len(site1)>0:
            for site in site1:
                dicts1 = read_excel(site).readExcel_testCase()  # 读取测试用例
                ar_testdicts = FormatConversion().RemoveSubscript(dicts1)
                list_dicts = list_dicts + ar_testdicts
        else:
            list_dicts=site1
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
            print("testCase_dict:", testCase_dict)
            print("testCase_attribute:", testCase_attribute)
            UseCaseNumber = testCase_dict["用例编号"]
            expect_result = testCase_dict["预期结果文本信息"]  # 取出Excel文件中的预期值
            messageType = testCase_dict["预期值信息类型"]  # 取出提示信息载体类型
            els = testCase_dict["其他"]  # 取出提示信息载体类型
            testCase_dict["被测程序文件地址"] = ProjectPath
            print("开始执行用例：", UseCaseNumber)
            """测试用例步骤"""
            actual_result = editWorkingCondition_execute(testCase_attribute, testCase_dict).SelectFile()  # 调用测试步骤


"""材料信息--定义复合材料参数"""
@ddt
@unittest.skip(u"无条件跳过此用例")
class Test_compositeMaterial(unittest.TestCase):
        """材料信息--定义复合材料参数"""
        global number
        number = 1

        def setUp(self):
            global ProjectPath  # 项目所在路径
            global old_content  # 在执行用例前信息窗口中的文本信息，用于确定信息窗口中最新的文本
            global messageType  # 预期值信息类型
            global actual_result  # 实际值
            global expect_result  # 预期结果
            global testCase_attribute  # 控件属性方法
            global number
            actual_result = None
            expect_result = None
            messageType = None
            print("测试开始")
            # 被测系统置顶
            WindowTop.EnumWindows("Aerobook v1.0.4")
            # 获取项目所在路径
            ProjectPath = ProfileDataProcessing("commonality", "ProjectSave_path").config_File()
            # 用例在执行前，首先获取信息窗口的文本信息，用于获取最新的信息窗口文本信息
            old_content = Information_Win().acquire_HTML_TXT(ProjectPath)
            # 在用例执行第一次获取控件操作方法
            # 在用例执行第一次，获取控件属性已经操作方法
            if number == 1:
                site1 = {"详细地址": r"src\testCase\c_useCase_file\Aerocheck\材料信息\自动化定义许用值.xlsx",
                         "表单名称": "控件属性已经操作方法", "初始行": 1, "初始列": 1}
                testCase_attribute = read_excel(site1).readExcel_ControlProperties()  # 读取测试用例
                # 清除所有的许用值曲线
                execute_useCase_initialize().clear_AllowableCurve()
                print("值执行一次")
            number = number + 1







        def tearDown(self):
            """用例执行完后收尾"""
            global ProjectPath  # 项目所在路径
            global old_content  # 在执行用例前信息窗口中的文本信息，用于确定信息窗口中最新的文本
            global messageType  # 预期值信息类型
            global actual_result  # 实际值
            global expect_result  # 预期结果
            global testCase_attribute  # 控件属性方法
            # 收尾，判断有没有弹窗没有关闭，如果有就关闭
            Check_winControl("警告", "OK").popUp_Whether_close()
            """取出Excel里面的值"""
            """处理预期结果或实际结果，用以实际结果和预期结果文本对比"""
            if messageType == "信息窗口":  # 如果预期值在信息窗口，就通过以下方法获取最新的信息窗口文本信息
                actual_result = FormatConversion().GetLatestData(actual_result, old_content)
            # 格式化实际值跟预期值
            if type(actual_result) == list:  # 实际值如果是列表，就转化成字符串
                actual_result = ' '.join(actual_result)
            if actual_result:  # 如果实际值不为空
                expect_result = expect_result.strip()  # 去掉预期值，前后的空格
                actual_result = actual_result.strip()  # 去掉实际值，前后的空格
            """实际值跟预期值对比（文本对比）"""
            assert_that(expect_result).is_equal_to(actual_result)
            print("测试结束")


        # 测试用例Excel文件的相关信息
        # site1 = [{"详细地址": r"src\testCase\c_useCase_file\Aerocheck\材料信息\自动化定义许用值.xlsx","表单名称": "其他", "初始行": 1,"初始列":1}]
        site1 =[{"详细地址": r"src\testCase\c_useCase_file\Aerocheck\材料信息\自动化定义许用值.xlsx","表单名称": "测试", "初始行": 1,"初始列":1}]
        list_dicts = []
        if len(site1)>0:
            for site in site1:
                dicts1 = read_excel(site).readExcel_testCase()  # 读取测试用例
                ar_testdicts = FormatConversion().RemoveSubscript(dicts1)
                list_dicts = list_dicts + ar_testdicts
        else:
            list_dicts=site1
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
            print("testCase_dict:", testCase_dict)
            print("testCase_attribute:", testCase_attribute)
            UseCaseNumber = testCase_dict["用例编号"]
            expect_result = testCase_dict["预期结果文本信息"]  # 取出Excel文件中的预期值
            messageType = testCase_dict["预期值信息类型"]  # 取出提示信息载体类型
            els = testCase_dict["其他"]  # 取出提示信息载体类型
            testCase_dict["被测程序文件地址"] = ProjectPath
            print("开始执行用例：", UseCaseNumber)
            actual_result= compositeMaterial(testCase_attribute, testCase_dict).SelectFile()  # 调用测试步骤



"""复材结构强度校核--复合材料强度校核"""
@ddt
@unittest.skip(u"无条件跳过此用例")
class Test_CompoundStrengthCheck(unittest.TestCase):
        """复材结构强度校核--复合材料强度校核"""
        global number
        number = 1

        def setUp(self):
            global ProjectPath  # 项目所在路径
            global old_content  # 在执行用例前信息窗口中的文本信息，用于确定信息窗口中最新的文本
            global messageType  # 预期值信息类型
            global actual_result  # 实际值
            global expect_result  # 预期结果
            global testCase_attribute  # 控件属性方法
            global number
            actual_result = None
            expect_result = None
            messageType = None
            print("测试开始")
            # 被测系统置顶
            WindowTop.EnumWindows("Aerobook v1.0.4")
            # 获取项目所在路径
            ProjectPath = ProfileDataProcessing("commonality", "ProjectSave_path").config_File()
            # 用例在执行前，首先获取信息窗口的文本信息，用于获取最新的信息窗口文本信息
            old_content = Information_Win().acquire_HTML_TXT(ProjectPath)
            # 在用例执行第一次获取控件操作方法
            # 在用例执行第一次，获取控件属性已经操作方法
            if number == 1:
                site1 = {"详细地址": r"src\testCase\c_useCase_file\Aerocheck\复材结构强度校核\自动化一维复合材料强度校核.xlsx",
                         "表单名称": "控件属性已经操作方法", "初始行": 1, "初始列": 1}
                testCase_attribute = read_excel(site1).readExcel_ControlProperties()  # 读取测试用例
                print("值执行一次")
            number = number + 1





        def tearDown(self):
            """用例执行完后收尾"""
            global ProjectPath  # 项目所在路径
            global old_content  # 在执行用例前信息窗口中的文本信息，用于确定信息窗口中最新的文本
            global messageType  # 预期值信息类型
            global actual_result  # 实际值
            global expect_result  # 预期结果
            global testCase_attribute  # 控件属性方法
            # 收尾，判断有没有弹窗没有关闭，如果有就关闭
            Check_winControl("警告", "OK").popUp_Whether_close()
            """取出Excel里面的值"""
            """处理预期结果或实际结果，用以实际结果和预期结果文本对比"""
            if messageType == "信息窗口":  # 如果预期值在信息窗口，就通过以下方法获取最新的信息窗口文本信息
                actual_result = FormatConversion().GetLatestData(actual_result, old_content)
            # 格式化实际值跟预期值
            if type(actual_result) == list:  # 实际值如果是列表，就转化成字符串
                actual_result = ' '.join(actual_result)
            if actual_result:  # 如果实际值不为空
                expect_result = expect_result.strip()  # 去掉预期值，前后的空格
                actual_result = actual_result.strip()  # 去掉实际值，前后的空格
            """实际值跟预期值对比（文本对比）"""
            assert_that(expect_result).is_equal_to(actual_result)
            print("测试结束")



        # 测试用例Excel文件的相关信息
        # site1 = [{"详细地址": r"src\testCase\c_useCase_file\Aerocheck\复材结构强度校核\自动化二维复合材料强度校核.xlsx","表单名称": "其他", "初始行": 1}]
        site1 =[{"详细地址": r"src\testCase\c_useCase_file\Aerocheck\复材结构强度校核\自动化二维复合材料强度校核.xlsx","表单名称": "测试", "初始行": 1}]
        list_dicts1 = []
        if len(site1)>0:
            for site in site1:
                dicts1 = read_excel(site).readExcel_testCase()  # 读取测试用例
                ar_testdicts1 = FormatConversion().RemoveSubscript(dicts1)
                list_dicts1 = list_dicts1 + ar_testdicts1
        else:
            list_dicts1=site1

        @unittest.skip(u"无条件跳过此用例")
        @data(*list_dicts1)  # 参数化参数用例
        def test_1(self, testCase_dict):
            """复材结构强度校核--复合材料强度校核"""
            global ProjectPath  # 项目所在路径
            global old_content  # 在执行用例前信息窗口中的文本信息，用于确定信息窗口中最新的文本
            global messageType  # 预期值信息类型
            global actual_result  # 实际值
            global expect_result  # 预期结果
            global testCase_attribute  # 控件属性方法
            global els  # 控件属性方法
            print("testCase_dict:", testCase_dict)
            print("testCase_attribute:", testCase_attribute)
            UseCaseNumber = testCase_dict["用例编号"]
            expect_result = testCase_dict["预期结果文本信息"]  # 取出Excel文件中的预期值
            messageType = testCase_dict["预期值信息类型"]  # 取出提示信息载体类型
            els = testCase_dict["其他"]  # 取出提示信息载体类型
            testCase_dict["被测程序文件地址"] = ProjectPath
            print("开始执行用例：", UseCaseNumber)
            actual_result= CompoundStrengthCheck(testCase_dict).二D_flow_test()  # 调用测试步骤
            print("actual_result:",actual_result)




        # 测试用例Excel文件的相关信息
        # site2 = [{"详细地址": r"src\testCase\c_useCase_file\Aerocheck\复材结构强度校核\自动化一维复合材料强度校核.xlsx","表单名称": "其他", "初始行": 1,"初始列":1}]
        site2 = [
            {"详细地址": r"src\testCase\c_useCase_file\Aerocheck\复材结构强度校核\自动化一维复合材料强度校核.xlsx", "表单名称": "测试", "初始行": 1,"初始列":1}]
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
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test_LaminatedataPopup))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test_sizeInfo_1D2DXls))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test_solveCalculation))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test_editWorkingCondition))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test_compositeMaterial))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test_CompoundStrengthCheck))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test_loaddatabase_popUp))
    file_name=time.strftime("%Y%m%d%H%M%S")+"铺层库优化测试报告"    # 测试报告名称
    relativeAddress = path.location()
    logPath = relativeAddress+"report//Aerocheck//laminateOptimize_testReport//" # 测试报告保存地址
    result = BeautifulReport(suite).report(filename=file_name,log_path=logPath,description="铺层库优化工作栏")
