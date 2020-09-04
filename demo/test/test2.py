import win32api
import win32gui

def resolution():  # 获取屏幕分辨率
    return win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)

# 调用getWindowName类获取护眼宝窗口信息赋值给wname，返回一个矩形窗口四个坐标
def get_window_info():
    handle = win32gui.FindWindow(0, "警告")  # 获取窗口句柄
    if handle == 0:
         print('end', '提示：请打开护眼宝\n')
        #return None
    else:
        return win32gui.GetWindowRect(handle)
# 启动
if __name__ == "__main__":
    screen_resolution =resolution()
    window_size = get_window_info()
    print(window_size)