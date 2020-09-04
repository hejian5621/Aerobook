
from src.utils.otherMethods.initialize import programInitialization,execute_useCase_initialize

import sys,os,time



# 单元尺寸定义

testdicts={}

testdicts["所在模块"] = "尺寸信息->一维单元尺寸定义（模板）"


aero_window, son_window = execute_useCase_initialize().execute_useCase_enterInto(testdicts)

dlg_spec= son_window.scrolledpanelwxWindowNR2

print("分割线————————————————————————————————————————————————————————————————————————————————————————————————————")

dlg_spec1=dlg_spec.child_window(class_name="_wx_SysTabCtl32")


dlg_spec2=dlg_spec1.panelwxWind


# # 点击浏览按钮
dlg_spec2.Button1.click()
dlg_spec2.Button1.click()
dlg_spec2.Button1.click()
dlg_spec2.Button1.click()






# dlg_spec2.print_control_identifiers()

# 操作菜单栏，进入1D尺寸定义（模板）工作栏

text=""
# dlg_spec2.材料类型Edit.set_text(text)



# # 材料类型--选择复合材料
# dlg_spec2.金属材料.click()
#
#
# time.sleep(2)
# # dlg_spec3.print_control_identifiers()
#
# dlg_spec2.复合材料.click()
#
#
# time.sleep(2)
#
#
#
# # 点击创建按钮
# dlg_spec2.创建.click()
#
#
# # 点击浏览按钮
# dlg_spec2.Button1.click()






# dlg_spec=aero_window.child_window(auto_id="panel_Graph", control_type="System.Windows.Forms.Panel")
#

# dlg_spec1=dlg_spec.child_window(title="Aerocheck 1.0.4", class_name="wxWindowNR")
#
#
# dlg_spec2=dlg_spec1.panelwxWindowNR
#
# dlg_spec3=dlg_spec2.child_window(title="multiSplitter", class_name="wxWindowNR")
#
# dlg_spec4=dlg_spec3.child_window(title="scrolledpanel", class_name="wxWindowNR")
#
# dlg_spec5=dlg_spec4.child_window(class_name="_wx_SysTabCtl32")
#
# dlg_spec6=dlg_spec4.panelwxWindowNR2

