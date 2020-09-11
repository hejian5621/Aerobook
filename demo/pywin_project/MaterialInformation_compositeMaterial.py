# 材料信息--复合材料需用值定义

from config.configurationFile import ProfileDataProcessing
from src.utils.otherMethods.initialize import pywin_openAProgram
from src.utils.otherMethods.initialize import execute_useCase_initialize
from OperatingControls.enterModule import BeingMeasured_popupWin,specialWay_OperatingControls,BeingMeasured_work
import uiautomation
from pywinauto.application import Application
import time


#
# testdicts={"所在模块":"材料信息->定义复合材料参数"}
#
#
# operationWindow="定义材料许用值"
#
# son_window = execute_useCase_initialize().link_window()  # 链接被测程序
# module_window = BeingMeasured_work(son_window).workField_composite_information() # 切换到被测模块
#
#
# # 点击选项卡
# aero_title = ProfileDataProcessing("commonality", "AerobookEdition").config_File()  # 从配置文件获取Aerobook窗口标题
# Use = uiautomation.WindowControl(searchDepth=1, Name=aero_title)
#
# specialWay_OperatingControls(operationWindow).uia_OperatingControls()  # 使用uiautomation框架点击切换模块
#
# module_window.print_control_identifiers()



# dlg_spec.print_control_identifiers()






"""获取”编辑材料许用值“中的值"""

# 点击创建材料需用值曲线
# module_window.Button1.click()


"""连接编辑材料许用值曲线弹框"""
dlg_spec3=BeingMeasured_popupWin("编辑材料许用值曲线").menu_LetsGoTopopover()


dlg_spec3.print_control_identifiers()

# """编辑材料许用值曲线弹框中"""
# # 曲线名称
# dlg_spec3.Edit.set_text("aa")


# 确认
# dlg_spec3.Button2.click()



# 切换到网格窗口
# dlg_spec5=dlg_spec3.child_window(title="GridWindow", class_name="wxWindowNR")
# # 在第一行,X轴
# dlg_spec5.double_click_input(coords = (40, 20),button ="left")
# dlg_spec5.Edit.set_text("0")
#
#
# txt=dlg_spec5.Edit.window_text()
#
# print("txt：",txt)
#




"""切换到定义材料需用值"""
# 点击"拉伸"对于的"+"按钮
# module_window.Button0.click()
#
#
# # 点击"压缩"对于的"+"按钮
# module_window.Button2.click()
#
#
# # 点击"剪切"对于的"+"按钮
# module_window.Button3.click()




# # 在曲线文本框中输入内容
# dlg_spec3.Edit2.set_text("sa")
#
# # 切换到网格窗口
# dlg_spec5=dlg_spec3.child_window(title="GridWindow", class_name="wxWindowNR")
# # 在第一行,X轴
# dlg_spec5.double_click_input(coords = (40, 20),button ="left")
# dlg_spec5.Edit.set_text("0")
#
# # # 在第一行,Y轴
# dlg_spec5.double_click_input(coords = (180, 20),button ="left")
# dlg_spec5.Edit.set_text("4500")
#
# dlg_spec3.Edit2.set_text("sa")
#
# dlg_spec3.确认.click()



# # 第二行,X轴
# dlg_spec5.double_click_input(coords = (40, 40),button ="left")
# # 第二行,Y轴
# dlg_spec5.double_click_input(coords = (180, 40),button ="left")


# # 第三行,X轴
# dlg_spec5.click_input(coords = (40, 60),double = True)
# # 第三行,Y轴
# dlg_spec5.double_click_input(coords = (180, 60),button ="left")


# dlg_spec5.print_control_identifiers()

print("__________________________________________________")





"""定义材料许用值"""
# 点击"拉伸"对于的"+"按钮
# dlg_spec1.Button0.click()

# dlg_spec1.print_control_identifiers()
#
# dlg_spec3=BeingMeasured_popupWin("选择材料许用值曲线").menu_LetsGoTopopover()
#
# dlg_spec4=dlg_spec3.child_window(title="GridWindow", class_name="wxWindowNR")
#
#
#
# dlg_spec4.double_click_input(coords=(50, 10), button="left")
#
# dlg_spec3.print_control_identifiers()
#
# dlg_spec3.确认.move_mouse()

# dlg_spec3.确认.click()

#


from tool import instrument

# 选择结构单元
# dlg_spec1.child_window(title="选择结构单元", class_name="Button").click()
#
# instrument().selectionModel()








