#信息窗口获取文本信息

from src.utils.otherMethods.initialize import programInitialization
from pywinauto.application import Application
from config.configurationFile import ProfileDataProcessing
from win32gui import *
from win32api import *
from win32process import *
import win32con





aero_title = ProfileDataProcessing("commonality", "AerobookEdition").config_File()  # 从配置文件获取Aerobook窗口标题
aerocheck_title = ProfileDataProcessing("commonality", "AerocheckEdition").config_File()  # 从配置文件获取Aerocheck窗口标题


# # 通过Aerobook标题链接Aerobook进行，并切换到Aerobook窗口
aero_window = programInitialization(aero_title).entrance_subroutine_title()

dlg_spec = aero_window.child_window(auto_id="panel_Graph", control_type="System.Windows.Forms.Panel")

dlg_spec1 = dlg_spec.child_window(title="Aerocheck 1.0.4", class_name="wxWindowNR")

dlg_spec2 = dlg_spec1.panelwxWindowNR0

dlg_spec3 = dlg_spec2.child_window(title="multiSplitter", class_name="wxWindowNR")


dlg_spec4 = dlg_spec3.child_window(title="splitter", class_name="wxWindowNR")

dlg_spec5 = dlg_spec4.controlwxWindowNR

dlg_spec6 = dlg_spec5.wxWindowNR3

dlg_spec7 = dlg_spec6.child_window(class_name="_wx_SysTabCtl32")

dlg_spec8 = dlg_spec7.child_window(title="richText", class_name="wxWindow")



dlg_spec8.print_control_identifiers()

# test=dlg_spec8.window_text()

# test=dlg_spec8.Dialog.rich_text.window_text()

# print("test：",test)
#
# dlg_spec8.click()
#
# dlg_spec8.Calculator.Static.Texts()


aero_window.Calculator.Static.DrawOutline()

aero_window.Calculator.Static2.DrawOutline("red")


aero_window.Calculator.Static3.DrawOutline("blue")

aero_window.Calculator.Static3.Texts()



# # print ('##########')
# # app = Application()
# # window_handle = dlg_spec8.find_windows(title = u'My Dialog Name')
# # my_handle = window_handle[0]
# # window = app.window_(handle = my_handle)
# for x in dlg_spec8.children():
#     print ('Child %s' % x)
# print ('##########')