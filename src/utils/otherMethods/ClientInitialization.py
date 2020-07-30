# 客户初始化，打开应用程序
import subprocess
import uiautomation
import time

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



#
# class ProcesslinkApplication:
#
#     def __init__(self):
#         pass
#
#
#     def Aia_link(self):
