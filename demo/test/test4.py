
from tool import WindowTop
import win32gui

# WindowTop("Aerobook v1.0.4").EnumWindows()

WindowState=WindowTop("Aerobook v1.0.4").console()

print("WindowState:",WindowState)



