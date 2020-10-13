



# 获取警告弹窗文本

import subprocess
import uiautomation
from pywinauto import Application

py=Application().connect(title_re="编辑工况")

app=py.window(title_re="编辑工况")

app.print_control_identifiers()
