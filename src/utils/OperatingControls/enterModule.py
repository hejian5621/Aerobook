# 打开被模块
import time
from pywinauto.application import Application




class open_module:
    """进入被测模块"""


    def __init__(self):
        pass


    def menu_laminateOptimize(self,son_window):
        """
        切换到菜单栏，点击对应的菜单选项，打开铺层库优化工作栏，切换到铺层库优化工作栏
        通过pywinauto框架执行
        :param son_window: 子窗口实体
        :return:铺层库优化工作栏对象
        """
        # 切换到铺层库优化工作栏
        dlg_spec = son_window.scrolledpanelwxWindowNR2
        # dlg_spec3.print_control_identifiers()
        return dlg_spec


    def menu_Laminatedata(self):
        """
        切换到被测弹窗
        :return:
        """
        app = Application().connect(title_re="铺层数据库制作工具")
        dlg_spec = app.window(title="铺层数据库制作工具")
        return dlg_spec


    def menu_sizeInfo_1DXls(self,son_window):
        """
        切换到菜单栏，点击对应的菜单选项，打开尺寸信息进入-一维和二维尺寸定义模块
        :return:
        """
        dlg_spec = son_window.scrolledpanelwxWindowNR2
        dlg_spec1 = dlg_spec.child_window(class_name="_wx_SysTabCtl32")
        dlg_spec2 = dlg_spec1.panelwxWindowNR2
        # dlg_spec2.print_control_identifiers()
        return dlg_spec2


    def menu_general(self,son_window):
        """
        通用菜单切换，并进入工作栏
        :param son_window:
        :return:
        """
        # 切换到铺层库数据库弹窗
        dlg_spec = son_window.scrolledpanelwxWindowNR2
        # dlg_spec3.print_control_identifiers()
        return dlg_spec