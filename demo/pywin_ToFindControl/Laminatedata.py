#铺层数据库制作工具



from src.utils.otherMethods.initialize import programInitialization
from pywinauto.application import Application
from config.configurationFile import ProfileDataProcessing

import sys,os
from src.utils.otherMethods.initialize import execute_useCase_initialize
import time
from tool import Check_winControl




from tool import WindowTop
# 被系统置顶
WindowTop.EnumWindows("Aerobook v1.0.4")



testdicts={"所在模块":"铺层信息->铺层数据库制作工具"}

# 链接“铺层数据库制作工具”弹窗
app = Application().connect(title_re="铺层数据库制作工具")
dlg_spec = app.window(title="铺层数据库制作工具")

dlg_spec.click()

dlg_spec1=dlg_spec.filepickerwxWindowNR

dlg_spec1.click()


dlg_spec1.click()

dlg_spec1.click()


# dlg_spec1.print_control_identifiers()


# print("使用方法",dir(dlg_spec1.wrapper_object()))

dlg_spec2=dlg_spec1.child_window(title="...", class_name="Button")

print("a")

Check_winControl("选择Excel铺层文件",dlg_spec2).window_WhetherOpen()

print("b")
# 链接“选择Excel铺层文件”弹窗
app = Application().connect(title_re="选择Excel铺层文件")
dlg2_spec = app.window(title="选择Excel铺层文件")
# dlg2_spec.print_control_identifiers()
print("c")

dlg2_spec1=dlg2_spec.ComboBoxEx1

dlg2_spec1.Edit1.set_text("aaa")





























