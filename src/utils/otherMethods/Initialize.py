# 初始化

from config.configurationFile import ProfileDataProcessing
from pywinauto.application import Application

class programInitialization:
    """程序初始化"""


    def __init__(self):
        pass


    def open_accredit(self):
        """
        打开程序做授权操作，并打开Aerobook控制台
        :return:
        """

        app = Application().start(r"C:\Program Files (x86)\Aerobook\bin\Aerobook.exe") # 通过exe打开程序
        dlg_spec = app['Aerobook平台启动器']   # 连接Aerobook授权窗口
        # 点击请求授权按钮
        dlg_spec1 = dlg_spec1=dlg_spec.child_window(title="本地授权", auto_id="groupBox_local",
                                control_type="System.Windows.Forms.GroupBox").window(title="请求授权").click()
        dlg_spec2 = app.window(title=r'成功') # 切换到授权成功窗口
        dlg_spec2.child_window(title="确定").click() # 在授权成功窗口点击确定按钮
        # 切回到Aerobook平台启动器窗口并点击运行按钮
        app.window(title=r'Aerobook平台启动器').window(title=r'运行').click()
        # 切换到Aerobook主窗口
        Aerobook_main = app.window(title=r'Aerobook v1.0.4')
        return Aerobook_main



    def entrance_subroutine_coord(self):
        """
        进入子程序，通过坐标的方法进入
        :return:
        """



    def entrance_subroutine_title(self,Aero_title):
        """
        进入子程序,通过标题链接
        :return:
        """
        Aero_window = Application().connect(title_re=Aero_title).window(title=Aero_title)  # 通过Aerobook标题连接Aerobook
        return Aero_window















