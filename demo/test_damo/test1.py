
import win32gui



hwnd = win32gui.FindWindow(None, "multiSplitter")  # 通过弹窗的标题获取弹窗的句柄

print("hwnd:",hwnd)