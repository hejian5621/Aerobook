#coding:utf-8

#coding=utf-8
import win32gui
import win32api
import win32con

# 获取主窗口句柄
f = win32gui.FindWindow("警告",None)
print (f,win32gui.GetWindowText(f))

#获取主窗口的子窗口句柄
ex=win32gui.FindWindowEx(f,None,"DirectUIHWND",None)

#获取子窗口ex窗口的句柄
exx=win32gui.FindWindowEx(ex,None,"CtrlNotifySink",None)

SB_GETTEXT = win32con.WM_USER + 2
SB_GETTEXTLENGTH = win32con.WM_USER + 3

sub_item = 0

sb_retcode = win32api.SendMessage(exx, SB_GETTEXTLENGTH, sub_item, 0)
sb_type = sb_retcode & 0xFFFF
sb_length = (sb_retcode >> 16) & 0xFFFF

text_buffer = win32gui.PyMakeBuffer(1 + sb_length)
sb_retcode = win32api.SendMessage(exx, SB_GETTEXT, sub_item, text_buffer)

print (text_buffer)