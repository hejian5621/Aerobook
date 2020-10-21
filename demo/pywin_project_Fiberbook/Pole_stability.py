
# 杆柱稳定性响应和约束


from src.utils.otherMethods.initialize import pywin_openAProgram
import time

from OperatingControls.enterModule import ctrW_AeroFiberbook


time.sleep(2)

testdicts={"所在模块":"优化->优化设置->稳定性设计响应->杆柱稳定性响应和约束"}
module="Aerobook-Fiberbook"


aero_window, son_window = pywin_openAProgram(module).menuOpen(testdicts)


win_one =ctrW_AeroFiberbook(son_window).workField_general()

win_twe=win_one.材料类型_wx_SysTabCtl32


win_three=win_twe.child_window(title="grid", class_name="wxWindowNR").child_window(title="GridWindow", class_name="wxWindowNR")



win_one.print_ctrl_ids ()


# 滚动鼠标



# # 局部稳定性复选框
# win_one.CheckBox1.click_input()
#
# # 局部稳定性--安全系数文本框
# win_one.Edit1.set_text("1.5")
#
# # 压损复选框
# win_one.CheckBox2.click_input()
#
# # 压损--安全系数文本框
# win_one.Edit2.set_text("1.5")
#
# # 均值复选框
# win_one.child_window(title="均值   ", class_name="Button").click_input()
#
# # 极值复选框
# win_one.child_window(title="极值  ", class_name="Button").click_input()


# # 复合材料复选框
# win_one.RadioButton1.click_input()
#
# # 金属材料复选框
# win_one.RadioButton2.click_input()


#
# # 有自由边--系数1窗格
# win_three.click_input(coords=(10, 10), button="left")
# win_three.double_click_input(coords=(10, 10), button="left")
# win_three.Edit.set_text("2")
#
# # 有自由边--系数2窗格
# win_three.click_input(coords=(10, 30), button="left")
# win_three.double_click_input(coords=(10, 30), button="left")
# win_three.Edit.set_text("2")
#
# # 无自由边--系数1窗格
# win_three.click_input(coords=(100, 30), button="left")
# win_three.double_click_input(coords=(100, 10), button="left")
# win_three.Edit.set_text("2")
#
# # 无自由边--系数2窗格
# win_three.click_input(coords=(100, 30), button="left")
# win_three.double_click_input(coords=(100, 30), button="left")
# win_three.Edit.set_text("2")



# # 蔡-希尔（Tsai-Hill）准则计算
# win_twe.RadioButton1.click_input()
#
# # 霍夫曼（Hoffman）准则计算
# win_twe.RadioButton2.click_input()
#
# # 纵向拉伸强度Xt文本框
# win_twe.Edit1.set_text("1500")
#
# # 纵向压缩强度Xc
# win_twe.Edit2.set_text("1500")
#
# # 横向拉伸强度Yt
# win_twe.Edit3.set_text("1500")
#
# # 横向压缩强度Yc
# win_twe.Edit4.set_text("1500")
#
# # 剪切强度S
# win_twe.Edit5.set_text("40")
#
# # 许用应变计算
# win_twe.RadioButton3.click_input()
#
# # 压缩许用应变
# win_twe.Edit6.set_text("2000")
#
# # B值减缩系数
# win_twe.Edit7.set_text("0.9")





#
# # 弯制复选框
# win_twe.child_window(title="弯制", class_name="Button").click_input()
#
# # 挤压复选框
# win_twe.RadioButton4.click_input()

# 杆材料参数--屈服强度文本框
# win_twe.Edit8.set_text("400")

# 相邻蒙皮材料参数--屈服强度文本框
# win_twe.Edit9.set_text("400")