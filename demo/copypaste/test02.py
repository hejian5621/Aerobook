
from src.utils.otherMethods.initialize import pywin_openAProgram
from config.configurationFile import ProfileDataProcessing
import time



time.sleep(2)
inModule="铺层信息->铺层库优化"

# inModule = testdicts["所在模块"]
# 读取配置文档信息
aero_title = ProfileDataProcessing("commonality", "AerobookEdition").config_File()  # 从配置文件获取Aerobook窗口标题
aerocheck_title = ProfileDataProcessing("commonality", "AerocheckEdition").config_File()  # 从配置文件获取Aerocheck窗口标题
# 通过Aerobook标题链接Aerobook进行，并切换到Aerobook窗口
aero_window = pywin_openAProgram().entrance_subroutine_title()

# aero_window.print_control_identifiers()

# 通过操作菜单栏，打开被测模块，然后切换到被测模块
# module_window = open_module().menu_laminateOptimize(inModule, aero_window, aerocheck_title)

# dlg_spec1 = aero_window.child_window(auto_id="panel_Graph", control_type="System.Windows.Forms.Panel")
# dlg_spec2 = dlg_spec1.child_window(title=aerocheck_title, class_name="wxWindowNR")
# dlg_spec3=dlg_spec2.child_window(title="splitter", class_name="wxWindowNR")
# dlg_spec4=dlg_spec3.child_window(class_name="_wx_SysTabCtl32")
# dlg_spec5=aero_window.richText2
# dlg_spec4.print_control_identifiers()
# dlg_spec5.click()
print("_______")
# 打印装饰器
# print(dir(dlg_spec5.wrapper_object()))
# text1=dlg_spec5.Texts
# print("text1:",text1)
# dlg_spec5.send_keystrokes("^a")
# dlg_spec5.send_keystrokes("^c")

# test=dlg_spec5.Dialog.Static1.window_text()


# print("test:",test)

import win32clipboard as wc
import win32con
import chardet


def getCopyText():
    wc.OpenClipboard()
    copy_text = wc.GetClipboardData(win32con.CF_TEXT)
    wc.CloseClipboard()
    return copy_text

# test

# print (chardet.detect(getCopyText()) )  # 找到包含中文内容的字符串编码
print (getCopyText().decode('GB2312') ) # 转码
