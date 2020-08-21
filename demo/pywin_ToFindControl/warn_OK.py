# # 点击警告弹窗的OK按钮
#
import win32api,win32con
# import warnings


import tkinter.messagebox #这个是消息框，对话框的关键

# from pywinauto import win32defines
# from pywinauto import findwindows
# from pywinauto import application
# #
#
# from pywinauto.application import Application
# from pywinauto import taskbar
#
# import time
#
#
#
# time.sleep(3)
# app = Application().connect(title_re="提醒")
#
# dlg_spec = app.window(title="提醒")
#
# dlg_spec1=dlg_spec.Element
#
# # TaskBar = dlg_spec.window_(handle = TaskBarHandle())
#
# dlg_spec1.print_control_identifiers()
#
# # TXT=dlg_spec1.SysLink.window_text()
#
# # TXT=dlg_spec1.Dialog.SysLink.window_text()
#
# # TXT=dlg_spec1.taskbar.SystemTrayIcons.WrapperObject().window_text()
# print("TXT:",TXT)
#


#
# # 生成 buffer 对象
# import win32con
# from win32gui import PyMakeBuffer, SendMessage, PyGetBufferAddressAndLen, PyGetString
#
# length = 10000
#
# # hWnd=68214
# hWnd=68302
#
# buf = PyMakeBuffer(length)
# length2 = SendMessage(hWnd, win32con.WM_GETTEXT, length, buf)+1
# print(length2)
# buf = PyMakeBuffer(length2)
# print('get: ', SendMessage(hWnd, win32con.WM_GETTEXT, length2, buf))
#
# address, length = PyGetBufferAddressAndLen(buf)
# text = PyGetString(address, length)
#
# print('text: ', text)

#提醒OK消息框


# win32api.MessageBox(0, "这是一个测试警告信息框", "提醒",win32con.MB_ICONWARNING)

tkinter.messagebox.showerror('错误','出错了')