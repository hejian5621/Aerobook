from pywinauto.application import Application

import time

app = Application().connect(title_re="Aerobook v1.0.4")


time.sleep(2)

dlg_spec = app.window(title='Aerobook v1.0.4')
# dlg_spec.print_control_identifiers()

dlg_spec1=dlg_spec.child_window(auto_id="panel_Graph", control_type="System.Windows.Forms.Panel")

dlg_spec2=dlg_spec1.child_window(title="Aerocheck 1.0.4", class_name="wxWindowNR")

dlg_spec3= dlg_spec2.child_window(title="multiSplitter", class_name="wxWindowNR")

dlg_spec4=dlg_spec3.child_window(title="splitter", class_name="wxWindowNR")


dlg_spec5=dlg_spec4.control0


dlg_spec6=dlg_spec5.wxWindowNR3


dlg_spec7=dlg_spec6.child_window(class_name="_wx_SysTabCtl32")

dlg_spec8=dlg_spec7.Properties.child_window(title="richText", control_type="ControlType.Pane")

dlg_spec7.print_control_identifiers()

dlg_spec9=dlg_spec8.Dialog.richText.WindowText()

# dlg_spec4=dlg_spec3.richText