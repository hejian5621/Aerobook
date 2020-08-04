
from pywinauto.application import Application

import time

app = Application().connect(title_re="Aerobook v1.0.4")

print(app)

time.sleep(2)

dlg_spec = app.window(title='Aerobook v1.0.4')

dlg_spec1=dlg_spec.child_window(auto_id="panel_Graph", control_type="System.Windows.Forms.Panel")

dlg_spec2=dlg_spec1.child_window(title="Aerocheck 1.0.4", class_name="wxWindowNR")

dlg_spec2.menu_select( r"铺层信息->铺层库优化")



