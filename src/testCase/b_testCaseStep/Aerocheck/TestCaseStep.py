# 用例步骤
from src.utils.otherMethods.initialize import pywin_openAProgram,execute_useCase_initialize
from OperatingControls.enterModule import BeingMeasured_popupWin,BeingMeasured_work,specialWay_OperatingControls
from src.utils.OperatingControls.moduleControlOperation import ModuleControlOperation
from src.utils.otherMethods.actual import Warning_PopUp,GetActual_Value
from src.utils.otherMethods.actual import Information_Win
from src.utils.OperatingControls.moduleControlOperation import OperatingControls
import time
import sys, os



class UseCase_step:
    """执行测试用例步骤"""

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
        self.global_UseCase_Name= testCase_dict["用例集名称"]
        self.actual_Text = None
        self.aero_window = None
        self.son_window = None
        self.general_window = None  # 通用
        self.special_window_one = None  # 特殊一
        self.module_window_two = None  # 特殊二
        self.example=None


    def Perform_useCase_Steps(self):
        """
        执行用例步骤
        :return:
        """
        # 连接到被测程序，并且通过菜单栏打开被测模块
        aero_window, son_window = pywin_openAProgram().menuOpen(self.testCase_dict)
        # 铺层信息--铺层库优化工作栏测试用例、尺寸信息--一维二维单元尺寸定义（模板）、求解计算--求解计算、复材结构强度校核--复合材料强度校核
        if self.global_UseCase_Name == "Test_LaminateOptimize" or self.global_UseCase_Name == "Test_sizeInfo_1D2DXls" \
           or self.global_UseCase_Name =="Test_solveCalculation" or self.global_UseCase_Name =="Test_CompoundStrengthCheck":
            self.general_window = BeingMeasured_work(son_window).workField_general()
        elif self.global_UseCase_Name == "Test_LaminatedataPopup":  # 铺层信息--铺层数据库制作工具弹窗
            # 切入铺层数据库工具弹窗中
            self.general_window = BeingMeasured_popupWin("铺层数据库制作工具").menu_LetsGoTopopover()
            # 切入铺层数据库工具弹窗中控件中
            self.special_window_one, self.module_window_two = BeingMeasured_popupWin(None).\
                Laminatedata_popUp(self.general_window)
        elif self.global_UseCase_Name == "Test_loaddatabase_popUp":  # 载荷信息--载荷数据库制作工具弹窗
            # 切入铺层数据库工具弹窗中
            self.general_window = BeingMeasured_popupWin("载荷数据库制作工具").menu_LetsGoTopopover()
            # 切入铺层数据库工具弹窗中控件中
            self.special_window_one, self.module_window_two = BeingMeasured_popupWin(None).\
                Laminatedata_popUp(self.general_window)
        elif self.global_UseCase_Name == "Test_editWorkingCondition":  # 载荷信息--编辑工况
            self.general_window = BeingMeasured_popupWin("编辑工况").menu_LetsGoTopopover()
        OperatingControls(self.general_window, self.special_window_one, self.module_window_two). \
            controlConsole(self.testCase_attribute, self.testCase_dict)
        # 获取实际值
        time.sleep(self.results_waitTime) # 实际值等待时间
        # 获取时间值实例
        if self.global_UseCase_Name == "Test_editWorkingCondition":
            self.example = self.general_window.ComboBox

        self.actual_Text = GetActual_Value(self.testCase_dict,self.example).ActualValue_controller()
        return self.actual_Text



    def Perform_useCase_Steps_nest(self):
        """
         执行用例步骤代嵌套弹框
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









