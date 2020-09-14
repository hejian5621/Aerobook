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
        self.window_one = None  # 通用
        self.window_two = None  # 特殊一
        self.window_three = None  # 特殊二
        self.example=None


    def Perform_useCase_Steps(self):
        """
        执行用例步骤
        :return:
        """
        # 连接到被测程序，并且通过菜单栏打开被测模块
        aero_window, son_window = pywin_openAProgram().menuOpen(self.testCase_dict)
        # 铺层信息--铺层库优化工作栏测试用例、求解计算--求解计算
        if self.global_UseCase_Name == "铺层信息--铺层库优化工作栏测试用例" or self.global_UseCase_Name =="求解计算--求解计算" :
            self.window_one = BeingMeasured_work(son_window).workField_general()
        elif self.global_UseCase_Name == "尺寸信息--一维二维单元尺寸定义（模板）":  # 尺寸信息--一维二维单元尺寸定义（模板）
            print("执行到此地方")
            self.window_one=BeingMeasured_work(son_window).workField_sizeInfo()
        elif self.global_UseCase_Name == "铺层信息--铺层数据库制作工具弹窗":  # 铺层信息--铺层数据库制作工具弹窗
            # 切入铺层数据库工具弹窗中
            self.window_three = BeingMeasured_popupWin("铺层数据库制作工具").menu_LetsGoTopopover()
            # 切入铺层数据库工具弹窗中控件中
            self.window_one, self.window_two = BeingMeasured_popupWin(None).\
                Laminatedata_popUp(self.window_three)
        elif self.global_UseCase_Name == "载荷信息--载荷数据库制作工具弹窗":  # 载荷信息--载荷数据库制作工具弹窗
            # 切入铺层数据库工具弹窗中
            self.window_three = BeingMeasured_popupWin("载荷数据库制作工具").menu_LetsGoTopopover()
            # 切入铺层数据库工具弹窗中控件中
            self.window_one, self.window_two = BeingMeasured_popupWin(None).\
                Laminatedata_popUp(self.window_three)
        elif self.global_UseCase_Name == "载荷信息--编辑工况":  # 载荷信息--编辑工况
            self.window_one = BeingMeasured_popupWin("编辑工况").menu_LetsGoTopopover()
        elif self.global_UseCase_Name == "复材结构强度校核--复合材料强度校核1D" or \
                self.global_UseCase_Name == "复材结构强度校核--复合材料强度校核2D":  # 复材结构强度校核--复合材料强度校核
            print("开始切换到复合材料强度校核工作栏")
            specialWay_OperatingControls(self.operationWindow_son).uia_OperatingControls()  # 使用uiautomation框架点击切换模块
            self.window_one, self.window_two=BeingMeasured_work(son_window).workField_intensityCheck()
        # 操作控件
        OperatingControls(self.window_one,  self.window_two, self.window_three). \
            controlConsole(self.testCase_attribute, self.testCase_dict)
        # 获取实际值
        time.sleep(self.results_waitTime) # 实际值等待时间
        # 获取时间值实例
        if self.global_UseCase_Name == "载荷信息--编辑工况":
            self.example = self.window_one
        self.actual_Text = GetActual_Value(self.testCase_dict,self.example).ActualValue_controller()
        return self.actual_Text



    def Perform_useCase_Steps_nest(self):
        """
         执行用例步骤代嵌套弹框
        :return:
        """
        # 执行步骤之前初始化
        if self.initialLevel == "整个被测模块":  # 点击菜单栏进入被测模板，并且通过UIA框架切换窗口，针对工作栏
            self.aero_window, self.son_window = pywin_openAProgram().\
                menuOpen_switchingWin_UIA(self.testCase_dict,self.operationWindow)
        elif self.initialLevel == "编辑材料许用值弹窗" or self.initialLevel == "定义材料许用值":  # 初始化编辑材料许用值和定义材料许用值
            self.son_window = execute_useCase_initialize().link_window()  # 链接被测程序
        else:
            print("在执行用例步骤前不知道程序初始化级别", __file__, sys._getframe().f_lineno)
            os._exit(0)
        # 切换到材料信息--定义复合材料信息--编辑材料许用值、定义材料许用值模块
        self.window_one = BeingMeasured_work(self.son_window).workField_composite_information() #



        #  操作步骤
        if self.operationWindow_son =="编辑材料许用值曲线弹窗":
            # 打开“编辑材料许用值曲线弹窗”弹框
            ModuleControlOperation(self.window_one).editAllowable_operation(self.testCase_dict)
            # 切换到“编辑材料许用值曲线弹窗”中
            dlg1_spec = BeingMeasured_popupWin("编辑材料许用值曲线").menu_LetsGoTopopover()
            #  切换到网格窗口
            dlg2_spec = dlg1_spec.child_window(title="GridWindow", class_name="wxWindowNR")
            # 向被测模块输入数据
            OperatingControls(dlg1_spec,dlg2_spec).controlConsole(self.testCase_attribute, self.testCase_dict)
        elif self.operationWindow_son =="定义材料许用值":
            # 操作“定义材料许用值”工作栏
            OperatingControls(self.window_one).controlConsole(self.testCase_attribute, self.testCase_dict)
        # 获取实际值
        time.sleep(self.results_waitTime)
        example = self.window_one.ComboBox
        self.actual_Text = GetActual_Value(self.testCase_dict,example).ActualValue_controller()
        return self.actual_Text













