# import win32gui, win32con
# hwnd = win32gui.FindWindow(None, "Aerobook v1.0.4")
#
# print(win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE))

Popup_parameter="选择输出路径；；选择文件夹"


list_AfterParsing = Popup_parameter.split("；")

print("list_AfterParsing:",list_AfterParsing)