# 强度校核


from pywinauto.application import Application
import time
from src.utils.otherMethods.initialize import pywin_openAProgram
from config.configurationFile import ProfileDataProcessing
import uiautomation
from tool import WindowTop
from OperatingControls.enterModule import BeingMeasured_work



WindowTop.EnumWindows("Aerobook v1.0.4")
time.sleep(1)
# 连接到被测程序，并且通过菜单栏打开被测模块

testCase_dict={"所在模块":"复材结构强度校核->复合材料强度校核"}

operationWindow="二维单元"

# operationWindow="杆柱单元"

aero_window, son_window = pywin_openAProgram().menuOpen_switchingWin_UIA(testCase_dict,operationWindow)

#

aero_window, son_window=BeingMeasured_work(son_window).workField_intensityCheck()


aero_window.print_control_identifiers()




"""二维单元"""


# 点击复合强度校核工作栏的二维单元按钮
# open_module().menu_compositeMaterial(Aero_window,"二维单元")

# 进入二维单元工作栏

# dlg_spec1=dlg_spec.复合材料强度校核_wx_SysTabCtl32
#
# dlg_spec2=dlg_spec1.panelwxWindowNR2
#
# dlg_spec2.print_control_identifiers()




# print("使用方法",dir(dlg_spec3.wrapper_object()))






"""
# 勾选2D静强度
while True:
    State=dlg_spec2.CheckBox0.get_check_state()
    if State==0:
        dlg_spec2.CheckBox0.click()
    else:
        break

# 勾选2D静强度下的VonMises
while True:
    State=dlg_spec2.CheckBox2.get_check_state()
    if State==0:
        dlg_spec2.CheckBox2.click()
    else:
        break


# 勾选2D静强度下的P1(major)
    dlg_spec2.CheckBox3.click()
while True:
    State=dlg_spec2.CheckBox3.get_check_state()
    if State==0:
        dlg_spec2.CheckBox3.click()
    else:
        break


# 勾选2D静强度下的P3(minor)
dlg_spec2.CheckBox4.click()
while True:
    State=dlg_spec2.CheckBox4.get_check_state()
    if State==0:
        dlg_spec2.CheckBox4.click()
    else:
        break


# 勾选2D静强度下的X向
dlg_spec2.CheckBox5.click()
while True:
    State=dlg_spec2.CheckBox5.get_check_state()
    if State==0:
        dlg_spec2.CheckBox5.click()
    else:
        break


# 勾选2D静强度下的Y向
dlg_spec2.CheckBox6.click()
while True:
    State=dlg_spec2.CheckBox6.get_check_state()
    if State==0:
        dlg_spec2.CheckBox6.click()
    else:
        break


# 勾选2D静强度下的XY向
dlg_spec2.CheckBox7.click()
while True:
    State=dlg_spec2.CheckBox7.get_check_state()
    if State==0:
        dlg_spec2.CheckBox7.click()
    else:
        break


# 勾选2D静强度下的耦合应变
dlg_spec2.CheckBox8.click()
while True:
    State=dlg_spec2.CheckBox8.get_check_state()
    if State==0:
        dlg_spec2.CheckBox8.click()
    else:
        break


# 勾选简支压缩
dlg_spec2.CheckBox9.click()
while True:
    State=dlg_spec2.CheckBox9.get_check_state()
    if State==0:
        dlg_spec2.CheckBox9.click()
    else:
        break

# 勾选简支剪切
dlg_spec2.CheckBox10.click()
while True:
    State=dlg_spec2.CheckBox10.get_check_state()
    if State==0:
        dlg_spec2.CheckBox10.click()
    else:
        break

# 勾选弯剪复合失稳
dlg_spec2.CheckBox11.click()
while True:
    State = dlg_spec2.CheckBox11.get_check_state()
    if State == 0:
        dlg_spec2.CheckBox11.click()
    else:
        break


# 勾选压剪复合失稳（单轴压）
dlg_spec2.CheckBox12.click()
while True:
    State = dlg_spec2.CheckBox12.get_check_state()
    if State == 0:
        dlg_spec2.CheckBox12.click()
    else:
        break


# 勾选简支压缩（双轴压）
dlg_spec2.CheckBox13.click()
while True:
    State = dlg_spec2.CheckBox13.get_check_state()
    if State == 0:
        dlg_spec2.CheckBox13.click()
    else:
        break


# 勾选压剪复合失稳（双轴压）
dlg_spec2.CheckBox14.click()
while True:
    State = dlg_spec2.CheckBox14.get_check_state()
    if State == 0:
        dlg_spec2.CheckBox14.click()
    else:
        break



# 勾选曲板结构
dlg_spec2.CheckBox15.click()
while True:
    State = dlg_spec2.CheckBox15.get_check_state()
    if State == 0:
        dlg_spec2.CheckBox15.click()
    else:
        break


# 勾选机身蒙皮
dlg_spec2.RadioButton1.click()
while True:
    State = dlg_spec2.RadioButton1.get_check_state()
    if State == 0:
        dlg_spec2.RadioButton1.click()
    else:
        break


# 勾选翼盒蒙皮
dlg_spec2.RadioButton2.click()
while True:
    State = dlg_spec2.RadioButton2.get_check_state()
    if State == 0:
        dlg_spec2.RadioButton2.click()
    else:
        break



# 勾选梁腹板
dlg_spec2.RadioButton3.click()
while True:
    State = dlg_spec2.RadioButton3.get_check_state()
    if State == 0:
        dlg_spec2.RadioButton3.click()
    else:
        break


# 勾选其他
dlg_spec2.RadioButton4.click()
while True:
    State = dlg_spec2.RadioButton4.get_check_state()
    if State == 0:
        dlg_spec2.RadioButton4.click()
    else:
        break


# 勾选方法三
dlg_spec2.RadioButton8.click()
while True:
    State = dlg_spec2.RadioButton8.get_check_state()
    if State == 0:
        dlg_spec2.RadioButton8.click()
    else:
        break



# 勾选方法一
dlg_spec2.RadioButton6.click()
while True:
    State = dlg_spec2.RadioButton6.get_check_state()
    if State == 0:
        dlg_spec2.RadioButton6.click()
    else:
        break

# 勾选方法二
dlg_spec2.RadioButton7.click()
while True:
    State = dlg_spec2.RadioButton7.get_check_state()
    if State == 0:
        dlg_spec2.RadioButton7.click()
    else:
        break


"""

# 勾选曲板结构
# aero_window.CheckBox15.click()
# while True:
#     State = aero_window.CheckBox15.get_check_state()
#     if State == 0:
#         aero_window.CheckBox15.click()
#     else:
#         break


# 机身半径
# aero_window.Edit1.set_text("0.35")


# 在B值减缩系数文本框中输入数据
aero_window.Edit2.set_text("0.25")


# 宽度修正系数文本框
aero_window.Edit3.set_text("0.25")

# 勾选极值
# aero_window.极.click()
# while True:
#     State = aero_window.极.get_check_state()
#     if State == 0:
#         aero_window.极.click()
#     else:
#         break
#
#
# # 勾选均值
# aero_window.均.click()
# while True:
#     State = aero_window.均.get_check_state()
#     if State == 0:
#         aero_window.均.click()
#     else:
#         break


# 在主承载方向组合框中选择单元坐标系
aero_window.ComboBox0.select("全局坐标系")
while True:
    State = aero_window.ComboBox0.window_text()
    print("State:",State)
    if State == "全局坐标系":
        break
    else:
        aero_window.ComboBox0.select("全局坐标系")


# aero_window.ComboBox0.select("单元坐标系")
# while True:
#     State = aero_window.ComboBox0.window_text()
#     print("State:",State)
#     if State == "单元坐标系":
#         break
#     else:
#         aero_window.ComboBox0.select("单元坐标系")

time.sleep(1)

app=aero_window.ComboBox2

print("使用方法",dir(app.wrapper_object()))
State = aero_window.ComboBox2.window_text()
print("State:",State)
txt=app.selected_text()

print("txt:",txt)
aero_window.ComboBox2.select("Y轴")
while True:
    State = aero_window.ComboBox2.window_text()
    if State == "Y轴":
        break
    else:
        aero_window.ComboBox2.select("Y轴")



aero_window.ComboBox0.select("单元坐标系")
while True:
    State = aero_window.ComboBox0.window_text()
    print("State:",State)
    if State == "单元坐标系":
        break
    else:
        aero_window.ComboBox0.select("单元坐标系")



aero_window.参考方向ComboBox.select("Y轴")
while True:
    State = aero_window.参考方向ComboBox.window_text()
    if State == "Y轴":
        break
    else:
        aero_window.参考方向ComboBox.select("Y轴")
"""

# 在主承载方向组合框中选择单元坐标系
dlg_spec2.ComboBox0.select("单元坐标系")
while True:
    State = dlg_spec2.ComboBox0.window_text()
    print("State:",State)
    if State == "单元坐标系":
        break
    else:
        dlg_spec2.ComboBox0.select("单元坐标系")
        
        
# 在主承载方向组合框中选择全局坐标
dlg_spec2.ComboBox0.select(r"全局坐标系")
while True:
    State = dlg_spec2.ComboBox0.window_text()
    print("State:", State)
    if State == "全局坐标系":
        break
    else:
        dlg_spec2.ComboBox0.select("全局坐标系")


# 在主承载方向组合框中选择全局坐标的情况下，参考方向选择X轴
dlg_spec2.ComboBox2.select("Y轴")
while True:
    State = dlg_spec2.ComboBox2.window_text()
    if State == "Y轴":
        break
    else:
        dlg_spec2.ComboBox2.select("Y轴")





# 在宽度修正系数组合框中选择垂直于主承载方向 宽度
dlg_spec2.ComboBox3.select("垂直于主承载方向 宽度")
while True:
    State = dlg_spec2.ComboBox3.window_text()
    if State == "垂直于主承载方向 宽度":
        break
    else:
        dlg_spec2.ComboBox3.select("垂直于主承载方向 宽度")



# 在宽度修正系数组合框中选择平行于主承载方向宽度
dlg_spec2.ComboBox3.select("平行于主承载方向 宽度")
while True:
    State = dlg_spec2.ComboBox3.window_text()
    if State == "平行于主承载方向 宽度":
        break
    else:
        dlg_spec2.ComboBox3.select("平行于主承载方向 宽度")



# 在机身半径文本框中输入数据
dlg_spec2.机身半径Edit.set_text("0.15")





# 在B值减缩系数文本框中输入数据
dlg_spec2.B值减缩系数Edit.set_text("0.25")

"""

# 点击选择结构单元按钮
# dlg_spec.child_window(title="选择结构单元", class_name="Button").click()


# 点击选择结构校核工况
# dlg_spec.child_window(title="...", class_name="Button").click()

# dlg_spec2.机身半径Edit.set_text("0.15")
# while True:
#     State = dlg_spec2.机身半径Edit.window_text()
#     print("State:",State)
#     if State == "0.15":
#         break
#     else:
#         dlg_spec2.机身半径Edit.set_text("0.15")

#
# # 点击校核按钮
# dlg_spec.校核Button.click()
#
#
# # 点击关闭按钮
# dlg_spec.关闭.click()














""" 进入一维单元工作栏"""

#鼠标滑到最上面
# open_module().menu_compositeMaterial(Aero_window,"杆柱单元")






"""
# 勾选1D静强度

dlg_spec2.CheckBox0.click()
while True:
    State = dlg_spec2.CheckBox0.get_check_state()
    if State == 0:
        dlg_spec2.CheckBox0.click()
    else:
        break


# 勾选局部失稳

dlg_spec2.CheckBox2.click()
while True:
    State = dlg_spec2.CheckBox2.get_check_state()
    if State == 0:
        dlg_spec2.CheckBox2.click()
    else:
        break

# 勾选压损

dlg_spec2.CheckBox3.click()
while True:
    State = dlg_spec2.CheckBox3.get_check_state()
    if State == 0:
        dlg_spec2.CheckBox3.click()
    else:
        break
"""
# 勾选加筋板柱屈曲

# aero_window.CheckBox4.click()
# while True:
#     State = aero_window.CheckBox4.get_check_state()
#     if State == 0:
#         aero_window.CheckBox4.click()
#     else:
#         break

# 勾选极值

# aero_window.极.click()
# while True:
#     State = aero_window.极.get_check_state()
#     if State == 0:
#         aero_window.极.click()
#     else:
#         break
#
#
# #勾选均值
#
# aero_window.均.click()
# while True:
#     State = aero_window.均.get_check_state()
#     if State == 0:
#         aero_window.均.click()
#     else:
#         break


# 勾选两边各取蒙皮宽度一半
#
# aero_window.RadioButton5.click()
# while True:
#     State = aero_window.两边各取蒙皮宽度一半.get_check_state()
#     if State == 0:
#         aero_window.两边各取蒙皮宽度一半.click()
#     else:
#         break
# #
#
# time.sleep(0.5)
# # 勾选两边各取15倍蒙皮厚度
#
# dlg_spec2.RadioButton5.click()
# while True:
#     State = dlg_spec2.RadioButton5.get_check_state()
#     if State == 0:
#         dlg_spec2.RadioButton5.click()
#     else:
#         break



"""

# 勾选刚度比

dlg_spec2.CheckBox5.click()
while True:
    State = dlg_spec2.CheckBox5.get_check_state()
    if State == 0:
        dlg_spec2.CheckBox5.click()
    else:
        break



# 勾选极值

dlg_spec2.child_window(title="极  值", class_name="Button").click()
while True:
    State = dlg_spec2.child_window(title="极  值", class_name="Button").get_check_state()
    if State == 0:
        dlg_spec2.child_window(title="极  值", class_name="Button").click()
    else:
        break

time.sleep(0.5)







# 在端部支持系数文本框中输入数据
dlg_spec2.Edit0.set_text("0.15")


# 在端上限文本框中输入数据
dlg_spec2.Edit2.set_text("2.15")


# 在下限文本框中输入数据
dlg_spec2.Edit3.set_text("1.15")


# 在B值减缩系数文本框中输入数据
dlg_spec2.Edit4.set_text("1.15")

"""
# son_window.print_control_identifiers()
# 点击选择结构单元按钮
# son_window.Button2.click()



# 点击选择结构校核工况
# son_window.Button0.click()


# # 点击校核按钮
# son_window.Button3.click()

#
# # 点击关闭按钮
# dlg_spec.关闭.click()