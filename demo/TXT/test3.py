
from config.configurationFile import ProfileDataProcessing

import time
from pywinauto.application import Application
from pywinauto.keyboard import send_keys
from tool import instrument,Check_winControl
from pywinauto import mouse
from pykeyboard import PyKeyboard
from pywinauto  import  findwindows
from OperatingControls.enterModule import BeingMeasured_popupWin


app = Application().connect(title="项目设置", timeout=20)  # 连接项目设置弹窗
dlg_spec = app.window(title="项目设置")
    # app.window(title="项目设置").maximize()  # 项目弹窗最大化
x = int(ProfileDataProcessing("commonality", "coord1_x").config_File())  # 从配置文件获取鼠标点击坐标
y = int(ProfileDataProcessing("commonality", "coord1_y").config_File())  # 从配置文件获取鼠标点击坐标
dlg_spec.click_input(button='left', coords=(x, y))  # 点击有限元模型路径对应的文本框，显示出文本框
DetailedPath = r"F:\Aerobook\src\testCase\projectFile\automateFile" + "\Htail.fem"
dlg_spec.Edit.wait("exists", timeout=60, retry_interval=1).set_text(DetailedPath)  # 在有限元模型路径对应的文本框中输入数据
# time.sleep(1)
# dlg_spec.print_control_identifiers()
dlg_spec.wxPropertyGrid.click_input()
Check_winControl("项目设置", "完成").nest_popUpWindows("警告", "OK")  # 检查嵌套弹窗是否关闭