from pywinauto.application import Application
















"""获取紧固件参数工作栏中编辑参数弹窗"""


import win32gui,time


hwnd=win32gui.FindWindow(None,"Aerobook v1.0.4")   # 获取窗体的句柄
#
#
# # hwnd=win32gui.FindWindow("Button",None)   # 获取窗体的句柄
#
#
#
# # hwnd=win32gui.FindWindow(None,"wxWindowNR")   # 获取窗体的句柄
#
#
#
#
# # app = Application().connect(handle=hwnd,timeout=20)
# # dlg_spec = app.window(handle=hwnd)  # 切换到选择文件弹窗窗口
#
# # dlg_spec.print_control_identifiers()
#
#
#
#
# hwnd=win32gui.FindWindow(None,"Aerobook v1.0.4")   # 获取窗体的句柄
#
# print("hwnd:",hwnd)
#
# hwnd1=win32gui.FindWindowEx(hwnd, 0, None, "Aerobook v1.0.4")
#
# print("hwnd1:",hwnd1)






def find_idxSubHandle(pHandle, winClass, index=0):
    """
    已知子窗口的窗体类名
    寻找第index号个同类型的兄弟窗口
    """
    assert type(index) == int and index >= 0
    handle = win32gui.FindWindowEx(pHandle, 0, winClass, None)
    while index > 0:
        handle = win32gui.FindWindowEx(pHandle, handle, winClass, None)
        index -= 1
    return handle


def find_subHandle(pHandle, winClassList):
    """
    递归寻找子窗口的句柄
    pHandle是祖父窗口的句柄
    winClassList是各个子窗口的class列表，父辈的list-index小于子辈
    """
    assert type(winClassList) == list
    if len(winClassList) == 1:
        return find_idxSubHandle(pHandle, winClassList[0][0], winClassList[0][1])
    else:
        pHandle = find_idxSubHandle(pHandle, winClassList[0][0], winClassList[0][1])
        return find_subHandle(pHandle, winClassList[1:])



handle = find_subHandle(hwnd, [("wxWindowNR", 1)])
print("handle:",handle)

