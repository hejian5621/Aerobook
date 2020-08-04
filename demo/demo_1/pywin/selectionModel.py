

from pywinauto.application import Application

from pywinauto.keyboard import send_keys

from pywinauto import mouse
import time

app = Application().connect(title_re="Aerobook v1.0.4")

print(app)

time.sleep(2)

dlg_spec = app.window(title='Aerobook v1.0.4')
# dlg_spec.print_control_identifiers()

dlg_spec1=dlg_spec.child_window(auto_id="panel_Graph", control_type="System.Windows.Forms.Panel")

dlg_spec2=dlg_spec1.child_window(title="Aerocheck 1.0.4", class_name="wxWindowNR")

dlg_spec3= dlg_spec2.panelwxWindowNR0

dlg_spec4=dlg_spec3.child_window(title="multiSplitter", class_name="wxWindowNR")

dlg_spec5=dlg_spec4.child_window(title="splitter", class_name="wxWindowNR")


dlg_spec6=dlg_spec5.wxWindowNR2

# dlg_spec6.capture_as_image().save('模型.png')

dlg_spec6.print_control_identifiers()


#模式键盘点击“Shift”键
# send_keys("{VK_SHIFT}")

# 将鼠标移动到（300，40）坐标处释放，

# mouse.click(button='left', coords=(340, 145))

mouse.press(button='left', coords=(340, 145))

mouse.release(button='left', coords=(1486, 686))




