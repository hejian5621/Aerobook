# 警告


from pywinauto.application import Application

app = Application().connect(title_re="警告")

dlg_spec = app.window(title="警告")

# dlg_spec1=dlg_spec.child_window(class_name="DirectUIHWND")

dlg_spec.print_control_identifiers()


# for x in dlg_spec.descendants():
#     print ("x.window_text:",x.window_text())
#     print ("x.class_name:",x.class_name())

static = app.DialogName.child_window(title_re='铺层数据库为空！',
            class_name_re='SysLink')
# print("static:",static.title)


# dlg_spec2=dlg_spec.child_window(title="铺层数据库为空!")
# dlg_spec3=dlg_spec2.SysLink

# dlg_spec2.print_control_identifiers()

# dlg_spec.print_control_identifiers()
print("__________________________________________________________")
# dlg_spec2.print_control_identifiers()

app.Dialog.Static.window_text()

# dlg_spec9 = app.window(title="警告")

# dlg_spec.Dialog.Static2.window_text()