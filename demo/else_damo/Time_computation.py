
from pywinauto.application import Application
import win32gui


from time import *


title="选择输出路径"

begin_time = time()

hwnd = win32gui.FindWindow(None, title)
app = Application().connect(handle=hwnd,timeout=20)  # 连接校核工况弹窗
dlg_spec = app.window(handle=hwnd)


end_time = time()
run_time = end_time - begin_time
print('该循环程序运行时间1：', run_time)


dlg_spec.print_control_identifiers()



begin_time1 = time()
app1 = Application().connect(title_re=title,timeout=20)  # 连接校核工况弹窗
dlg_spec1 = app1.window(title_re=title)

end_time = time()
run_time1 = end_time - begin_time1
print('该循环程序运行时间2：', run_time1)

dlg_spec1.print_control_identifiers()

