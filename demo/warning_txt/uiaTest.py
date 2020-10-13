

# 获取警告弹窗文本

import subprocess
import uiautomation


wc=uiautomation.WindowControl(searchDepth=1,Name='警告')

# text=wc.EditControl(searchDepth=3,ClassName="Element")

txt=wc.Control(Descendants=1,AutomationId="ContentText")

txt=txt.Exists()

# print("txt:",txt)





