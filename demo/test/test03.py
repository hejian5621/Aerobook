
from src.utils.otherMethods.initialize import pywin_openAProgram
# 初始化

from pywinauto.application import Application
import uiautomation
from config.configurationFile import ProfileDataProcessing
import time,os
from OperatingControls.enterModule import specialWay_OperatingControls



aerocheck_title = ProfileDataProcessing("commonality", "AerocheckEdition").config_File()  # 从配置文件获取Aerocheck窗口标题
# 通过Aerobook标题链接Aerobook进程，并切换到Aerobook窗口
aero_window = pywin_openAProgram().entrance_subroutine_title()
# 切换到菜单栏
dlg_spec = aero_window.child_window(auto_id="panel_Graph", control_type="System.Windows.Forms.Panel")
son_window = dlg_spec.child_window(title=aerocheck_title, class_name="wxWindowNR")



son_window1=son_window.panelwxWindowNR1


son_window2=son_window1.child_window(title="multiSplitter", class_name="wxWindowNR")


son_window3=son_window2.panelwxWindowNR1

son_window4=son_window3.child_window(class_name="_wx_SysTabCtl32")



son_window5=son_window4.TreeView2

son_window5.get_child(child_spec="部件")

son_window5.print_control_identifiers()


