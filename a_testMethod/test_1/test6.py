import time

from pywinauto.application import Application

# 应用程序的地址
a = r"C:\Program Files (x86)\Aerobook\bin\Aerobook.exe"
#打开应用程序
app = Application("uia").start(a)


#选择应用程序
dlg_spec = app.window(title=r'Aerobook平台启动器').window(title=r'本地授权')
#点击请求授权
dlg_spec.child_window(title="请求授权").click()
time.sleep(1)
# 切换到授权成功窗口
dlg_spec1 = app.window(title=r'成功')
# 点击确定按钮Aerobook平台启动器
dlg_spec1.child_window(title="确定").click()
# 切回到Aerobook平台启动器窗口并点击运行按钮
app.window(title=r'Aerobook平台启动器').window(title=r'运行').click()
#切换到Aerobook主窗口
Aerobook_main = app.window(title=r'Aerobook v1.0.4').window(class_name=r'WindowsForms10.Window.8.app.0.141b42a_r9_ad1')
# Aerobook_main_1=Aerobook_main.window(class_name=r'WindowsForms10.Window.8.app.0.141b42a_r9_ad1')
Aerobook_main.print_control_identifiers()

# Aerobook_main_2=Aerobook_main_1.window(Name=r'Ribbon Tabs')
#
# Aerobook_main_3=Aerobook_main_2.window(Name=r'Fembook' )










