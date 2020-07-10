# 客户初始化，打开应用程序
from pywinauto.application import Application


class ClientInitialization:
    """k客初始化"""

    def __init__(self):
        pass

    def open_Aerobook(self, ApplicationAddress):
        """
       打开Aer0book，并授权
       :param ApplicationAddress:应用程序地址
       :return:
       """
        # 打开应用程序
        app = Application().start(r"%s" % ApplicationAddress)
        # 选择应用程序
        dlg_spec = app.window(title=r'Aerobook平台启动器').window(title=r'本地授权')
        # 点击请求授权
        dlg_spec.child_window(title="请求授权").click()
        # 切换到授权成功窗口
        dlg_spec1 = app.window(title=r'成功')
        # 点击确定按钮
        dlg_spec1.child_window(title="确定").click()
        # 切回到Aerobook平台启动器窗口，点击运行按钮
        app.window(title=r'Aerobook平台启动器').window(title=r'运行').click()
        Aerobook_main = app.window(title=r'Aerobook v1.0.4')
        return Aerobook_main


    def open_Aerolab(self,application):
        """
        点击Aerolab按钮，打开Aerolab
        :param application:
        :return:
        """
        # 打开Aerolab
        Aerobook_main_tool=application.window(auto_id="panel_Page",control_type="System.Windows.Forms.Panel").\
            window(auto_id="RibbonControl1").click()
        return Aerobook_main_tool




    def  manual_open_module(self,application):
        """
        手动打开模块
        :param application:
        :return:
        """
















