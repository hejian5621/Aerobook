import re, time
import win32gui, win32com.client




# def window_enum_callback(hwnd, wildcard):
#     '''
#     Pass to win32gui.EnumWindows() to check all the opened windows
#     把想要置顶的窗口放到最前面，并最大化
#     '''
#     print("hwnd:", hwnd)
#     print("wildcard:",wildcard)
#     if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) is not None:
#         win32gui.BringWindowToTop(hwnd)
#         # 先发送一个alt事件，否则会报错导致后面的设置无效：pywintypes.error: (0, 'SetForegroundWindow', 'No error message is available')
#         shell = win32com.client.Dispatch("WScript.Shell")
#         shell.SendKeys('%')
#         # 设置为当前活动窗口
#         win32gui.SetForegroundWindow(hwnd)
#
#
#
#
# win32gui.EnumWindows(window_enum_callback, ".*%s.*" %"网易有道词典")#此处为你要设置的活动窗口名



class dd:

    def window_enum_callback(hwnd, wildcard):
        '''
        Pass to win32gui.EnumWindows() to check all the opened windows
        把想要置顶的窗口放到最前面，并最大化
        '''
        print("hwnd:", hwnd)
        print("wildcard:",wildcard)
        if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) is not None:
            win32gui.BringWindowToTop(hwnd)
            # 先发送一个alt事件，否则会报错导致后面的设置无效：pywintypes.error: (0, 'SetForegroundWindow', 'No error message is available')
            shell = win32com.client.Dispatch("WScript.Shell")
            shell.SendKeys('%')
            # 设置为当前活动窗口
            win32gui.SetForegroundWindow(hwnd)


    def EnumWindows(window_name):
        win32gui.EnumWindows(dd.window_enum_callback, ".*%s.*" % window_name)  # 此处为你要设置的活动窗口名

dd.EnumWindows("网易有道词典")

