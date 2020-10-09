from tool import WindowTop
from config.configurationFile import ProfileDataProcessing
from src.utils.otherMethods.actual import Information_Win
from src.utils.commonality.ExcelFile import read_excel
from tool import folderFile_dispose,Check_winControl
from src.utils.otherMethods.initialize import execute_useCase_initialize
from utils.commonality.tool import UseCase_parameterization
from src.utils.otherMethods.dataFormatConversion import FormatConversion
from tool import pictureProcessing
import os,sys
import time





class Initializing:
    """用例执行前需要做的操作"""

    def __init__(self):
        self.testCase=None


    def controller(self,dictSet,dict_testCase ):
        """
        在执行用例前需要要准备的操作
        dict={"全局参数":"","全局用例集名称":"","当前用例集名称":"","删除文件名列表":[],"详细地址":"","关闭弹窗":[],"控件属性已经操作方法":testCase_attribute}
        :param dictSet:
        :param dict_testCase:
        :return:
        """
        print("\033[0;32;35m《开始进行执行用例前的准备工作》\033[0m", __file__, sys._getframe().f_lineno)
        print("")
        title=ProfileDataProcessing("commonality", "AerobookEdition").config_File()  # 读取配置文件信息
        WindowTop(title).console()    # 把被测系统页面置顶
        number=dictSet["全局参数"]
        global_UseCase_Name = dictSet["全局用例集名称"]
        sole_ModuleIdentifier = dict_testCase["模块唯一标识"]
        self.testCase = dictSet["控件属性已经操作方法"]
        moduleName=dict_testCase["测试模块"]
        # 用例运行前首先检查有没有弹窗没有关闭
        handlingMethod().Loop_closeWindow(global_UseCase_Name,moduleName)
        # 在运行每一个用例集之前初始化全局变量参数
        number,global_Name = handlingMethod().initialize_globalVariable(number, global_UseCase_Name, sole_ModuleIdentifier)
        # 获取项目所在路径
        ProjectPath = ProfileDataProcessing("commonality", "ProjectSave_path").config_File()
        # 用例在执行前，首先获取信息窗口的文本信息，用于获取最新的信息窗口文本信息
        old_content = Information_Win().acquire_HTML_TXT(ProjectPath)
        # 用例运行前删除指定的文件
        folderFile_dispose(ProjectPath).delfile(dict_testCase)
        if number == 1:  # 在执行该模块第一条用例前执行下面操作
            # 取出“控件属性已经操作方法”
            tableName=["控件属性已经操作方法"]
            site = UseCase_parameterization().parameterization_location(moduleName,sole_ModuleIdentifier, tableName)
            self.testCase = read_excel(site[0]).readExcel_ControlProperties()  # 读取该测试用例中控件的操作属性
            print("\033[0;32;34m获取到的Excel文档中控件属性和操作方法：\033[0m",self.testCase, __file__, sys._getframe().f_lineno)
            print(" ")
            # 在模块开始前数据清理
            if sole_ModuleIdentifier=="载荷信息--编辑工况":
                print("\033[0;32;34m清除包络工况：\033[0m", self.testCase, __file__, sys._getframe().f_lineno)
                print(" ")
                execute_useCase_initialize().clear_editWorkingCondition()    # 清除所有的包络工况
        print("\033[0;32;35m{{准备工作准备完毕}}\033[0;32;35m", __file__, sys._getframe().f_lineno)
        print("")
        print(" ")
        return number,global_Name,ProjectPath,old_content,self.testCase



class finish_clear:
    """结束清理"""

    def controller(self, dictSet):
        """
        用例步骤操作结束后
        准备如果测试失败后的截图
        关闭所有在用例执行中出现的的弹窗
        统一格式预期值和实际值
        :param dictSet:字典类型的数据集
        :return: 返回格式规范化的实际值和预期值
        """
        print("\033[0;32;35m《开始进行用例的收尾工作》\033[0m", __file__, sys._getframe().f_lineno)
        print("")
        actual_result = dictSet["实际值"]
        sole_ModuleIdentifier = dictSet["模块唯一标识"]
        moduleName=dictSet["测试模块"]
        """在关闭弹窗前首先截图，用于如果断言失败后，在测试报告上显示测试失败的截图"""
        actuals = pictureProcessing(None).BeingMeasured_system_screenshot()
        """ 收尾，如果有警告弹框就关掉"""
        handlingMethod().Loop_closeWindow(sole_ModuleIdentifier,moduleName)
        """处理预期结果和实际结果，用以实际结果和预期结果文本对比"""
        print("\033[0;34m格式化实际值和预期值\033[0m", __file__, sys._getframe().f_lineno)
        print("")
        expect_result,location = FormatConversion().expect_dataProcessing(dictSet, actual_result)  # 格式化实际值
        print("\033[0;34m预期值：\033[0m", expect_result)
        actual_result = FormatConversion().Actual_dataProcessing(dictSet,actual_result,location)  # 格式化实际值
        print("\033[0;34m实际值：\033[0m", actual_result)
        print("")
        print("\033[0;32;35m用例收尾工作完成\033[5;33m", __file__, sys._getframe().f_lineno)
        print("")
        print(" ")
        return  expect_result,actual_result





class handlingMethod:



    def __init__(self):
        self.list_CloseWindows=None


    def initialize_globalVariable(self, reset_arg, global_UseCase_Name, real_UseCase_Name):
        """
        在每一次运行用例集之前都初始化一次全局变量
        :param reset_arg: 需要初始化得参数
        :param global_UseCase_Name: 全局变量的用例集名称
        :param real_UseCase_Name:  正在执行用例集的用例集名称
        :return:
        """
        if global_UseCase_Name == real_UseCase_Name:
            real_arg = reset_arg + 1
        else:
            global_UseCase_Name = real_UseCase_Name
            real_arg = 1
        print("\033[0;32;34m初始化全局变量，全局变量参数：%r，全局变量模块名称：%r\033[0m" % (real_arg, global_UseCase_Name), __file__, sys._getframe().f_lineno)
        print("")
        return real_arg, global_UseCase_Name


    def Loop_closeWindow(self,sole_ModuleIdentifier,moduleName):
        """
        循环关闭窗口
        根据被测模块，检查特定模块的特定窗口
        :return:
        """
        site = {"详细地址": r"src\testCase\c_useCase_file\Aerocheck\initialize\自动化测试公共属性.xlsx", "表单名称": moduleName,
                 "初始行": 1,"初始列":1}
        dicts_title = read_excel(site).readExcel_common()  # 从Excel表格中取出要关闭窗口的标题
        # 根据模块名称取出对应模块应该检查的弹窗标题
        if sole_ModuleIdentifier in dicts_title:
            CloseWindows=dicts_title[sole_ModuleIdentifier]
            if "；" in CloseWindows:    # 如果字典的值里有“；”，就转化成列表
                self.list_CloseWindows = CloseWindows.split("；")
            else:  # 如果字典的值里没有“；”，就强行转化成列表
                self.list_CloseWindows.append(CloseWindows)
            print("\033[0;32;34m检查%r模块，弹窗是否关闭,需要检查的弹窗标题：%r\033[0m" % (sole_ModuleIdentifier, self.list_CloseWindows), __file__, sys._getframe().f_lineno)
            for title in self.list_CloseWindows:  # 依次取出预期关闭的弹窗的标题
                Check_winControl(title).Force_close_popUp()  # 关闭弹窗
        else:
            if "全部模块" in  dicts_title:  # 如果没有找到对应模块的关闭窗口，就全部找一遍
                CloseWindows = dicts_title["全部模块"]
                if "；" in CloseWindows:  # 如果字典的值里有“；”，就转化成列表
                    self.list_CloseWindows = CloseWindows.split("；")
                else:  # 如果字典的值里没有“；”，就强行转化成列表
                    self.list_CloseWindows.append(CloseWindows)
                print("\033[0;32;34m因为该被测模块名没有找到对应关闭窗口的名称，所以全部关闭一遍，被测模块名称：%r\033[0m" % sole_ModuleIdentifier, __file__, sys._getframe().f_lineno)
                for title in self.list_CloseWindows:  # 依次取出预期关闭的弹窗的标题
                    Check_winControl(title).Force_close_popUp()  # 关闭弹窗
        print("\033[0;32;34m%r模块弹窗检查完毕\033[0m" % sole_ModuleIdentifier, __file__, sys._getframe().f_lineno)
        print("")




