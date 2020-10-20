
from tool import WindowTop
from config.configurationFile import ProfileDataProcessing
from pywinauto.application import Application
import win32gui,win32con


Popup_Title="选择Excel铺层文件"

"""在执行每一条用例之前，首先把被测窗口置顶"""
title=ProfileDataProcessing("commonality", "AerobookEdition").config_File()  # 读取配置文件信息

# title="选择Excel铺层文件"

WindowTop(title).console()


hwnd1=win32gui.GetForegroundWindow()
print("hwnd1:",hwnd1)
# 这个是qq登录界面的窗口句柄
# hwnd = win32gui.FindWindow(None, title)
# print("hwnd:",hwnd)
#
# win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 0,0,800,600, win32con.SWP_SHOWWINDOW)
