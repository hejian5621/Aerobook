# 用例步骤
from src.utils.otherMethods.initialize import pywin_openAProgram,execute_useCase_initialize
from OperatingControls.enterModule import BeingMeasured_popupWin,BeingMeasured_work,specialWay_OperatingControls
from src.utils.otherMethods.actual import GetActual_Value
from tool import Check_winControl
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
        self.results_waitTime = testCase_dict["测试结果等待时间"]  # 取出预期值
        self.initialLevel = testCase_dict["初始化级别"]
        self.operationWindow = testCase_dict["操作窗口标题"]
        self.operationWindow_son = testCase_dict["操作子窗口标题"]
        self.global_UseCase_Name= testCase_dict["用例集名称"]
        self.actual_Text = None
        self.aero_window = None
        self.son_window = None
        self.window_one = None  # 窗口一
        self.window_two = None  # 窗口二
        self.window_three = None  # 窗口三
        self.window_four=None    # 窗口四
        self.example=None


    def Perform_useCase_Steps(self):
        """
        执行用例步骤
        :return:
        """
        # 连接到被测程序，并且通过菜单栏打开被测模块
        aero_window, son_window = pywin_openAProgram().menuOpen(self.testCase_dict)
        # 切换到被测模块窗口
        if self.global_UseCase_Name == "铺层信息--铺层库优化工作栏" or self.global_UseCase_Name =="求解计算--求解计算" or \
            self.global_UseCase_Name =="紧固件强度校核--紧固件参数设置":
            self.window_one = BeingMeasured_work(son_window).workField_general()
        elif self.global_UseCase_Name == "尺寸信息--一维二维单元尺寸定义（模板）":
            self.window_one=BeingMeasured_work(son_window).workField_sizeInfo()
        elif self.global_UseCase_Name == "铺层信息--铺层数据库制作工具弹窗":
            # 切入铺层数据库工具弹窗中
            self.window_three = BeingMeasured_popupWin("铺层数据库制作工具").menu_LetsGoTopopover()
            # 切入铺层数据库工具弹窗中控件中
            self.window_one, self.window_two = BeingMeasured_popupWin(None).\
                Laminatedata_popUp(self.window_three)
        elif self.global_UseCase_Name == "载荷信息--载荷数据库制作工具弹窗":
            # 切入铺层数据库工具弹窗中
            self.window_three = BeingMeasured_popupWin("载荷数据库制作工具").menu_LetsGoTopopover()
            # 切入铺层数据库工具弹窗中控件中
            self.window_one, self.window_two = BeingMeasured_popupWin(None).\
                Laminatedata_popUp(self.window_three)
        elif self.global_UseCase_Name == "载荷信息--编辑工况":
            self.window_one = BeingMeasured_popupWin("编辑工况").menu_LetsGoTopopover()
        elif self.global_UseCase_Name == "复材结构强度校核--复合材料强度校核1D" or \
                self.global_UseCase_Name == "复材结构强度校核--复合材料强度校核2D":
            specialWay_OperatingControls(self.operationWindow_son).uia_OperatingControls()  # 使用uiautomation框架点击切换模块
            self.window_one, self.window_two=BeingMeasured_work(son_window).workField_intensityCheck()
        elif self.global_UseCase_Name == "尺寸信息--1D单元尺寸定义":
            self.window_one,self.window_two,self.window_three,self.window_four = BeingMeasured_work(son_window).\
                workField_SizeDefinition_1D()
        elif self.global_UseCase_Name == "尺寸信息--2D单元尺寸定义":
            self.window_one,self.window_two = BeingMeasured_work(son_window).\
                workField_SizeDefinition_2D()
        elif self.global_UseCase_Name == "紧固件强度校核--紧固件参数输入":
            if self.operationWindow_son =="紧固件参数输入":
                self.window_one = BeingMeasured_work(son_window).workField_general()
            elif self.operationWindow_son =="编辑参数弹框":
                self.window_one = BeingMeasured_work(son_window).workField_Open_EditArgument()
        else:
            print("没有找到需要切换的窗口：%r"%self.global_UseCase_Name, __file__, sys._getframe().f_lineno)
            os._exit(0)
        # 操作控制
        OperatingControls(self.window_one,  self.window_two, self.window_three,self.window_four). \
            controlConsole(self.testCase_attribute, self.testCase_dict)
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

        self.aero_window, self.son_window = pywin_openAProgram().\
            menuOpen_switchingWin_UIA(self.testCase_dict,self.operationWindow)
        # 切换到材料信息--定义复合材料信息--编辑材料许用值、定义材料许用值模块
        self.window_one = BeingMeasured_work(self.son_window).workField_composite_information()
        #  操作步骤
        if self.operationWindow_son =="编辑材料许用值曲线弹窗":
            # # 清除所有的许用值曲线
            # execute_useCase_initialize().clear_AllowableCurve()
            dlg_spec = OperatingControls(self.window_one).ExpressionAssembly("Button1")
            # 检查点击按钮后，弹窗是否出现
            Check_winControl("编辑材料许用值曲线", dlg_spec).window_WhetherOpen()  # 判断预期窗口是否出现
            # 切换到“编辑材料许用值曲线弹窗”中
            self.window_one = BeingMeasured_popupWin("编辑材料许用值曲线").menu_LetsGoTopopover()
            #  切换到网格窗口
            self.window_two =  self.window_one.child_window(title="GridWindow", class_name="wxWindowNR")
        # 向被测模块输入数据
        OperatingControls(self.window_one, self.window_two, self.window_three). \
            controlConsole(self.testCase_attribute, self.testCase_dict)
        # 获取实际值
        time.sleep(self.results_waitTime)
        # example = self.window_one.ComboBox
        # self.actual_Text = GetActual_Value(self.testCase_dict).ActualValue_controller()
        return self.actual_Text













