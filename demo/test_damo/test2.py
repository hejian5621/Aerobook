
from tool import WindowTop
from config.configurationFile import ProfileDataProcessing
from pywinauto.application import Application
import win32gui


Popup_Title="选择Excel铺层文件"

"""在执行每一条用例之前，首先把被测窗口置顶"""
title=ProfileDataProcessing("commonality", "AerobookEdition").config_File()  # 读取配置文件信息
WindowTop(title).console()
hwnd = win32gui.FindWindow(None, Popup_Title)

app = Application().connect(handle=hwnd, timeout=20)
dlg_spec = app.window(handle=hwnd)  # 切换到选择文件弹窗窗口
# 切换控件
dlg_spec1 = dlg_spec.child_window(class_name="WorkerW")
dlg_spec2 = dlg_spec1.child_window(class_name="ReBarWindow32")
dlg_spec3 = dlg_spec2.child_window(class_name="Address Band Root")
dlg_spec4 = dlg_spec3.child_window(class_name="msctls_progress32")  # 切换到选择文件弹窗中的地址栏
dlg_spec5 = dlg_spec4.child_window(class_name="Breadcrumb Parent")
dlg_spec5.print_control_identifiers()


dlg_spec6 = dlg_spec5.Toolbar
dlg_spec6.click_input(coords = (10, 10))  # 点击地址栏，让地址栏输入框显示出来