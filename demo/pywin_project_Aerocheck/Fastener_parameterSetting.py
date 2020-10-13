# 紧固件参数设置

from tool import KeyboardMouse,Check_winControl
from src.utils.otherMethods.initialize import pywin_openAProgram



testdicts={"所在模块":"紧固件强度校核->紧固件参数设置"}


aero_window, module_window = pywin_openAProgram().menuOpen(testdicts)


workField1 = module_window.scrolledpanelwxWindowNR2   # 切换到被测工作



workField1.print_control_identifiers()

print("________________________")



"""连接板1参数设置"""

# # 连接板1参数设置--挤压许用应力设置
# workField1.Edit1.set_text("10")
#
#
#
# # 连接板1参数设置--紧固件牌号
# workField1.ComboBox0.select("CFBL1002-4")
#
#
# # 连接板1参数设置--紧固件排数文本框
# workField1.Edit2.set_text("15")
#
#
# # 连接板1参数设置--紧固件排数选择框
# workField1.ComboBox2.select("2")
#
#
# # 连接板1参数设置--紧固件个数
# workField1.Edit3.set_text("10")
#
#
# # 连接板1参数设置--连接件参数设置
# workField1.Edit4.set_text("10")
#
# # 连接板1参数设置--选择结构单元
# workField1.Button1.click()
# KeyboardMouse().selectionModel()  # 选择结构单元
#
# # 连接板1参数设置--确认
# workField1.Button2.click()



"""连接板2参数设置"""
# 连接板2参数设置--挤压许用应力设置


workField1.GroupBox3.click_input(coords = (150,30))

# w=workField1.child_window(title="挤压许用应力设置：", class_name="Static")

workField1.child_window(class_name="Edit").set_text("100")



# workField1.print_control_identifiers()

OK=u'挤压许用应力设置：Edit2'

# workField1["Button"].click()

# w.Edit6.set_text("100")

# work=workField1.Edit6



# txtx=work.get_properties()

# print("txtx:",txtx)


# # 连接板2参数设置--选择结构单元
# workField1.Button3.click()
# KeyboardMouse().selectionModel()  # 选择结构单元
#
#
#
# # 连接板2参数设置--确认
# workField1.Button4.click()




"""方法测试"""


import win32gui

# txt=work.is_visible()

# work.print_control_identifiers()

# hwnd=win32gui.FindWindow(None,work)



# print("txt:",txt)