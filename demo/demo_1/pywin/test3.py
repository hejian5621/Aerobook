

from pywinauto.application import Application

import time

app = Application().connect(title_re="Aerobook v1.0.4")

print(app)

time.sleep(2)

dlg_spec = app.window(title='Aerobook v1.0.4')
# dlg_spec.print_control_identifiers()

dlg_spec1=dlg_spec.child_window(auto_id="panel_Graph", control_type="System.Windows.Forms.Panel")

dlg_spec2=dlg_spec1.child_window(title="Aerocheck 1.0.3", class_name="wxWindowNR")

dlg_spec3= dlg_spec2.child_window(title="panel", class_name="wxWindowNR")


# dlg_spec2.menu_select(r"铺层信息->铺层库优化")



dlg_spec3=dlg_spec2.wxWindowNR4

dlg_spec4=dlg_spec3.splitter


dlg_spec5=dlg_spec4.wxWindowNR4



dlg_spec6=dlg_spec5.child_window(title="richText", class_name="wxWindow")

# dlg_spec7=dlg_spec6["richText2"]

dlg_spec5.print_control_identifiers()


dlg_spec6.print_control_identifiers()
dlg_spec6.Dialog.Static1.window_text()


# dlg_spec3.print_control_identifiers()




