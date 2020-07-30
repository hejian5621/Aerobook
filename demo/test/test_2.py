import subprocess
import uiautomation
import time
from pywinauto.application import Application


app = Application(backend="uia").connect(process=15000)
time.sleep(3)


# 模块Aerolab、fembook、fiberbook、Aerocheck、Plybook\\
window_console = uiautomation.WindowControl(searchDepth=1, Name='Aerobook v1.0.4')  # 切换到Aerobook的控制台窗口

# window_console1=window_console.MenuItemControl(searchDepth=4,Name='铺层信息')
# window_console1.Click()
# time.sleep(1)
# window_console2=uiautomation.WindowControl(searchDepth=1, Name='Aerobook v1.0.4')
