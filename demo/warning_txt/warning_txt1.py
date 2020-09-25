






from pywinauto.application import Application
app =Application().connect(title_re="警告")
py_app = app.window(title_re="警告")

# py_app.print_control_identifiers()


py_app1=py_app.child_window(class_name="DirectUIHWND")

py_app1.print_control_identifiers()


txt=py_app1.CtrlNotifySink6.get_item_rect()

# py_app2.print_control_identifiers()

print("txt:",txt)

