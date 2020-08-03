# 点击警告弹窗的OK按钮


from pywinauto.application import Application

import time

time.sleep(3)
app = Application().connect(title_re="警告")

dlg_spec = app.window(title="警告")


dlg_spec.capture_as_image().save('123.png')

dlg_spec.child_window(title="OK", class_name="Button").Click()