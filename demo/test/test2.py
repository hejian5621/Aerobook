
from src.utils.otherMethods.initialize import pywin_openAProgram
from OperatingControls.enterModule import BeingMeasured_popupWin
from tool import KeyboardMouse,Check_winControl
from pywinauto.application import Application

# try:
#     app = Application().connect(title_re="")
#     py_app = app.window(title_re="铺层数据库制作工具")  # 切换到需要关闭的窗口
# except:
#     break
#
# else:


app = Application().connect(title_re="警告")
py_app = app.window(title_re="警告")  # 切换到需要关闭的窗口
# window_one=py_app.Button1

# PopupTitle="选择Excel铺层文件"


# Check_winControl(PopupTitle, window_one).window_WhetherOpen()  # 判断预期窗口是否出现