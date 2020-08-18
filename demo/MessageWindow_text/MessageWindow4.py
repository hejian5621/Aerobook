import subprocess
import uiautomation

import time
wc=uiautomation.WindowControl(searchDepth=1,Name="警告")
time.sleep(2)
text=wc.TextControl(searchDepth=4,Name="请选择铺层库Excel文件!").GetTextPattern()

print("text:",text)