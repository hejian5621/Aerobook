import time

from pywinauto.application import Application
# 应用程序的地址
a = r"E:\Program Files (x86)\Aerobook\bin\Aerobook.exe"
#打开应用程序
app = Application().start(a)
#选择应用程序
dlg_spec = app.window(title=r'Aerobook平台启动器').window(title=r'本地授权')
#点击请求授权
dlg_spec.child_window(title="请求授权").click()
# 切换到授权成功窗口
dlg_spec1 = app.window(title=r'成功')
# 点击确定按钮Aerobook平台启动器
dlg_spec1.child_window(title="确定").click()
# 切回到Aerobook平台启动器窗口并点击运行按钮
app.window(title=r'Aerobook平台启动器').window(title=r'运行').click()
#切换到Aerobook主窗口
Aerobook_main = app.window(title=r'Aerobook v1.0.4')

Aerobook_main_1=Aerobook_main.window(title=r'正在启动应用程序，需要一定的时间，请耐心等待...')
Aerobook_main_2=Aerobook_main_1.window(title=r'The Ribbon')
Aerobook_main_3=Aerobook_main_2.window(title=r'Ribbon Tabs')
Aerobook_main_4=Aerobook_main_3.window(title=r'Fembook').click()
# Aerobook_main.print_control_identifiers()
# 切换到工具栏
#打开Aerolab
# Aerobook_main_tool=Aerobook_main.window(auto_id="panel_Page",control_type="System.Windows.Forms.Panel").\
#     window(auto_id="RibbonControl1").click()

#打开Aerolab
# Aerobook_main_tool=Aerobook_main.window(auto_id="panel_Page",control_type="System.Windows.Forms.Panel").\
#     window(auto_id="RibbonControl1").click()
# time.sleep(1)

#
# Aerobook_main_tool=Aerobook_main.\
#     child_window(auto_id="panel_Graph", control_type="System.Windows.Forms.Panel").click()

# time.sleep(10)
Aerobook_main.print_control_identifiers()














