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
        self.actual_Text = None
        self.win_one = None  # 窗口一
        self.win_two = None  # 窗口二
        self.win_three = None  # 窗口三
        self.win_four=None    # 窗口四
        self.example=None



    def Perform_useCase_Steps(self,result=0):
        """
        执行用例步骤
        :param result: 为1：就不需要获取实际值，为0就需要获取实际值
        :return:
        """
        # 打开被测试模块，并返回窗口的标识
        self.win_one,self.win_two,self.win_three,self.win_four=GetWindowInstance(self.property).get_window_instance()
        # 具体操作控件
        OperatingControls(self.win_one,self.win_two,self.win_three,self.win_four).console(self.testCase, self.property)
        # 当所有的操作步骤操作完成后，需要等待一段时间，让系统进行计算
        if self.results_waitTime :
            pass
        else:
            self.results_waitTime=0
        time.sleep(self.results_waitTime) # 实际值等待时间
        # 获取实际值
        self.example=[self.win_one,self.win_two,self.win_three,self.win_four]   # 把被测模块中的各个小窗口，打包
        self.actual_Text = GetActual_Value(self.property,self.example).ActualValue_controller(result)
        return self.actual_Text













