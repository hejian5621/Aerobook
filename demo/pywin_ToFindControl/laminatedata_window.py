# 铺层数据库制作工具


from pywinauto.application import Application

import time

time.sleep(1)
time.sleep(0)
app = Application().connect(title_re="铺层数据库制作工具")
dlg_spec = app.window(title="铺层数据库制作工具")

dlg_spec.print_control_identifiers()


# 找到选择铺层Excel文件对应的文本框和浏览按钮
# dlg_spec1=dlg_spec.wxWindowNR
# dlg_spec1.Edit.set_text(r"C:\Users\Administrator\Desktop\自动化测试相关\自动化测试用例\自动化测试用例")
# time.sleep(1)
# dlg_spec1.Button.click()


# 找到铺层数据库保存路径对应的文本框和浏览按钮
# dlg_spec1=dlg_spec.wxWindowNR2
# dlg_spec1.Edit2.set_text(r"C:\Users\Administrator\Desktop\自动化测试相关\自动化测试用例\自动化测试用例")
# time.sleep(1)
# dlg_spec1.Button2.click()


# 找到开始制作按钮
# dlg_spec1=dlg_spec.开始制作Button.click()

# 找到模板文件按钮
# dlg_spec1=dlg_spec.模板文件.click()

# 找到关闭按钮
dlg_spec1=dlg_spec.关闭.click()
