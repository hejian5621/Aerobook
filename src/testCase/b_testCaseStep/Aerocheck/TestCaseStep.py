# 用例步骤

from src.utils.otherMethods.initialize import programInitialization,execute_useCase_initialize

from OperatingControls.enterModule import open_module
from src.utils.OperatingControls.moduleControlOperation import ModuleControlOperation
from src.utils.otherMethods.actual import ActualProcessing
import time
from src.utils.commonality.tool import instrument




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
        aero_window, son_window = execute_useCase_initialize().execute_useCase_enterInto(testdicts)
        # 通过操作菜单栏，打开被测模块，然后切换到被测模块
        module_window=open_module().menu_laminateOptimize(son_window)
        # 向被测模块输入数据
        ModuleControlOperation(module_window).laminate_optimize(testdicts)
        # 获取实际值
        if Message_type == "信息窗口":
            expect_line = int(testdicts["预期结果行数"])
            actual_Text=ActualProcessing(aero_window).laminateOptimize(expect_line)
        return actual_Text




class Laminatedata_execute:
    """铺层数据库工具弹窗"""

    def __init__(self):
        pass


    def SelectFile(self,testdicts):
        """
        铺层数据库工具弹窗，选择文件文本框
        :return:
        """
        edit_list=None
        actual_Text=None
        inModule = testdicts["所在模块"]
        Message_type = testdicts["提示信息类型"]
        source = testdicts["被测程序文件地址"]
        aero_window, son_window = execute_useCase_initialize().execute_useCase_enterInto(testdicts)
        # 切入铺层数据库工具弹窗中
        module_window = open_module().menu_Laminatedata()
        # 向被测模块输入数据
        edit_list=ModuleControlOperation(module_window).Laminatedata_operation(testdicts)
        # 获取实际值
        if Message_type=="警告弹窗":
            UseCase_Number = testdicts["用例编号"]  # 取出预期值
            actual_Text= ActualProcessing(aero_window).Laminatedata_warning_warning(UseCase_Number)
            # 关闭警告窗口
            parWin_Dicti = {"窗口标题": "警告", "关闭窗口控件名称": "OK", "关闭窗口控件操作方法": "click"}
            instrument().popUp_Whether_close(parWin_Dicti)
        elif Message_type=="信息窗口":
            # expect_line = int(testdicts["预期结果行数"])
            # actual_Text = ActualProcessing(aero_window).laminateOptimize(expect_line)
            actual_Text = ActualProcessing(None).acquire_HTML_TXT(source)
        return actual_Text,edit_list


class sizeInfo_1DXls_execute:
    """尺寸信息--1D单元尺寸定义（模板）"""

    def __init__(self):
        pass



    def SelectFile(self, testdicts):
        """
        选择文件文本框
        :return:
        """
        edit_list = None;actual_Text = None
        inModule = testdicts["所在模块"]
        Message_type = testdicts["提示信息类型"]
        source=testdicts["被测程序文件地址"]
        aero_window, son_window = execute_useCase_initialize().execute_useCase_enterInto(testdicts)
        # 切换到尺寸定义工作栏
        module_window = open_module().menu_sizeInfo_1DXls(son_window )
        ModuleControlOperation(module_window).sizeInfo_1DXls_operation(testdicts)
        # 获取实际值
        if Message_type == "警告弹窗":
            UseCase_Number = testdicts["用例编号"]  # 取出预期值
            actual_Text = ActualProcessing(aero_window).Laminatedata_warning_warning(UseCase_Number)
            # 关闭警告窗口
            parWin_Dicti = {"窗口标题": "警告", "关闭窗口控件名称": "OK", "关闭窗口控件操作方法": "click"}
            instrument().popUp_Whether_close(parWin_Dicti)
        elif Message_type == "信息窗口":
            # expect_line = int(testdicts["预期结果行数"])
            # actual_Text = ActualProcessing(aero_window).laminateOptimize(expect_line)
            # 通过获取html文件里的内容获取”信息窗口“里的内容
            actual_Text =ActualProcessing(None).acquire_HTML_TXT(source)
        else:
            print("没有获取实际的文本测试结果")
        return actual_Text



class solveCalculation_execute:
    """求解计算"""

    def __init__(self):
        pass



    def SelectFile(self, testdicts):
        """
        选择文件文本框
        :return:
        """
        edit_list = None;actual_Text = None
        inModule = testdicts["所在模块"]
        Message_type = testdicts["提示信息类型"]
        source=testdicts["被测程序文件地址"]
        aero_window,son_window =execute_useCase_initialize().execute_useCase_enterInto(testdicts)
        # 切换到尺寸定义工作栏
        module_window = open_module().menu_general(son_window)
        # 向被测模块输入数据
        ModuleControlOperation(module_window).solveCalculation_operation(testdicts)
        # 获取实际值
        if Message_type == "警告弹窗":
            UseCase_Number = testdicts["用例编号"]  # 取出预期值
            actual_Text = ActualProcessing(aero_window).Laminatedata_warning_warning(UseCase_Number)
        elif Message_type == "信息窗口":
            actual_Text =ActualProcessing(None).acquire_HTML_TXT(source)
        else:
            print("没有获取实际的文本测试结果")
        return actual_Text




class editWorkingCondition_execute:
    """求解计算"""

    def __init__(self):
        pass



    def SelectFile(self, testdicts):
        """
        选择文件文本框
        :return:
        """
        edit_list = None;actual_Text = ""
        inModule = testdicts["所在模块"]
        Message_type = testdicts["提示信息类型"]
        source=testdicts["被测程序文件地址"]
        aero_window,son_window =execute_useCase_initialize().execute_useCase_enterInto(testdicts)
        # 切换到编辑工况弹窗
        module_window = open_module().menu_editWorkingCondition()
        # 向被测模块输入数据
        ModuleControlOperation(module_window).editWorkingCondition_operation(testdicts)
        # 获取实际值
        if Message_type == "警告弹窗":
            UseCase_Number = testdicts["用例编号"]  # 取出预期值
            actual_Text = ActualProcessing(aero_window).Laminatedata_warning_warning(UseCase_Number)
        elif  Message_type == "本地返回":
            # 获取工况组合下拉框里的文本信息
            actual_Text = ActualProcessing(None).editWorkingCondition_TXT(module_window)
        else:
            print("没有获取实际的文本测试结果")
        return actual_Text