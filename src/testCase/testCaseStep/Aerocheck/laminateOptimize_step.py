# 用例步骤

from src.utils.otherMethods.Initialize import programInitialization
from config.configurationFile import ProfileDataProcessing
from OperatingControls.EnterModule import open_module
from src.utils.OperatingControls.ModuleControlOperation import ModuleControlOperation
from src.utils.otherMethods.actual import ActualProcessing
import time

class LaminateOptimize_execute:
    """测试用例执行步骤"""

    def __init__(self):
        pass


    def textbox(self,testdicts):
        """
        文本框测试
        :return:
        """
        inModule=testdicts["所在模块"];expect_line=int(testdicts["预期结果行数"])
        # 读取配置文档信息
        aero_title = ProfileDataProcessing("commonality", "AerobookEdition").config_File()  # 从配置文件获取Aerobook窗口标题
        aerocheck_title = ProfileDataProcessing("commonality", "AerocheckEdition").config_File()  # 从配置文件获取Aerocheck窗口标题
        # 通过Aerobook标题链接Aerobook进行，并切换到Aerobook窗口
        aero_window=programInitialization().entrance_subroutine_title(aero_title)
        # 通过操作菜单栏，打开被测模块，然后切换到被测模块
        module_window=open_module().menu_laminateOptimize(inModule,aero_window,aerocheck_title)
        # 向被测模块输入数据
        ModuleControlOperation(module_window).laminate_optimize(testdicts)
        time.sleep(3)
        # 获取实际值
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
        inModule = testdicts["所在模块"];expect_line = int(testdicts["预期结果行数"])
        # 读取配置文档信息
        aero_title = ProfileDataProcessing("commonality", "AerobookEdition").config_File()  # 从配置文件获取Aerobook窗口标题
        aerocheck_title = ProfileDataProcessing("commonality", "AerocheckEdition").config_File()  # 从配置文件获取Aerocheck窗口标题
        # 通过Aerobook标题链接Aerobook进行，并切换到Aerobook窗口
        aero_window = programInitialization().entrance_subroutine_title(aero_title)
        # 通过操作菜单栏，打开被测模块，然后切换到被测模块
        module_window = open_module().menu_laminateOptimize(inModule, aero_window, aerocheck_title)
        # 向被测模块输入数据
        ModuleControlOperation(module_window).laminate_optimize(testdicts)