from src.utils.otherMethods.initialize import pywin_openAProgram



testdicts={"所在模块":"金属结构强度校核->金属加筋板强度校核"}

module="Aerobook-Aerocheck"
aero_window, module_window = pywin_openAProgram(module).menuOpen(testdicts)


workField1 = module_window.scrolledpanelwxWindowNR2   # 切换到被测工作


workField1.print_control_identifiers()



#安全系数文本框
workField1.Edit1.set_text("222")


#蒙皮厚度的倍数单选框
workField1.RadioButton1.click_input()


#蒙皮厚度的倍数文本框
workField1.Edit2.set_text("222")

#迭代法计算单选框
workField1.RadioButton2.click_input()


#弯制勾选框
workField1.RadioButton3.click_input()


#挤压勾选框
workField1.RadioButton4.click_input()



#端部支持系数文本框
workField1.Edit3.set_text("222")


#刚度比勾选框
workField1.CheckBox2.click_input()
workField1.CheckBox2.click_input()

#上限文本框
workField1.Edit4.set_text("222")

#下线文本框
workField1.Edit5.set_text("222")





#均值单选框
workField1.child_window(title="均  值", class_name="Button").click_input()

#极值单选框
workField1.child_window(title="极  值", class_name="Button").click_input()



#选择校核工况按钮
# workField1.Button1.click_input()

# #选择结构单元按钮文本框
# workField1.child_window(title="选择结构单元", class_name="Button").click_input()
#
# #校核按钮
# workField1.Button3.click_input()