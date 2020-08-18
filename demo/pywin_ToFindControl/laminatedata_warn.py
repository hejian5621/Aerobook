

import time

from pywinauto.application import Application

app = Application().connect(title_re="警告")

dlg_spec = app.window(title="警告")

# dlg_spec.print_control_identifiers()

dlg_spec1=dlg_spec.警告DirectUIHWND

dlg_spec2=dlg_spec1.ScrollBar

# dlg_spec2=dlg_spec1["L734, T197, R734, B197"]

dlg_spec1.print_control_identifiers()

print("_____________________________________________________________")

dlg_spec2.print_control_identifiers()

time.sleep(2)

dlg_spec2.capture_as_image().save("123.png")

# text=dlg_spec1.win32gui.SendMessage
# print("text:",text)

