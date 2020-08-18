import win32gui
import time

while True:
    window = win32gui.GetForegroundWindow()
    title = win32gui.GetWindowText(window)
    if 'GLS Exportdatei' in title:
     control = win32gui.FindWindowEx(window, 0, 'static', None)
     buffer = win32gui.PyMakeBuffer(255)
     length = win32gui.SendMessage(control, win32con.WM_GETTEXT, 255, buffer)

     result = buffer[:length]
     print (result)
     time.sleep(1)