
import win32gui,time


hwnd=win32gui.FindWindow(None,"Aerobook v1.0.5")
print ('hwnd:',hwnd)
time.sleep(1)
win32gui.EnableWindow(hwnd,True)
win32gui.SetForegroundWindow(hwnd)