# 点击警告弹窗的OK按钮


from pywinauto.application import Application

import time

time.sleep(2)
app = Application().connect(title_re="警告")

dlg_spec = app.window(title="警告")

dlg_spec1=dlg_spec.child_window(class_name="DirectUIHWND")



dlg_spec2=dlg_spec1.CtrlNotifySink0

dlg_spec1.print_control_identifiers()
print("__________________________________________")

dlg_spec2.print_control_identifiers()
dlg_spec2.capture_as_image().save('456.png')

# dlg_spec1=dlg_spec.child_window(title="OK", class_name="Button").Click()





