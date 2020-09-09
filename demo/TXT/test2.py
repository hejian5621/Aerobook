from src.utils.otherMethods.initialize import pywin_openAProgram
from pywinauto.application import Application


# from tool import pictureProcessing,KeyboardMouse
#
#
# """在Aerobook--Aerocheck的图形区通过键盘和鼠标的操作方式选中全部的结构单元"""
#
# # KeyboardMouse().selectionModel()  # 选择结构单元
#
#
#
# """API获取图片信息"""
#
# location=r"F:\Aerobook\src\testCase\d_useCase_screenshot\1.png"
#
# actuals=pictureProcessing(location).screenshot()
#
# print("actuals:",actuals)
#

# aero_window = pywin_openAProgram().entrance_subroutine_title()
#
# main_window = Application().connect(title_re="Aerobook v1.0.4", timeout=10)
# Aerobook_main = main_window.window(title_re="Aerobook v1.0.4")
# # Aero_window =  Application().connect(title_re=self.aero_title, timeout=10)  # 通过Aerobook标题连接Aerobook
# # Aero1_window=Aero_window.window(title_re=self.aero_title).wait("exists", timeout=10, retry_interval=0.1)
# Aerobook_main.print_control_identifiers()
