# 初始化


class programInitialization:
    """程序初始化"""


    def __init__(self):
        pass


    def open_accredit(self):
        """
        打开程序做授权操作，并打开Aerobook控制台
        :return:
        """


    def entrance_subroutine_coord(self):
        """
        进入子程序，通过坐标的方法进去
        :return:
        """



    def entrance_subroutine_title(self):
        """
        进入子程序,通过标题链接
        :return:
        """

import subprocess
import uiautomation
import time

class ClientInitialization:
    """Aerobook程序初始化"""

    def __init__(self):
        pass

    def open_Aerobook(self, ApplicationAddress):
        """
       打开Aerobook，并授权
       :param ApplicationAddress:应用程序地址
       :return:
       """
        a = r"E:\Program Files (x86)\Aerobook\bin\Aerobook.exe"
        subprocess.Popen(a)  # 启动Aerobook.exe
        window_impower = uiautomation.WindowControl(searchDepth=1, Name='Aerobook平台启动器')  # 找到Aerobook平台启动器窗口
        authority = window_impower.Control(searchDepth=1, Name='本地授权')  # 找到本地授权控件
        authority.ButtonControl(searchDepth=1, Name='请求授权').Click()  # 找到请求授权按钮,并点击
        time.sleep(1)  # 等待一秒
        popup = window_impower.Control(searchDepth=1, Name='成功')  # 找到成功弹窗
        popup.ButtonControl(searchDepth=1, Name='确定').Click()  # 在弹出的成功窗口中点击确定按钮
        window_impower.ButtonControl(searchDepth=1, Name='运行').Click()  # 在Aerobook平台启动器窗口中点击运行按钮
        time.sleep(2)  # 等待两秒


    def open_Aerolab(self,module):
        """
        点击Aerolab按钮，打开Aerolab
        :param module:需要点击的模块
        :return:
        """
        # 模块Aerolab、fembook、fiberbook、Aerocheck、Plybook
        window_console = uiautomation.WindowControl(searchDepth=1, Name='Aerobook v1.0.4')  # 切换到Aerobook的控制台窗口

        window_console.ShowWindow(uiautomation.ShowWindow.Maximize)
        sub3 = window_console.Control(searchDepth=1, Name='正在启动应用程序，需要一定的时间，请耐心等待...',
                               className="WindowsForms10.Window.8.app.0.141b42a_r9_ad1")
        sub4 = sub3.Control(searchDepth=1, Name='The Ribbon')
        sub5 = sub4.Control(searchDepth=1, Name='Ribbon Tabs')
        sub5.TabItemControl(searchDepth=1, Name=module).Click()








# 客户初始化，打开应用程序
import subprocess
import uiautomation
import time
from pywinauto.application import Application


class ClientInitialization:
    """1、Aerobook授权
       2、打开对应得应用
    """

    def __init__(self):
        pass

    def open_Aerobook(self, ApplicationAddress):
        """
       打开Aerobook，并授权
       :param ApplicationAddress:应用程序地址
       :return:
       """
        subprocess.Popen(ApplicationAddress)  # 启动Aerobook.exe
        window_impower = uiautomation.WindowControl(searchDepth=1, Name='Aerobook平台启动器')  # 找到Aerobook平台启动器窗口
        authority = window_impower.Control(searchDepth=1, Name='本地授权')  # 找到本地授权控件
        authority.ButtonControl(searchDepth=1, Name='请求授权').Click()  # 找到请求授权按钮,并点击
        time.sleep(1)  # 等待一秒
        popup = window_impower.Control(searchDepth=1, Name='成功')  # 找到成功弹窗
        popup.ButtonControl(searchDepth=1, Name='确定').Click()  # 在弹出的成功窗口中点击确定按钮
        window_impower.ButtonControl(searchDepth=1, Name='运行').Click()  # 在Aerobook平台启动器窗口中点击运行按钮
        time.sleep(2)  # 等待两秒


    def open_Aerocheck(self,module):
        """
        点击Aerolab按钮，打开Aerolab
        :param module:需要点击的模块
        :return:
        """
        time.sleep(5)
        # 模块Aerolab、fembook、fiberbook、Aerocheck、Plybook
        window_console = uiautomation.WindowControl(searchDepth=1, Name='Aerobook v1.0.4')  # 切换到Aerobook的控制台窗口
        #最大化
        window_console.ButtonControl(searchDepth=2, Name='最大化').Click()
        sub3 = window_console.Control(searchDepth=1, Name='正在启动应用程序，需要一定的时间，请耐心等待...',
                               className="WindowsForms10.Window.8.app.0.141b42a_r9_ad1")
        sub4 = sub3.Control(searchDepth=1, Name='The Ribbon')
        sub5 = sub4.Control(searchDepth=1, Name='Ribbon Tabs')
        sub5.TabItemControl(searchDepth=1, Name=module).Click()


class ConnectApp:
    """连接应用程序"""

    def __init__(self,title):
        """
        :param title:  pywinauto是标题，uiautomation是名称
        """
        self.title=title

    def pyw_Connect(self):
        """
         pywinauto通过应用程序标题（title）连接到应用程序
        :return:
        """
        app=None
        # 通过应用标题连接到应用
        try:
            app = Application().connect(title_re=self.title)  # 通过应用标题连接到该应用的进程
        except:
            print("没有找到被测应用窗口的标题，请检查是否没有打开应用" ,__file__, sys._getframe().f_lineno)
        dlg_spec = app.window(title=self.title)  # 切换到应用的窗口
        return dlg_spec  #返回应用对象


    def uia_Connect(self):
        """
        uiavtomation通过应用程序名称（Name）连接到应用程序
        :return:
        """
        # 通过应用名称连接到应用，searchDepth搜索深度
        app = uiautomation.WindowControl(searchDepth=1, Name=self.title)
        return app






