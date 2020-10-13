

from src.utils.otherMethods.initialize import pywin_openAProgram



testdicts={"所在模块":"金属结构强度校核->金属一维单元强度校核"}

module="Aerobook-Aerocheck"
aero_window, module_window = pywin_openAProgram(module).menuOpen(testdicts)


workField1 = module_window.scrolledpanelwxWindowNR2   # 切换到被测工作


workField1.print_control_identifiers()

#
# #安全系数文本框
# workField1.Edit1.set_text("222")
#
#
# #1D静强度勾选框
# workField1.CheckBox1.click_input()
#
#
# #压损勾选框
# workField1.CheckBox2.click_input()
#
# #弯制单选框
# workField1.RadioButton1.click_input()
#
#
# #挤压单选框
# workField1.RadioButton2.click_input()
#
#
# #局部失稳勾选框
# workField1.CheckBox3.click_input()
#
# #均值单选框
# workField1.child_window(title="均  值", class_name="Button").click_input()
#
# #极值单选框
# workField1.child_window(title="极  值", class_name="Button").click_input()



#选择校核工况按钮
# workField1.Button1.click_input()

# #选择结构单元按钮文本框
# workField1.child_window(title="选择结构单元", class_name="Button").click_input()
#
# #校核按钮
# workField1.Button3.click_input()