# 用例步骤

from src.utils.otherMethods.initialize import programInitialization
from config.configurationFile import ProfileDataProcessing
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
        inModule=testdicts["所在模块"];Message_type = int(testdicts["提示信息类型"]);actual_Text=None
        # 读取配置文档信息
        aero_title = ProfileDataProcessing("commonality", "AerobookEdition").config_File()  # 从配置文件获取Aerobook窗口标题
        aerocheck_title = ProfileDataProcessing("commonality", "AerocheckEdition").config_File()  # 从配置文件获取Aerocheck窗口标题
        # 通过Aerobook标题链接Aerobook进行，并切换到Aerobook窗口
        aero_window=programInitialization(aero_title).entrance_subroutine_title()
        # 通过操作菜单栏，打开被测模块，然后切换到被测模块
        module_window=open_module().menu_laminateOptimize(inModule,aero_window,aerocheck_title)
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
        选择文件文本框
        :return:
        """
        edit_list=None
        actual_Text=None
        inModule = testdicts["所在模块"]
        Message_type = testdicts["提示信息类型"]
        # 读取配置文档信息
        aero_title = ProfileDataProcessing("commonality", "AerobookEdition").config_File()  # 从配置文件获取Aerobook窗口标题
        aerocheck_title = ProfileDataProcessing("commonality", "AerocheckEdition").config_File()  # 从配置文件获取Aerocheck窗口标题
        # 通过Aerobook标题链接Aerobook进行，并切换到Aerobook窗口
        aero_window = programInitialization(aero_title).entrance_subroutine_title()
        # 通过操作菜单栏，打开被测模块，然后切换到被测模块
        module_window,dlg_spec = open_module().menu_Laminatedata(inModule, aero_window, aerocheck_title)
        # 向被测模块输入数据
        edit_list=ModuleControlOperation(module_window).Laminatedata(testdicts,dlg_spec)
        # 获取实际值
        if Message_type=="警告弹窗":
            expect_result = testdicts["预期结果提示信息"]  # 取出预期值
            actual_Text,app1,dlg_spec_warn = ActualProcessing(aero_window).Laminatedata_warning_warning(expect_result)
            # 关闭警告窗口
            instrument().window_WhetherClose(dlg_spec_warn,app1,"警告窗口没有关闭")
        elif Message_type=="信息窗口":
            expect_line = int(testdicts["预期结果行数"])
            actual_Text = ActualProcessing(aero_window).laminateOptimize(expect_line)
        return actual_Text,edit_list,dlg_spec