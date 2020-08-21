
from src.utils.otherMethods.initialize import programInitialization
from pywinauto.application import Application
from config.configurationFile import ProfileDataProcessing
from OperatingControls.enterModule import open_module
import sys,os


import time

# inModule="铺层信息->铺层数据库制作工具"
#
# aero_title = ProfileDataProcessing("commonality", "AerobookEdition").config_File()  # 从配置文件获取Aerobook窗口标题
# aerocheck_title = ProfileDataProcessing("commonality", "AerocheckEdition").config_File()  # 从配置文件获取Aerocheck窗口标题
#
# # 通过Aerobook标题链接Aerobook进行，并切换到Aerobook窗口
# aero_window = programInitialization().entrance_subroutine_title(aero_title)
# 通过操作菜单栏，打开被测模块，然后切换到被测模块
# module_window = open_module().menu_Laminatedata(inModule, aero_window, aerocheck_title)
app = Application().connect(title_re="铺层数据库制作工具")
dlg_spec = app.window(title="铺层数据库制作工具")
# dlg_spec1=dlg_spec.wxWindowNR.Edit.set_text(r"C:\Users\Administrator\Desktop\aro\aro1\PlyLibDb_352_541.xlsx")

# TEXT=dlg_spec.wxWindowNR.Edit85.window_text()

# dlg_spec1.print_control_identifiers()

# print("使用方法",dir(dlg_spec1.wrapper_object()))

# TEXT=dlg_spec1.Dialog.Edit.set_edit_text()


time.sleep(1)
# dlg_spec.wxWindowNR.Button.click()


# time.sleep(1)
# app1 = Application().connect(title_re="铺层数据库制作工具")





# dlg_spec6 = dlg_spec5.Toolbar
# dlg_spec6.click()  # 点击地址栏，让地址栏输入框显示出来



# print("使用方法",dir(Application().connect(title_re="选择Excel铺层文件")))

# print("TEXT:",TEXT)




# dlg_spec1=dlg_spec.wxWindowNR2.Button2
# app1=app.window(title="选择铺层数据库保存路径")


app1=app.window(title="确认另存为")

app1.print_control_identifiers()

app1.是.click()
# # 判断控件是否存在
# control = 0
# n=5
# while control <= 5:  # 检查
#     control = control + 1
#     if app1.exists():
#         print("控件存在")
#         app1.print_control_identifiers()
#         break
#     else:
#         dlg_spec1.click()
#         time.sleep(1)
# if control==(n+1):
#     print("没有找到元素")

#
# control = 1  # 循环初始次数
# n = 5
# while control <= n:  # 如果没有找到控件，就继续点击触发按钮
#     t = 1
#     if app1.exists():  # 判断窗口是否存在
#         break
#     else:  # 如果不存在点击触发按钮
#         time.sleep(t)
#     control = control + t
# if control == (n + 1):
#     print("没有找到控件", __file__, sys._getframe().f_lineno)
#     os._exit(0)
# else:
#     print("找到控件")


