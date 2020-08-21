import time

from pywinauto.application import Application
from pywinauto.keyboard import send_keys


time.sleep(2)
# app = Application().connect(title_re="选择输出路径")
# dlg_spec = app.window(title="选择输出路径")

# app = Application().connect(title_re="选择Excel铺层文件")
# dlg_spec = app.window(title="选择Excel铺层文件")

app = Application().connect(title_re="选择铺层数据库保存路径")
dlg_spec = app.window(title="选择铺层数据库保存路径")



dlg_spec1 = dlg_spec.child_window(class_name="WorkerW")


dlg_spec2 = dlg_spec1.child_window(class_name="ReBarWindow32")

dlg_spec3 = dlg_spec2.child_window(class_name="Address Band Root")

dlg_spec4 = dlg_spec3.child_window(class_name="msctls_progress32")

dlg_spec5 = dlg_spec4.child_window(class_name="Breadcrumb Parent")

# dlg_spec6=dlg_spec5.Toolbar

# dlg_spec6.click()

# time.sleep(1)

# 在地址栏输入地址
# dlg_spec4.Edit.set_text("F:\Aerobook\demo\selectFile_PopupWindow")

# 点击回车键
# send_keys('{ENTER}')
# dlg_spec4.print_control_identifiers()


# 在文件夹内输入文件名
#
# dlg_spec.Edit.set_text("cs")
#
# dlg_spec.print_control_identifiers()
#
# 点击选择文件夹按钮
dlg_spec.print_control_identifiers()

# dlg_spec.child_window(title="保存(&S)", class_name="Button").click()

dlg_spec.保存.click()



# dlg_spec6=dlg_spec5.Toolbar
# dlg_spec.print_control_identifiers()



# dlg_spec6.send_keystrokes("F:\Aerobook\demo\selectFile_PopupWindow")
# dlg_spec6.click()
# dlg_spec6.click_input("F:\Aerobook\demo\selectFile_PopupWindow")

# print("使用方法",dir(dlg_spec6.wrapper_object()))


