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
        WindowTop("Aerobook v1.0.4").console()    # 把被测系统页面置顶
        number=dictSet["全局参数"]
        global_UseCase_Name = dictSet["全局用例集名称"]
        sole_ModuleIdentifier = dict_testCase["模块唯一标识"]
        self.testCase = dictSet["控件属性已经操作方法"]
        # 用例运行前首先检查有没有弹窗没有关闭
        handlingMethod().Loop_closeWindow(sole_ModuleIdentifier)
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
            site = UseCase_parameterization().parameterization_location(sole_ModuleIdentifier, tableName)
            self.testCase = read_excel(site[0]).readExcel_ControlProperties()  # 读取该测试用例中控件的操作属性
            # 在模块开始前数据清理
            if sole_ModuleIdentifier=="载荷信息--编辑工况":
                execute_useCase_initialize().clear_editWorkingCondition()    # 清除所有的包络工况
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
        actual_result = dictSet["实际值"]
        sole_ModuleIdentifier = dictSet["模块唯一标识"]
        """在关闭弹窗前首先截图，用于如果断言失败后，在测试报告上显示测试失败的截图"""
        actuals = pictureProcessing(None). BeingMeasured_system_screenshot()
        """ 收尾，如果有警告弹框就关掉"""
        handlingMethod().Loop_closeWindow(sole_ModuleIdentifier)
        """处理预期结果和实际结果，用以实际结果和预期结果文本对比"""
        expect_result,location = FormatConversion().expect_dataProcessing(dictSet, actual_result)  # 格式化实际值
        print("预期值：", expect_result)
        actual_result = FormatConversion().Actual_dataProcessing(dictSet,actual_result,location)  # 格式化实际值
        print("实际值：", actual_result)
        return  expect_result,actual_result





class handlingMethod:



    def __init__(self):
        pass

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
        return real_arg, global_UseCase_Name


    def Loop_closeWindow(self,sole_ModuleIdentifier):
        """
        循环关闭窗口
        根据被测模块，检查特定模块的特定窗口
        :return:
        """
        list_CloseWindows=None
        if sole_ModuleIdentifier=="铺层信息--铺层库优化":
            list_CloseWindows = [["警告"],["选择输出路径"]]
        elif sole_ModuleIdentifier=="铺层信息--铺层数据库制作工具":
            list_CloseWindows = [["警告"], ["选择Excel铺层文件"], ["选择铺层数据库保存路径"],["确认另存为"],
                                 ["铺层数据库制作工具"]]
        elif sole_ModuleIdentifier == "尺寸信息--一维单元尺寸定义":
            list_CloseWindows = [["警告"],["选择铺层库信息"]]
        elif sole_ModuleIdentifier == "尺寸信息--二维单元尺寸定义":
            list_CloseWindows = [["警告"],["选择铺层库信息"]]
        elif sole_ModuleIdentifier == "尺寸信息--一维单元尺寸定义（模板）":
            list_CloseWindows = [["警告"], ["指定Excel模板文件路径"]]
        elif sole_ModuleIdentifier == "尺寸信息--二维单元尺寸定义（模板）":
            list_CloseWindows = [["警告"], ["指定Excel模板文件路径"]]
        elif sole_ModuleIdentifier == "求解计算--求解计算":
            list_CloseWindows = [["警告"], ["指定bdf文件保存路径"], ["指定载荷数据库保存路径"]]
        elif sole_ModuleIdentifier == "载荷信息--载荷数据库制作工具":
            list_CloseWindows = [["警告"], ["选择f06文件"], ["选择载荷数据库保存路径"],["确认另存为"],
                                 ["载荷数据库制作工具"]]
        elif sole_ModuleIdentifier == "载荷信息--编辑工况":
            list_CloseWindows = [["警告"], ["编辑工况"]]
        elif sole_ModuleIdentifier == "材料信息--定义复合材料参数":
            list_CloseWindows = [["警告", "OK"], ["选择材料许用值曲线", "关闭"], ["编辑材料许用值曲线", "关闭"]]
        elif sole_ModuleIdentifier == "材料信息--定义金属材料参数":
            list_CloseWindows = [["警告", "OK"]]
        elif sole_ModuleIdentifier == "复材结构强度校核--复合材料强度校核1D":
            list_CloseWindows = [["警告", "OK"], ["选择校核工况", "关闭"]]
        elif sole_ModuleIdentifier == "复材结构强度校核--复合材料强度校核2D":
            list_CloseWindows = [["警告", "OK"], ["选择校核工况", "关闭"]]
        elif sole_ModuleIdentifier == "紧固件强度校核--紧固件信息输入":
            list_CloseWindows = [["警告", "OK"]]
        elif sole_ModuleIdentifier == "紧固件强度校核--紧固件参数设置":
            list_CloseWindows = [["警告", "OK"], ["选择连接件参数Excel文件", "打开"]]
        elif sole_ModuleIdentifier == "紧固件强度校核--紧固件强度校核":
            list_CloseWindows = [["警告", "OK"], ["选择优化工况", "关闭"]]
        elif sole_ModuleIdentifier == "紧固件优化--紧固件参数优化":
            list_CloseWindows = [["警告", "OK"], ["选择优化工况", "关闭"],["错误"]]
        elif sole_ModuleIdentifier == "金属结构强度校核--金属一维单元强度校核":
            list_CloseWindows = [["警告", "OK"], ["选择校核工况", "关闭"]]
        elif sole_ModuleIdentifier == "金属结构强度校核--金属二维单元强度校核":
            list_CloseWindows = [["警告", "OK"], ["选择校核工况", "关闭"]]
        elif sole_ModuleIdentifier == "金属结构强度校核--金属加筋板强度校核":
            list_CloseWindows = [["警告", "OK"], ["选择校核工况", "关闭"]]
        elif sole_ModuleIdentifier == "金属结构强度校核--金属曲板后驱曲强度校核":
            list_CloseWindows = [["警告", "OK"], ["选择校核工况", "关闭"]]
        else:
            list_CloseWindows = [["警告", "OK"], ["选择校核工况", "关闭"]]
        for CloseWindows in list_CloseWindows:
            title = CloseWindows[0]
            Check_winControl(title).Force_close_popUp()



