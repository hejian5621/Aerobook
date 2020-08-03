
from pywinauto.application import Application

app = Application().connect(title_re="警告")

dlg_spec = app.window(title="警告")

dlg_spec1=dlg_spec.child_window(class_name="DirectUIHWND")

dlg_spec2=dlg_spec1
# dlg_spec3=dlg_spec2.SysLink

# dlg_spec2.print_control_identifiers()

dlg_spec1.print_control_identifiers()

# dlg_spec1.Dialog.Static2.window_text()

# dlg_spec9 = app.window(title="警告")

# dlg_spec.Dialog.Static2.window_text()