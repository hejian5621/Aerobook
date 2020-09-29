# 编辑工况



from src.utils.otherMethods.initialize import execute_useCase_initialize,pywin_openAProgram
from OperatingControls.enterModule import BeingMeasured_popupWin
import sys,os,time
from pywinauto.application import Application
from pywinauto import findwindows



testdicts={"所在模块":"载荷信息->编辑工况"}


aero_window, module_window = pywin_openAProgram().menuOpen(testdicts)


dlg_spec=BeingMeasured_popupWin("编辑工况").menu_LetsGoTopopover()
#




dlg_spec1=dlg_spec.child_window(title="panel", class_name="wxWindowNR")


dlg_spec.print_control_identifiers()



# dlg_spec1.CustomTreeCtrl.start_dragging("1：CASE1")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")




# # # 勾选新建勾选框
dlg_spec.RadioButton2.check()
#
# txt=dlg_spec.check_by_click_input()
# print("txt:",txt)


#
# # 在新建文本框中输入数据
# dlg_spec.Edit2.set_text("all")

#
#
# # 点击全部取消工况按钮
# dlg_spec.Button5.click()
#
# # 点击全选工况按钮
# dlg_spec.Button4.click()
#
# # 点击新建对应的增加按钮
# dlg_spec.Button3.click()
#
#
# # 勾选新建勾选框
# dlg_spec.RadioButton2.click()
#
# # 在新建文本框中输入数据
# dlg_spec.Edit2.set_text("all2")
#
# # 点击全选工况按钮
# dlg_spec.Button4.click()
#
#
# # 在工况组合下拉框中选择all2
#
#
#
#
# # 勾选重命名勾选框
# dlg_spec.RadioButton0.click()
#
# # 在重命名文本框中输入数据
# dlg_spec.Edit0.set_text("a1")




# # 在重命名对应的修改按钮
# dlg_spec.编辑工况Button2.click()






# dlg_spec.关闭.click()  # 关闭编辑工况



# dlg_spec.ComboBox.click()
# dlg_spec1=dlg_spec.ComboBox.select("all2").click()

#
#
# txt=dlg_spec.ComboBox.window_text()
# print("txt:",txt)
#
# dlg_spec.print_control_identifiers()

# dlg_spec1.



#
# # 删除工况
# dlg_spec.编辑工况Button.click()





# dlg_spec1=dlg_spec.child_window(title="panel", class_name="wxWindowNR")
# dlg_spec2=dlg_spec1.CustomTreeCtrlwxWindowNR
# dlg_spec2.print_control_identifiers()
#
# print("使用方法",dir(dlg_spec1.CustomTreeCtrl.wrapper_object()))
# list1=dlg_spec1.CustomTreeCtrl.menu_select(r"选择工况->CASE1")  # 切换树结构
# print("list1:",list1)
# # dlg_spec1.CustomTreeCtrl.select() # 切换树结构


# app = Application().connect(title_re="编辑工况")
# dlg_spec = app.window(title="编辑工况")
#
