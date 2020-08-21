
from src.utils.otherMethods.initialize import programInitialization
from pywinauto.application import Application
from src.utils.otherMethods.controlOperationSuite import ControlOperationSuite
import uiautomation
from pywinauto import mouse
import time
from pywinauto.controls.hwndwrapper import HwndWrapper
from pywinauto import Desktop
from pykeyboard import PyKeyboard




time.sleep(2)

#
# instrument().delFile()
# # 复制模板文件，并返回复制的地址
# source = instrument().copyFile()



windowTitle=r'Aerobook v1.0.4'

childApp_title="Aerocheck 1.0.4"

childApp_Name="Aerocheck"

MenuOptions="文件->项目->新建"

source=r"C:\Users\Administrator\Desktop\aro\aro2"


# # 启动程序
py_app=programInitialization(windowTitle).open_accredit()
#
uia_app=programInitialization(windowTitle).EntrySubapplication(childApp_Name)
#
# #————————————————————————————————————————————————————————————————————————————————————————————————————————
#
# # 新增项目
ControlOperationSuite(childApp_title).childApp_newProject(py_app,MenuOptions,source)
#
#
# # 独立显示底部蒙皮
ControlOperationSuite(py_app).ShowSkinSeparately()







# time.sleep(1)












# app = Application().connect(title=r'新建项目: 指定项目保存路径')
#
# dlg_spec = app.window(title="新建项目: 指定项目保存路径")


# app = Application().connect(title=r'项目设置')
# #
# app.window(title="项目设置").Maximize()
# dlg_spec=app.window(title="项目设置")
#
# mouse.click(button='left', coords=(198, 152))
#
# dlg_spec.Edit.wait("exists",timeout=60,retry_interval=0.1).set_text(r"C:\Users\Administrator\Desktop\aro\aro2\Htail.fem")
#
# # dlg_spec.Edit.
#
# #
# dlg_spec.完成.wait("exists",timeout=60,retry_interval=0.1).click()









# dlg_spec.print_control_identifiers()

# 选择项目的保存路径
# ControlOperationSuite().SelectFile_Popover("新建项目: 指定项目保存路径", source, "保存", "选择文件","test_01")


# programInitialization(childApp_title).childApp_newProject(py_app,MenuOptions,source)





# dlg_spec2 = py_app.child_window(title="Aerocheck 1.0.4", class_name="wxWindowNR").wait("exists",timeout=60,retry_interval=0.5)
#
# dlg_spec2.menu_select(MenuOptions)




# app = Application().connect(title=r'Aerobook v1.0.4')
# py_app = app.window(title=r'Aerobook v1.0.4')
# # py_app1 = py_app.window(title=r'Aerocheck 1.0.4')
# # py_app2 = py_app.panelwxWindowNR0
# # py_app3 = py_app.window(title=r'multiSplitter')
# # py_app4 = py_app.panelwxWindowNR1
# # py_app5 = py_app4.wx_SysTabCtl321
# py_Tree = py_app.TreeView
#
#
# py_Tree.select("\\模型\部件(1)\HTail_W28(1)\STRUCTURE MODEL(1)\STRUCTURE NATURALMESH(3)\Skin(2)\SkinBottom(1)")
#
# # py_app6.print_control_identifiers()
#
# time.sleep(1)
#
# # # py_app7.right_click()
# mouse.right_click(coords=(182,285))
# time.sleep(1)

# app3 = Application().connect(title=r'菜单')
# app3.print_control_identifiers()

# k = PyKeyboard()
# k.press_key(k.down_key)
# time.sleep(0.5)
# k.press_key(k.down_key)
# time.sleep(0.5)
# k.press_key(k.down_key)
# time.sleep(0.5)
# k.press_key(k.enter_key)
#
#
#
#
# # m.click
# # HwndWrapper(py_app6.windows()[0].handle).double_click()
#
# #
# py_app6.print_control_identifiers()