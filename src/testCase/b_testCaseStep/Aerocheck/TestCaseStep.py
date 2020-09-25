# 用例步骤
from src.utils.otherMethods.initialize import pywin_openAProgram
from OperatingControls.enterModule import GetWindowInstance
from src.utils.otherMethods.actual import GetActual_Value
from src.utils.OperatingControls.moduleControlOperation import OperatingControls
import time
import sys, os



class UseCase_step:
    """执行测试用例步骤"""

    def __init__(self, testCase_attribute, property):
        self.testCase = testCase_attribute  # 字典类型嵌套字典类型的控件属性方法
        self.property = property  # 字典类型测试用例
        self.results_waitTime = property["测试结果等待时间"]
        self.initialLevel = property["初始化级别"]
        self.testWinTitle = property["操作窗口标题"]
        self.testWinTitle_son = property["操作子窗口标题"]
        self.ModuMarking= property["模块唯一标识"]
        self.actual_Text = None
        self.win_one = None  # 窗口一
        self.win_two = None  # 窗口二
        self.win_three = None  # 窗口三
        self.win_four=None    # 窗口四
        self.example=None



    def Perform_useCase_Steps(self):
        """
        执行用例步骤
        :return:
        """
        # 连接到被测程序，并且通过菜单栏打开被测模块
        aero_window, son_window = pywin_openAProgram().menuOpen(self.property)
        # 切换到被测模块窗口
        self.win_one,self.win_two,self.win_three,self.win_four=GetWindowInstance(self.property,son_window).\
            get_window_instance()
        # 操作控制
        OperatingControls(self.win_one,self.win_two,self.win_three,self.win_four).console(self.testCase, self.property)
        time.sleep(self.results_waitTime) # 实际值等待时间
        # 获取时间值实例
        if self.ModuMarking == "载荷信息--编辑工况":
            self.example = self.win_one
        self.actual_Text = GetActual_Value(self.property,self.example).ActualValue_controller()
        return self.actual_Text













