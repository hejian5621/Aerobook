

from pywinauto.application import Application
# 应用程序的地址
a = r"C:\Program Files (x86)\Aerobook\bin\Aerobook.exe"
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
Aerobook_main=app.window(title=r'Aerobook v1.0.4')
# 切换到工具栏
Aerobook_main_tool=Aerobook_main.child_window(auto_id="ribbonStatusBar1")
# 打印控件
Aerobook_main.print_control_identifiers()





