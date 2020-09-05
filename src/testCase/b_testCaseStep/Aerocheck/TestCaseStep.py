# 用例步骤

from src.utils.otherMethods.initialize import pywin_openAProgram,execute_useCase_initialize
from OperatingControls.enterModule import BeingMeasured_popupWin,BeingMeasured_work,specialWay_OperatingControls
from src.utils.OperatingControls.moduleControlOperation import ModuleControlOperation
from src.utils.otherMethods.actual import ActualProcessing,Warning_PopUp
import time
from tool import instrument,Check_winControl
from src.utils.otherMethods.actual import localControl
from src.utils.otherMethods.actual import Information_Win


class LaminateOptimize_execute:
    """测试用例执行步骤"""

    def __init__(self):
        pass


    def textbox(self,testdicts):
        """
        文本框测试
        :return:
        """
        MenuOptions=testdicts["所在模块"];Message_type = int(testdicts["提示信息类型"]);actual_Text=None
        # 读取配置文档信息
        aero_window, son_window = pywin_openAProgram().execute_useCase_enterInto(testdicts)
        # 通过操作菜单栏，打开被测模块，然后切换到被测模块
        module_window=BeingMeasured_work(son_window).workField_general()
        # 向被测模块输入数据
        ModuleControlOperation(module_window).laminate_optimize(testdicts)
        # 获取实际值
        if Message_type == "信息窗口":
            expect_line = int(testdicts["预期结果行数"])
            actual_Text=ActualProcessing(aero_window).laminateOptimize(expect_line)
        return actual_Text




class Laminatedata_execute:
    """铺层数据库工具弹窗"""

    def __init__(self, testdicts):
        self.testdicts = testdicts
        self.Message_type = testdicts["提示信息类型"]
        self.source = testdicts["被测程序文件地址"]
        self.actual_Text = None


    def SelectFile(self):
        """
        铺层数据库工具弹窗，选择文件文本框
        :return:
        """
        aero_window, son_window = pywin_openAProgram().execute_useCase_enterInto(self.testdicts)
        # 切入铺层数据库工具弹窗中
        module_window = BeingMeasured_popupWin("铺层数据库制作工具").menu_LetsGoTopopover()
        # 向被测模块输入数据
        edit_list=ModuleControlOperation(module_window).Laminatedata_operation(self.testdicts)
        # 获取实际值
        if self.Message_type=="警告弹窗":
            UseCase_Number = self.testdicts["用例编号"]  # 取出预期值
            self.actual_Text=Warning_PopUp(aero_window).Warning_PopUp_TXT(UseCase_Number)
            # 关闭警告窗口
            Check_winControl("警告", "OK").popUp_Whether_close()
        elif self.Message_type=="信息窗口":
            self.actual_Text = Information_Win().acquire_HTML_TXT(self.source)
        return self.actual_Text,edit_list


class sizeInfo_1DXls_execute:
    """尺寸信息--1D单元尺寸定义（模板）"""

    def __init__(self, testdicts):
        self.testdicts = testdicts
        self.Message_type = testdicts["提示信息类型"]
        self.source = testdicts["被测程序文件地址"]
        self.actual_Text = None



    def SelectFile(self):
        """
        选择文件文本框
        :return:
        """
        aero_window, son_window = pywin_openAProgram().execute_useCase_enterInto(self.testdicts)
        # 切换到尺寸定义工作栏
        module_window = BeingMeasured_work(son_window).workField_sizeInfo()
        ModuleControlOperation(module_window).sizeInfo_1DXls_operation( self.testdicts)
        # 获取实际值
        if self.Message_type == "警告弹窗":
            UseCase_Number = testdicts["用例编号"]  # 取出预期值
            self.actual_Text = Warning_PopUp(aero_window).Warning_PopUp_TXT(UseCase_Number)

            # 关闭警告窗口
            Check_winControl("警告", "OK").popUp_Whether_close()
        elif self.Message_type == "信息窗口":
            # expect_line = int(testdicts["预期结果行数"])
            # actual_Text = ActualProcessing(aero_window).laminateOptimize(expect_line)
            # 通过获取html文件里的内容获取”信息窗口“里的内容
            self.actual_Text = Information_Win().acquire_HTML_TXT(self.source)
        else:
            print("没有获取实际的文本测试结果")
        return self.actual_Text



class solveCalculation_execute:
    """求解计算"""

    def __init__(self, testdicts):
        self.testdicts = testdicts
        self.Message_type = testdicts["提示信息类型"]
        self.source=testdicts["被测程序文件地址"]
        self.actual_Text = None



    def SelectFile(self):
        """
        选择文件文本框
        :return:
        """
        aero_window,son_window =pywin_openAProgram().execute_useCase_enterInto(self.testdicts)
        # 切换到尺寸定义工作栏
        module_window = BeingMeasured_work(son_window).workField_general()
        # 向被测模块输入数据
        ModuleControlOperation(module_window).solveCalculation_operation(self.testdicts)
        # 获取实际值
        if self.Message_type == "警告弹窗":
            UseCase_Number = self.testdicts["用例编号"]  # 取出预期值
            self.actual_Text = Warning_PopUp(aero_window).Warning_PopUp_TXT(UseCase_Number)
        elif self.Message_type == "信息窗口":
            self.actual_Text = Information_Win().acquire_HTML_TXT(self.source)
        else:
            print("没有获取实际的文本测试结果")
        return self.actual_Text





class loaddatabase_popUp_execute:
    """载荷数据库工具弹窗"""

    def __init__(self, testdicts):
        self.testdicts = testdicts
        self.Message_type = testdicts["提示信息类型"]
        self.source = testdicts["被测程序文件地址"]
        self.actual_Text = None


    def SelectFile(self):
        """
        铺层数据库工具弹窗，选择文件文本框
        :return:
        """
        aero_window, son_window = pywin_openAProgram().execute_useCase_enterInto(self.testdicts)
        # 切入铺层数据库工具弹窗中
        module_window = BeingMeasured_popupWin("载荷数据库制作工具").menu_LetsGoTopopover()
        # 向被测模块输入数据
        edit_list=ModuleControlOperation(module_window).loaddatabase_popUp_operation(self.testdicts)
        # 获取实际值
        if self.Message_type=="警告弹窗":
            UseCase_Number = self.testdicts["用例编号"]  # 取出预期值
            self.actual_Text = Warning_PopUp(aero_window).Warning_PopUp_TXT(UseCase_Number)
            # 关闭警告窗口
            Check_winControl("警告", "OK").popUp_Whether_close()
        elif self.Message_type=="信息窗口":
            self.actual_Text = Information_Win().acquire_HTML_TXT(self.source)
        return self.actual_Text,edit_list



class editWorkingCondition_execute:
    """求解计算"""

    def __init__(self,testdicts):
        self.testdicts=testdicts
        self.Message_type = testdicts["提示信息类型"]
        self.actual_Text = None



    def SelectFile(self):
        """
        选择文件文本框
        :return:
        """
        from src.utils.otherMethods.actual import localControl
        # 初始化，链接Aerobook，返回对象实体
        aero_window,son_window =pywin_openAProgram().execute_useCase_enterInto(self.testdicts)
        # 切换到编辑工况弹窗
        module_window = BeingMeasured_popupWin("编辑工况").menu_LetsGoTopopover()
        # 向被测模块输入数据
        ModuleControlOperation(module_window).editWorkingCondition_operation(self.testdicts)
        # 获取实际值
        if self.Message_type == "警告弹窗":
            UseCase_Number = self.testdicts["用例编号"]  # 取出预期值
            self.actual_Text = Warning_PopUp(aero_window).Warning_PopUp_TXT(UseCase_Number)
        elif  self.Message_type == "本地返回":
            # 获取工况组合下拉框里的文本信息
            example=module_window.ComboBox
            self.actual_Text = localControl(example).LocalControl_TXT()
        else:
            print("没有获取实际的文本测试结果")
        return self.actual_Text


class compositeMaterial:
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




    def SelectFile(self):
        """
        选择文件文本框
        :return:
        """
        # 执行步骤之前初始化
        if self.initialLevel == "整个工作栏":  # 初始化这个工作栏，或者弹窗，返回对象实体
            self.aero_window, self.son_window = pywin_openAProgram().execute_useCase_enterInto(self.testdicts)
            specialWay_OperatingControls(self.operationWindow).uia_OperatingControls()
            self.module_window = BeingMeasured_work(self.son_window).workField_composite_information()
        elif self.initialLevel == "编辑材料许用值弹窗" or self.initialLevel == "定义材料许用值":  # 初始化编辑材料许用值和定义材料许用值
            # 链接被测程序
            self.son_window = execute_useCase_initialize().link_window()
            self.module_window = BeingMeasured_work(self.son_window).workField_composite_information()
        else:
            import sys, os
            print("在执行用例步骤前不知道程序初始化级别", __file__, sys._getframe().f_lineno)
            os._exit(0)
        #  操作步骤
        if self.operationWindow_son =="编辑材料许用值曲线弹窗":
            # 打开“编辑材料许用值曲线弹窗”弹框
            ModuleControlOperation(self.module_window).editAllowable_operation(self.testdicts)
            # 切换到“编辑材料许用值曲线弹窗”中
            dlg1_spec = BeingMeasured_popupWin("编辑材料许用值曲线").menu_LetsGoTopopover()
            # 操作“编辑材料许用值曲线弹窗”弹框
            ModuleControlOperation(dlg1_spec).editAllowable_CurvePopupWin_operation(self.testdicts)
        elif self.operationWindow_son =="定义材料许用值":
            # 操作“定义材料许用值”工作栏
            ModuleControlOperation(self.module_window).DefineAllowable_operation(self.testdicts)
        # 获取实际值
        if self.Message_type == "警告弹窗":
            UseCase_Number = self.testdicts["用例编号"]  # 取出预期值
            self.actual_Text = Warning_PopUp(self.aero_window).Warning_PopUp_TXT(UseCase_Number)
        elif self.Message_type == "本地返回":
            # 获取工况组合下拉框里的文本信息
            example=self.module_window.ComboBox
            self.actual_Text = localControl(example).LocalControl_TXT()
        else:
            print("没有获取实际的文本测试结果")
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
            self.aero_window, self.son_window = pywin_openAProgram().execute_useCase_enterInto(self.testdicts)
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
            self.aero_window, self.son_window = pywin_openAProgram().execute_useCase_enterInto(testdicts)
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