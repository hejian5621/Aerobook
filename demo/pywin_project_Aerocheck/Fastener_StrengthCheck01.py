from pywinauto.application import Application


from src.utils.otherMethods.initialize import pywin_openAProgram
from OperatingControls.enterModule import BeingMeasured_popupWin


testdicts={"所在模块":"紧固件强度校核->紧固件信息输入"}
#
#
# aero_window, module_window = pywin_openAProgram().menuOpen(testdicts)
#
#
# workField1 = module_window.scrolledpanelwxWindowNR2   # 切换到被测工作
#
#
#
# workField1.print_control_identifiers()


# 向牌号文本框中输入数据

# workField1.Edit1.set_text("aa")
#
#
# # 向名称文本框中输入数据
#
# workField1.Edit2.set_text("bb")
#
#
# # 向直径文本框中输入数据
#
# workField1.Edit3.set_text("cc")


# 向双剪许用值文本框中输入数据

# workField1.Edit4.set_text("cc")


# 打开编辑参数弹窗
# workField1.Button2.click()



"""切换到编辑参数弹窗"""

# import win32gui
#
# hwnd=win32gui.FindWindow("#32770",None)   # 获取窗体的句柄
#
# print("hwnd:",hwnd)
#
#
# app = Application().connect(handle=hwnd,timeout=20)
# dlg_spec = app.window(handle=hwnd)  # 切换到选择文件弹窗窗口
#
# dlg_spec.print_control_identifiers()






"""判断弹窗是否存在"""


from OperatingControls.enterModule import BeingMeasured_popupWin,ctrW_AeroAerochcek,specialWay_OperatingControls

module="Aerobook-Aerocheck"

aero_window, module_window = pywin_openAProgram(module).menuOpen(testdicts)




window_one = ctrW_AeroAerochcek(module_window).workField_Open_EditArgument()


window_one.Edit4.set_text("cc")



