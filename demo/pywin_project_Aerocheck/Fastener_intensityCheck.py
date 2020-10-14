from tool import KeyboardMouse,Check_winControl
from src.utils.otherMethods.initialize import pywin_openAProgram



testdicts={"所在模块":"紧固件强度校核->紧固件强度校核"}

module="Aerobook-Aerocheck"
aero_window, module_window = pywin_openAProgram(module).menuOpen(testdicts)


workField1 = module_window.scrolledpanelwxWindowNR2   # 切换到被测工作

workField1.print_control_identifiers()


# 安全系数文本框输入数据
workField1.Edit1.set_text("1.11")


# 钉载面内分配系数文本框输入数据
workField1.Edit2.set_text("2.22")


# 热载荷分配系数文本框输入数据
workField1.Edit3.set_text("3.33")

# 旁路分配系数文本框输入数据
workField1.Edit4.set_text("4.44")


# 选择工况

workField1.Button1.click_input()

#
# from pywinauto.application import Application
# app = Application().connect(title="选择优化工况",timeout=20)  # 连接校核工况弹窗
# dlg_spec = app.window(title="选择优化工况")
# dlg_spec.print_control_identifiers()



from src.utils.otherMethods.ControlOperationSuite_Aercheck import ControlOperationSuite_Aercheck
ControlOperationSuite_Aercheck(None).select_workingCondition("选择优化工况")



# 选择极值
workField1.RadioButton2.click_input()


# 选择均值
workField1.RadioButton1.click_input()


# 点击校核按钮
workField1.Button2.click_input()