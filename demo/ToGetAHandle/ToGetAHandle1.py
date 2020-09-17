from pywinauto.application import Application

import win32gui,time


# hwnd=win32gui.FindWindow(None,"Aerobook v1.0.5")   # 获取窗体的句柄


# hwnd=win32gui.FindWindow("#32770",None)   # 获取窗体的句柄



hwnd=win32gui.FindWindow(None,"wxWindowNR")   # 获取窗体的句柄

print("hwnd:",hwnd)


# app = Application().connect(handle=hwnd,timeout=20)
# dlg_spec = app.window(handle=hwnd)  # 切换到选择文件弹窗窗口
#
# dlg_spec.print_control_identifiers()