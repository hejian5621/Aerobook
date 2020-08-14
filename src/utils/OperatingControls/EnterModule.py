# 打开被模块
import time

class open_module:
    """进入被测模块"""


    def __init__(self):
        pass


    def menu_laminateOptimize(self, MenuOptions,Aero_window,Aerocheck_title):
        """
        切换到菜单栏，点击对应的菜单选项，打开铺层库优化工作栏，切换到铺层库优化工作栏
        通过pywinauto框架执行
        :param Aero_window:
        :param Aerocheck_title: Aerocheck窗口标题
        :param MenuOptions: 菜单选项,使用格式：r"尺寸信息->一维单元尺寸定义"
        :return:铺层库优化工作栏对象
        """
        # 从Aerobook切换到子应用
        dlg_spec1 = Aero_window.child_window(auto_id="panel_Graph", control_type="System.Windows.Forms.Panel")
        dlg_spec2 = dlg_spec1.child_window(title=Aerocheck_title, class_name="wxWindowNR")
        # 点击菜单选项
        dlg_spec2.menu_select(MenuOptions)
        dlg_spec3 = dlg_spec2.scrolledpanelwxWindowNR2
        # dlg_spec3.print_control_identifiers()
        return dlg_spec3







# Entrance_module().combination_Control("铺层信息->铺层库优化")

# open_module().menu_laminateOptimize("尺寸信息->一维单元尺寸定义")