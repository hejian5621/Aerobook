# 打开被模块
import time,sys,os
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
        from pywinauto import findwindows
        n = 0;dlg_spec = None;k = 5;err = None
        while n < k:
            try:
                app = Application().connect(title_re="铺层数据库制作工具")
                dlg_spec = app.window(title="铺层数据库制作工具")
            except findwindows.ElementNotFoundError as err:  # 如果没有找到编辑工况窗口继续循环找
                time.sleep(0.2)
            except Exception as err:
                print(err, __file__, sys._getframe().f_lineno)
                os._exit(0)
            n = n + 1
        if n >= k:
            print("没有找到“铺层数据库制作工具”弹框")
            print(err, __file__, sys._getframe().f_lineno)
            os._exit(0)
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


    def menu_editWorkingCondition(self):
        """
        切换到编辑工况弹窗中
        :return:
        """
        from pywinauto import findwindows
        n=0;dlg_spec=None;k=5;err=None
        while n<k:
            try:
                app = Application().connect(title_re="编辑工况")
                dlg_spec = app.window(title="编辑工况")
            except findwindows.ElementNotFoundError as err:   # 如果没有找到编辑工况窗口继续循环找
                time.sleep(0.2)
            except Exception as err:
                print(err, __file__, sys._getframe().f_lineno)
                os._exit(0)
            else:
                break
            n = n + 1
        if n>=k:
            print("没有找到“编辑工况”弹框")
            print(err, __file__, sys._getframe().f_lineno)
            os._exit(0)
        return dlg_spec