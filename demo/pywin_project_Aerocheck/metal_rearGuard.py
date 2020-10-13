from src.utils.otherMethods.initialize import pywin_openAProgram



testdicts={"所在模块":"金属结构强度校核->金属曲板后驱曲强度校核"}


aero_window, module_window = pywin_openAProgram().menuOpen(testdicts)


workField1 = module_window.scrolledpanelwxWindowNR2   # 切换到被测工作


workField1.print_control_identifiers()



#安全系数文本框
workField1.Edit1.set_text("222")


#曲板剪切勾选框
workField1.CheckBox1.click_input()


#2系勾选框
workField1.RadioButton1.click_input()

#7系勾选框
workField1.RadioButton2.click_input()


#其他勾选框
workField1.RadioButton3.click_input()


#τ*文本框
workField1.Edit2.set_text("222")


#折减宽度文本框
workField1.Edit3.set_text("222")


#长桁局部失稳勾选框
workField1.CheckBox2.click_input()


#考虑勾选框
workField1.RadioButton5.click_input()

#不考虑勾选框
workField1.RadioButton6.click_input()


#长桁总体失稳（中间）勾选框
workField1.CheckBox3.click_input()


#长桁总体失稳（端头）勾选框
workField1.child_window(title="长桁总体失稳（端头）", class_name="Button").click_input()


#弯制勾选框
workField1.RadioButton8.click_input()

#挤压勾选框
workField1.RadioButton9.click_input()


#蒙皮厚度的倍数勾选框
workField1.RadioButton11.click_input()


#迭代法勾选框
workField1.RadioButton12.click_input()


#端部支持系数文本框
workField1.Edit5.set_text("222")

#框外缘条局部失稳稳定性勾选框
workField1.CheckBox5.click_input()


# # 缘条宽度文本框
# workField1.Edit6.set_text("222")
#
#
# # 屈服强度文本框
# workField1.Edit7.set_text("222")


#剪切框勾选框
workField1.RadioButton13.click_input()

#浮框勾选框
workField1.child_window(title="浮框", class_name="Button").click_input()

#坐标系勾选框
workField1.ComboBox1.select("全局坐标系")

#参考方向勾选框
workField1.ComboBox2.select("Y轴")



workField1.Static15.click_input()


import win32api,win32con

win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL,0,0,-500)   # 滚动鼠标


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