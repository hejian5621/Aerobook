# 初始化

from pywinauto.application import Application
import subprocess
import uiautomation
from config.configurationFile import ProfileDataProcessing
from pywinauto import mouse
from src.utils.otherMethods.controlOperationSuite import ControlOperationSuite

import time
from config.relative_location import  path
from pathlib import Path


class programInitialization:
    """程序初始化"""


    def __init__(self,windowTitle):
        # 窗口标题
        self.windowTitle=windowTitle


    def open_accredit(self):
        """
        打开程序做授权操作，并打开Aerobook控制台
        :return:
        """
        # 读取配置文档信息
        aero_title = ProfileDataProcessing("commonality", "exe").config_File()  # 从配置文件获取Aerobook窗口标题
        app = Application().start(aero_title) # 通过exe打开程序
        dlg_spec = app['Aerobook平台启动器']   # 连接Aerobook授权窗口
        # 点击请求授权按钮
        dlg_spec1 = dlg_spec1=dlg_spec.child_window(title="本地授权", auto_id="groupBox_local",
                                control_type="System.Windows.Forms.GroupBox").window(title="请求授权").click()
        dlg_spec2 = app.window(title=r'成功') # 切换到授权成功窗口
        dlg_spec2.child_window(title="确定").click() # 在授权成功窗口点击确定按钮
        # 切回到Aerobook平台启动器窗口并点击运行按钮
        app.window(title=r'Aerobook平台启动器').window(title=r'运行').click()
        # 切换到Aerobook主窗口
        Aerobook_main = app.window(title=self.windowTitle)
        Aerobook_main.wait("exists",timeout=5,retry_interval=0.01)
        Aerobook_main.Maximize()
        return Aerobook_main



    def entrance_subroutine_coord(self):
        """
        进入子程序，通过坐标的方法进入
        :return:
        """




    def entrance_subroutine_title(self):
        """
        进入子程序,通过标题链接
        :return:
        """
        Aero_window = Application().connect(title_re=self.windowTitle).window(title=self.windowTitle)  # 通过Aerobook标题连接Aerobook
        return Aero_window



    def EntrySubapplication(self,childApp_Title):
        """
        进入子应用
        点击“Aerocheck”按钮
        :param childApp_Title:
        :return:
        """
        # 连接Aerobook控制台窗口进程
        Use = uiautomation.WindowControl(searchDepth=1, Name=self.windowTitle)
        # 点击子应用，进入子应用
        Use.Control(searchDepth=4,Name=childApp_Title).Click()
        return Use




















