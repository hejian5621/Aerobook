
from src.utils.otherMethods.initialize import pywin_openAProgram



testdicts={"所在模块":"金属结构强度校核->金属二维单元强度校核"}

module="Aerobook-Aerocheck"
aero_window, module_window = pywin_openAProgram(module).menuOpen(testdicts)


workField1 = module_window.scrolledpanelwxWindowNR2   # 切换到被测工作


workField1.print_control_identifiers()


#安全系数文本框
workField1.Edit1.set_text("222")


#2D静强度勾选框
workField1.CheckBox1.click_input()


#VonMises勾选框
workField1.CheckBox2.click_input()

#环向勾选框
workField1.CheckBox3.click_input()


#P1(major)勾选框
workField1.CheckBox4.click_input()


#P3(minor)勾选框
workField1.CheckBox5.click_input()



#X向勾选框
workField1.CheckBox6.click_input()


#Y向勾选框
workField1.CheckBox7.click_input()


#剪应力勾选框
workField1.CheckBox8.click_input()

#四边简支压缩勾选框
workField1.CheckBox9.click_input()


#四边简支剪切勾选框
workField1.CheckBox10.click_input()


#压剪复合失稳（单轴压）勾选框
workField1.CheckBox11.click_input()


#四边简支双轴压勾选框
workField1.CheckBox12.click_input()





#曲板勾选框
workField1.CheckBox13.click_input()

#机身半径文本框
workField1.Edit2.set_text("222")


#折减宽度选择框
workField1.ComboBox1.select("平行于主承载方向  宽度")


#折减宽度文本框
workField1.Edit3.set_text("222")


#坐标系选择框
workField1.ComboBox2.select("全局坐标系")


#参考方向选择框
workField1.ComboBox3.select("Y轴")


#均值单选框
workField1.child_window(title="均 值", class_name="Button").click_input()

#极值单选框
workField1.child_window(title="极 值", class_name="Button").click_input()



#选择校核工况按钮
# workField1.Button1.click_input()

# #选择结构单元按钮文本框
# workField1.child_window(title="选择结构单元", class_name="Button").click_input()
#
# #校核按钮
# workField1.Button3.click_input()