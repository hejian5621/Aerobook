import win32gui, win32con
hwnd = win32gui.FindWindow(None, "Aerobook v1.0.4")

print(win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE))
#
#
# win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 0,0,800,600, win32con.SWP_SHOWWINDOW)
#
#
# print(win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE))


# HWND GetForegroundWindow( void)
