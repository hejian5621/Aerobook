
# 铺层数据库制作工具弹窗

from OperatingControls.enterModule import BeingMeasured_popupWin

from src.utils.otherMethods.initialize import pywin_openAProgram



testCase_attribute={"所在模块":"铺层信息->铺层数据库制作工具"}

aero_window, son_window = pywin_openAProgram().execute_useCase_enterInto(testCase_attribute)
# 切入铺层数据库工具弹窗中
module_window = BeingMeasured_popupWin("铺层数据库制作工具").menu_LetsGoTopopover()


module_window.print_control_identifiers()

# # 选择铺层Excel文件文本框
#
# module_window.filepicker0.Edit.set_text("ss")
#
# # 铺层数据保存路径文本框
#
# module_window.filepicker2.Edit2.set_text("ss")

# 选择铺层Excel文件浏览按钮

# module_window.filepicker0.Button1.click()

# 铺层数据保存路径浏览按钮

# module_window.filepicker2.Button2.click()


# 模板文件按钮

module_window.Button3.click()