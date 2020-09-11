# 用例步骤
from src.utils.otherMethods.initialize import pywin_openAProgram,execute_useCase_initialize
from OperatingControls.enterModule import BeingMeasured_popupWin,BeingMeasured_work,specialWay_OperatingControls
from src.utils.OperatingControls.moduleControlOperation import ModuleControlOperation
from src.utils.otherMethods.actual import Warning_PopUp,GetActual_Value
from src.utils.otherMethods.actual import Information_Win
from src.utils.OperatingControls.moduleControlOperation import OperatingControls
import time
import sys, os


class LaminateOptimize_execute:
    """测试用例执行步骤"""

    def __init__(self,testCase_attribute,testCase_dict):
        self.testCase_attribute = testCase_attribute  # 字典类型嵌套字典类型的控件属性方法
        self.testCase_dict = testCase_dict  # 字典类型测试用例
        self.Message_type = testCase_dict["预期值信息类型"]
        self.ProjectPath = testCase_dict["被测程序文件地址"]
        self.UseCase_Number = self.testCase_dict["用例编号"]  # 取出预期值
        self.actual_Text = None


    def textbox(self):
        """
        文本框测试
        :return:
        """
        # 连接到被测程序，并且通过菜单栏打开被测模块
        aero_window, son_window = pywin_openAProgram().menuOpen(self.testCase_dict)
        # 通过操作菜单栏，打开被测模块，然后切换到被测模块
        module_window=BeingMeasured_work(son_window).workField_general()
        # 向被测模块输入数据
        OperatingControls(module_window).controlConsole(self.testCase_attribute,self.testCase_dict)
        # 获取实际值
        self.actual_Text = GetActual_Value(self.testCase_dict).ActualValue_controller()
        return self.actual_Text


class Laminatedata_execute:
    """铺层数据库工具弹窗"""

    def __init__(self,testCase_attribute,testCase_dict):
        self.testCase_attribute = testCase_attribute  # 字典类型嵌套字典类型的控件属性方法
        self.testCase_dict = testCase_dict  # 字典类型测试用例
        self.Message_type = testCase_dict["预期值信息类型"]
        self.ProjectPath = testCase_dict["被测程序文件地址"]
        self.UseCase_Number = self.testCase_dict["用例编号"]  # 取出预期值
        self.actual_Text = None


    def SelectFile(self):
        """
        铺层数据库工具弹窗，选择文件文本框
        :return:
        """

        pywin_openAProgram().menuOpen(self.testCase_dict)
        # 切入铺层数据库工具弹窗中
        module_window = BeingMeasured_popupWin("铺层数据库制作工具").menu_LetsGoTopopover()
        # 切入铺层数据库工具弹窗中控件中
        general_window,special_window_one = BeingMeasured_popupWin(None).Laminatedata_popUp(module_window)
        # 向被测模块输入数据
        OperatingControls(general_window,special_window_one,module_window).\
            controlConsole(self.testCase_attribute, self.testCase_dict)
        # 获取实际值
        self.actual_Text = GetActual_Value(self.testCase_dict).ActualValue_controller()
        return self.actual_Text


class sizeInfo_1D2DXlsTemplate_execute:
    """尺寸信息--1D单元尺寸定义（模板）"""

    def __init__(self, testCase_attribute, testCase_dict):
        self.testCase_attribute = testCase_attribute  # 字典类型嵌套字典类型的控件属性方法
        self.testCase_dict = testCase_dict  # 字典类型测试用例
        self.Message_type = testCase_dict["预期值信息类型"]
        self.ProjectPath = testCase_dict["被测程序文件地址"]
        self.UseCase_Number = testCase_dict["用例编号"]  # 取出预期值
        self.results_waitTime = testCase_dict["测试结果等到时间"]  # 取出预期值
        self.actual_Text = None



    def SelectFile(self):
        """
        选择文件文本框
        :return:
        """
        # 连接到被测程序，并且通过菜单栏打开被测模块
        aero_window, son_window = pywin_openAProgram().menuOpen(self.testCase_dict)
        # 通过操作菜单栏，打开被测模块，然后切换到被测模块
        module_window = BeingMeasured_work(son_window).workField_sizeInfo()
        # 向被测模块输入数据
        OperatingControls(module_window).controlConsole(self.testCase_attribute, self.testCase_dict)
        # 获取实际值
        time.sleep(self.results_waitTime)
        self.actual_Text = GetActual_Value(self.testCase_dict).ActualValue_controller()
        return self.actual_Text


"""求解计算"""
class solveCalculation_execute:
    """求解计算"""

    def __init__(self, testCase_attribute, testCase_dict):
        self.testCase_attribute = testCase_attribute  # 字典类型嵌套字典类型的控件属性方法
        self.testCase_dict = testCase_dict  # 字典类型测试用例
        self.Message_type = testCase_dict["预期值信息类型"]
        self.ProjectPath = testCase_dict["被测程序文件地址"]
        self.UseCase_Number = testCase_dict["用例编号"]  # 取出预期值
        self.results_waitTime = testCase_dict["测试结果等到时间"]  # 取出预期值
        self.actual_Text = None

    def SelectFile(self):
        """
        选择文件文本框
        :return:
        """
        # 连接到被测程序，并且通过菜单栏打开被测模块
        aero_window, son_window = pywin_openAProgram().menuOpen(self.testCase_dict)
        # 通过操作菜单栏，打开被测模块，然后切换到被测模块
        module_window = BeingMeasured_work(son_window).workField_general()
        # 向被测模块输入数据
        OperatingControls(module_window).controlConsole(self.testCase_attribute, self.testCase_dict)
        # 获取实际值
        time.sleep(self.results_waitTime)
        self.actual_Text = GetActual_Value(self.testCase_dict).ActualValue_controller()
        return self.actual_Text

"""载荷数据库工具弹窗"""
class loaddatabase_popUp_execute:
    """载荷数据库工具弹窗"""

    def __init__(self, testCase_attribute, testCase_dict):
        self.testCase_attribute = testCase_attribute  # 字典类型嵌套字典类型的控件属性方法
        self.testCase_dict = testCase_dict  # 字典类型测试用例
        self.Message_type = testCase_dict["预期值信息类型"]
        self.ProjectPath = testCase_dict["被测程序文件地址"]
        self.UseCase_Number = self.testCase_dict["用例编号"]  # 取出预期值
        self.actual_Text = None

    def SelectFile(self):
        """
        铺层数据库工具弹窗，选择文件文本框
        :return:
        """

        pywin_openAProgram().menuOpen(self.testCase_dict)
        # 切入铺层数据库工具弹窗中
        module_window = BeingMeasured_popupWin("载荷数据库制作工具").menu_LetsGoTopopover()
        # 切入铺层数据库工具弹窗中控件中
        general_window, special_window_one = BeingMeasured_popupWin(None).Laminatedata_popUp(module_window)
        # 向被测模块输入数据
        OperatingControls(general_window, special_window_one, module_window). \
            controlConsole(self.testCase_attribute, self.testCase_dict)
        # 获取实际值
        self.actual_Text = GetActual_Value(self.testCase_dict).ActualValue_controller()
        return self.actual_Text


"""编辑工况"""
class editWorkingCondition_execute:
    """编辑工况"""

    def __init__(self, testCase_attribute, testCase_dict):
        self.testCase_attribute = testCase_attribute  # 字典类型嵌套字典类型的控件属性方法
        self.testCase_dict = testCase_dict  # 字典类型测试用例
        self.Message_type = testCase_dict["预期值信息类型"]
        self.ProjectPath = testCase_dict["被测程序文件地址"]
        self.UseCase_Number = testCase_dict["用例编号"]  # 取出预期值
        self.results_waitTime = testCase_dict["测试结果等到时间"]  # 取出预期值
        self.actual_Text = None


    def SelectFile(self):
        """
        选择文件文本框
        :return:
        """
        # 连接到被测程序，并且通过菜单栏打开被测模块
        pywin_openAProgram().menuOpen(self.testCase_dict)
        # 通过操作菜单栏，打开被测模块，然后切换到被测模块
        module_window = BeingMeasured_popupWin("编辑工况").menu_LetsGoTopopover()
        # 向被测模块输入数据
        OperatingControls(module_window).controlConsole(self.testCase_attribute, self.testCase_dict)
        # 获取实际值
        time.sleep(self.results_waitTime)
        example = module_window.ComboBox
        self.actual_Text = GetActual_Value(self.testCase_dict,example).ActualValue_controller()
        return self.actual_Text


"""材料信息--定义复合材料参数"""
class compositeMaterial:
    """材料信息--定义复合材料参数"""

    def __init__(self, testCase_attribute, testCase_dict):
        self.testCase_attribute = testCase_attribute  # 字典类型嵌套字典类型的控件属性方法
        self.testCase_dict = testCase_dict  # 字典类型测试用例
        self.Message_type = testCase_dict["预期值信息类型"]
        self.ProjectPath = testCase_dict["被测程序文件地址"]
        self.UseCase_Number = testCase_dict["用例编号"]  # 取出预期值
        self.results_waitTime = testCase_dict["测试结果等到时间"]  # 取出预期值
        self.initialLevel = testCase_dict["初始化级别"]
        self.operationWindow = testCase_dict["操作窗口标题"]
        self.operationWindow_son = testCase_dict["操作子窗口标题"]
        self.actual_Text = None
        self.aero_window = None
        self.son_window = None
        self.module_window = None


    def SelectFile(self):
        """
        选择文件文本框
        :return:
        """
        # 执行步骤之前初始化
        if self.initialLevel == "整个被测模块":  # 点击菜单栏进入被测模板，并且通过UIA框架切换窗口，针对工作栏
            self.aero_window, self.son_window = pywin_openAProgram().menuOpen_switchingWin_UIA(self.testCase_dict,self.operationWindow)
        elif self.initialLevel == "编辑材料许用值弹窗" or self.initialLevel == "定义材料许用值":  # 初始化编辑材料许用值和定义材料许用值
            self.son_window = execute_useCase_initialize().link_window()  # 链接被测程序
        else:
            print("在执行用例步骤前不知道程序初始化级别", __file__, sys._getframe().f_lineno)
            os._exit(0)
        # 切换到材料信息--定义复合材料信息--编辑材料许用值、定义材料许用值模块
        self.module_window = BeingMeasured_work(self.son_window).workField_composite_information() #
        #  操作步骤
        if self.operationWindow_son =="编辑材料许用值曲线弹窗":
            # 打开“编辑材料许用值曲线弹窗”弹框
            ModuleControlOperation(self.module_window).editAllowable_operation(self.testCase_dict)
            # 切换到“编辑材料许用值曲线弹窗”中
            dlg1_spec = BeingMeasured_popupWin("编辑材料许用值曲线").menu_LetsGoTopopover()
            #  切换到网格窗口
            dlg2_spec = dlg1_spec.child_window(title="GridWindow", class_name="wxWindowNR")
            # 向被测模块输入数据
            OperatingControls(dlg1_spec,dlg2_spec).controlConsole(self.testCase_attribute, self.testCase_dict)
        elif self.operationWindow_son =="定义材料许用值":
            # 操作“定义材料许用值”工作栏
            OperatingControls(self.module_window).controlConsole(self.testCase_attribute, self.testCase_dict)
        # 获取实际值
        time.sleep(self.results_waitTime)
        example = self.module_window.ComboBox
        self.actual_Text = GetActual_Value(self.testCase_dict,example).ActualValue_controller()
        return self.actual_Text







class CompoundStrengthCheck:
    """材料信息--定义复合材料参数"""

    def __init__(self, testdicts):
        self.testdicts = testdicts
        self.inModule = testdicts["所在模块"]
        self.Message_type = testdicts["预期值信息类型"]
        self.source = testdicts["被测程序文件地址"]
        self.initialLevel = testdicts["初始化级别"]
        self.operationWindow = testdicts["操作窗口"]
        self.operationWindow_son = testdicts["操作子窗口"]
        self.edit_list = None
        self.actual_Text = ""
        self.module_window =None
        self.aero_window = None
        self.son_window = None
        self.work_window=None




    def 二D_flow_test(self):
        """
        选择文件文本框
        :return:
        """
        # 执行步骤之前初始化
        if self.initialLevel == "整个工作栏":  # 初始化这个工作栏，或者弹窗，返回对象实体
            self.aero_window, self.son_window = pywin_openAProgram().menuOpen(self.testdicts)
            specialWay_OperatingControls(self.operationWindow_son).uia_OperatingControls()
            self.module_window, self.work_window = BeingMeasured_work(self.son_window).workField_intensityCheck()
        else:
            import sys, os
            print("在执行用例步骤前不知道程序初始化级别", __file__, sys._getframe().f_lineno)
            os._exit(0)
        #  操作步骤
        ModuleControlOperation(self.module_window).CompoundStrengthCheck_2D_operation(self.testdicts,self.work_window)
        # 获取实际值
        if self.Message_type == "警告弹窗":
            UseCase_Number = self.testdicts["用例编号"]  # 取出预期值
            self.actual_Text = Warning_PopUp(self.aero_window).Warning_PopUp_TXT(UseCase_Number)
        elif self.Message_type == "信息窗口":
            self.actual_Text = Information_Win().acquire_HTML_TXT(self.source)
        else:
            print("没有获取实际的文本测试结果")
        return self.actual_Text



    def 一D_flow_test(self):
        """
        选择文件文本框
        :return:
        """
        # 执行步骤之前初始化
        if self.initialLevel == "整个工作栏":  # 初始化这个工作栏，或者弹窗，返回对象实体
            self.aero_window, self.son_window = pywin_openAProgram().menuOpen(testdicts)
            specialWay_OperatingControls(self.operationWindow_son).uia_OperatingControls()
            self.module_window, self.work_window = BeingMeasured_work(self.son_window).workField_intensityCheck()
        else:
            import sys, os
            print("在执行用例步骤前不知道程序初始化级别", __file__, sys._getframe().f_lineno)
            os._exit(0)
        #  操作步骤
        ModuleControlOperation(self.module_window).CompoundStrengthCheck_1D_operation(self.testdicts,self.work_window)
        # 获取实际值
        if self.Message_type == "警告弹窗":
            UseCase_Number = self.testdicts["用例编号"]  # 取出预期值
            self.actual_Text = Warning_PopUp(self.aero_window).Warning_PopUp_TXT(UseCase_Number)
        elif self.Message_type == "信息窗口":
            self.actual_Text = Information_Win().acquire_HTML_TXT(self.source)
        else:
            print("没有获取实际的文本测试结果")
        return self.actual_Text