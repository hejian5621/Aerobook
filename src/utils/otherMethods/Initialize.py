# 初始化

from pywinauto.application import Application
import os
import shutil
from config.relative_location import  path
from pathlib import Path


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


    def copyFile(self):
        """
        复制文件夹或者文件
        :return:
        """
        relativeAddress = path.location()  # 获取项目相对位置
        target = relativeAddress + r"src\testCase\projectFile\自动化测试相关文件"  # 被复制文件的详细路径
        source = relativeAddress + r"\src\testCase\projectFile\automateFile"  # 被复制文件的详细路径
        source_path = os.path.abspath(target)
        target_path = os.path.abspath(source)
        if not os.path.exists(target_path):
            os.makedirs(target_path)
        if os.path.exists(source_path):
            # root 所指的是当前正在遍历的这个文件夹的本身的地址
            # dirs 是一个 list，内容是该文件夹中所有的目录的名字(不包括子目录)
            # files 同样是 list, 内容是该文件夹中所有的文件(不包括子目录)
            for root, dirs, files in os.walk(source_path):
                for file in files:
                    src_file = os.path.join(root, file)
                    shutil.copy(src_file, target_path)
            print('被测文件“%s“生成完成'%source)
        return source



    def delFile(self):
        """
        强制删除文件夹
        :return:
        """
        relativeAddress = path.location()  # 获取项目相对位置
        source = relativeAddress + r"\src\testCase\projectFile\automateFile"  # 被复制文件的详细路径
        if os.path.isdir(r"F:\Aerobook\\src\testCase\projectFile\automateFile"):
            shutil.rmtree(source)
            print('文件“%s“删除完毕' % source)













