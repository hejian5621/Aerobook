

from pywinauto.application import Application

a = r"D:\Program Files (x86)\Aerobook\bin\Aerobook.exe"
app = Application().start(a)
dlg_spec = app.window(title=r'Aerobook平台启动器')


d=dlg_spec.child_window(found_index = 0,class_name = "Button", title = u"请求授权")
print("d:",d)