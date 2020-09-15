
# 铺层数据库制作工具弹窗

from OperatingControls.enterModule import BeingMeasured_popupWin

from src.utils.otherMethods.initialize import pywin_openAProgram



testCase_attribute={"所在模块":"载荷信息->载荷数据库制作工具"}

aero_window, son_window = pywin_openAProgram().menuOpen(testCase_attribute)
# 切入载荷数据库工具弹窗中
module_window = BeingMeasured_popupWin("载荷数据库制作工具").menu_LetsGoTopopover()


module_window.print_control_identifiers()

# # 选择载荷文件文件文本框
#
# module_window.filepicker0.Edit.set_text("ss")
#
# # 载荷数据库保存路径文本框
#
# module_window.filepicker2.Edit2.set_text("ss")

# 选择载荷文件文件浏览按钮

# module_window.filepicker0.Button1.click()

# 载荷数据库保存路径浏览按钮

# module_window.filepicker2.Button2.click()


# 开始制作按钮

module_window.Button3.click()


# 关闭按钮

# module_window.Button4.click()