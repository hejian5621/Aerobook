
from src.utils.otherMethods.initialize import pywin_openAProgram

from OperatingControls.enterModule import ctrW_AeroAerochcek
import time
from src.utils.OperatingControls.moduleControlOperation import OperatingControls

from OperatingControls.enterModule import BeingMeasured_popupWin
#  1D单元设计变量(截面尺寸)

from OperatingControls.enterModule import ctrW_AeroFiberbook


# testdicts={"所在模块":"优化->优化设置->设计变量->一维单元设计变量（截面尺寸）"}
# module="Aerobook-Fiberbook"

#
#
# aero_window, son_window = pywin_openAProgram(module).menuOpen(testdicts)
#
#
# win_one =ctrW_AeroFiberbook(son_window).workField_general()
#
# win_one.print_control_identifiers()
#
# win_two=win_one.gridwxWindowNR1.GridWindowwxWindowNR1
#
#
# win_three=win_one.panelwxWindowNR4.GridWindow2
#
#
# win_four=win_one.panelwxWindowNR4
#
# # 截面形式下拉框
# win_one.ComboBox1.select("J字型1")
#
# # 截面参数表中第一行双击框
# # win=win_two.double_click_input(coords=(60, 10), button="left")
#
# #  截面参数表中第二行双击框
# # win=win_two.double_click_input(coords=(60, 30), button="left")
#
# #  截面参数表中第三行双击框
# # win=win_two.double_click_input(coords=(60, 50), button="left")
#
#
# #  截面参数表中第四行双击框
# # win=win_two.double_click_input(coords=(60, 70), button="left")
#
# # #  截面参数表中第五行双击框
# # win=win_two.double_click_input(coords=(60, 90), button="left")
# #
# # #  截面参数表中第六行双击框
# # win=win_two.double_click_input(coords=(60, 110), button="left")
# #
# # #  截面参数表中第七行双击框
# # win=win_two.double_click_input(coords=(60, 130), button="left")
#
#
# # 截面关联惯性矩复选框
# win_one.CheckBox1.click_input()
#
# # 金属材料复选框
# win_one.RadioButton2.click_input()
#
# # 复合材料复选框
# win_one.RadioButton1.click_input()
#
#
# # 滚动鼠标
# win1=win_one.GroupBox3
# OperatingControls(win1).scrollMouse()
#
#
#
# # 复合材料，铺层定义第一行双击框
# # win_three.double_click_input(coords=(60, 10), button="left")
#
# # 复合材料，铺层定义第二行双击框
# # win_three.double_click_input(coords=(60, 30), button="left")
#
# # 复合材料，铺层定义第三行双击框
# # win_three.double_click_input(coords=(60, 50), button="left")
#
# # 复合材料，铺层定义第四行双击框
# # win_three.double_click_input(coords=(60, 70), button="left")
#
# #铺层比可变复选框
# win_one.CheckBox2.click_input()
#
# #复合材料，铺层定义第一行文本框
# win_three.double_click_input(coords=(60, 10), button="left")
# win_three.click_input(coords=(60, 10), button="left")
# win_three.print_control_identifiers()
# win_three.Edit.set_text("1")
#
# #复合材料，铺层定义第二行文本框
# win_three.double_click_input(coords=(60, 30), button="left")
# win_three.click_input(coords=(60, 30), button="left")
# win_three.print_control_identifiers()
# win_three.Edit.set_text("2")
#
# #复合材料，铺层定义第三行文本框
# win_three.double_click_input(coords=(60, 50), button="left")
# win_three.click_input(coords=(60, 50), button="left")
# win_three.print_control_identifiers()
# win_three.Edit.set_text("3")
#
# #复合材料，铺层定义第四行文本框
# win_three.double_click_input(coords=(60, 70), button="left")
# win_three.click_input(coords=(60, 70), button="left")
# win_three.print_control_identifiers()
# win_three.Edit.set_text("4")
#
# # 对称铺层
# win_one.CheckBox3.click_input()
#
# # E11文本框
# win_four.Edit1.set_text("1")
#
# # E22文本框
# win_four.Edit2.set_text("1")
#
# # V12文本框
# win_four.Edit3.set_text("1")
#
# # G12文本框
# win_four.Edit4.set_text("1")
#
# #所有选中单元共享
# win_one.RadioButton5.click_input()
#
# # 不共享
# win_one.RadioButton4.click_input()
#
# # 属性卡片起始ID
# win_one.Edit5.set_text("1")
#
# # 材料卡片起始ID
# win_one.Edit6.set_text("1")
#
# # 选择单元结构
# win_one.child_window(title="选择结构单元", class_name="Button").click_input()
#
# # 输出到include文件
# win_one.Edit7.set_text("1")
#
# # 点击创建按钮
# win_one.Button2.click_input()
#
# # 点击关闭按钮
# # win_one.Button3.click_input()
#




"""1D截面参数定义弹窗"""


# testdicts={"所在模块":"优化->优化设置->设计变量->一维单元设计变量（截面尺寸）"}
# module="Aerobook-Fiberbook"
#
#
#
#
# aero_window, son_window = pywin_openAProgram(module).menuOpen(testdicts)


# win_one =ctrW_AeroFiberbook(son_window).workField_1DSection_popUps()

#
# win_one = BeingMeasured_popupWin("1D截面参数定义").menu_LetsGoTopopover()
#
# win_one.print_control_identifiers()
#
#
# # 1D截面参数定义弹窗-》使用固定数值复选框
# win_one.RadioButton1.click_input()
#
# #1D截面参数定义弹窗-》固定值文本框
# win_one.Edit1.set_text("0.5")
#
#
# # 1D截面参数定义弹窗-》参考相邻板高度复选框
# win_one.RadioButton2.click_input()
#
#
# # 1D截面参数定义弹窗-》比例系数文本框
# win_one.Edit2.set_text("0.5")
#
# # 1D截面参数定义弹窗-》在指定范围内优化复选框
# win_one.RadioButton3.click_input()
#
# # 1D截面参数定义弹窗-》初始文本框
# win_one.Edit3.set_text("0.5")
#
# # 1D截面参数定义弹窗-》下限文本框
# win_one.Edit4.set_text("0.5")
#
# # 1D截面参数定义弹窗-》上限文本框
# win_one.Edit5.set_text("0.5")
#
# #1D截面参数定义弹窗-》由其他参数确定复选框
# win_one.RadioButton4.click_input()
#
# # 1D截面参数定义弹窗-》C0文本框
# win_one.Edit6.set_text("0.5")
#
# # 1D截面参数定义弹窗-》CMULT文本框
# win_one.Edit7.set_text("0.5")
#
# # 1D截面参数定义弹窗-》参数名下拉框
# win_one.ComboBox.select("T2")
#
# # 1D截面参数定义弹窗-》系数文本框
# win_one.Edit8.set_text("0.5")
#
# # 1D截面参数定义弹窗-》DLINK\n方程文本框
# win_one.Edit9.set_text("0.5")
#
# # 1D截面参数定义弹窗-》确认按钮
# win_one.Button3.click_input()
#
# # 1D截面参数定义弹窗-》取消按钮
# # win_one.Button4.click_input()










"""铺层比定义"""


# testdicts={"所在模块":"优化->优化设置->设计变量->一维单元设计变量（截面尺寸）"}
# module="Aerobook-Fiberbook"




# aero_window, son_window = pywin_openAProgram(module).menuOpen(testdicts)
#
#
# win_one =ctrW_AeroFiberbook(son_window).workField_LayerThan_popUps()


win_one = BeingMeasured_popupWin("铺层比定义").menu_LetsGoTopopover()

win_one.print_control_identifiers()


# 铺层比定义弹窗-》在指定范围优化复选框
win_one.RadioButton1.click_input()

# 铺层比定义弹窗-》初始文本框
win_one.Edit1.set_text("0.5")

# 铺层比定义弹窗-》下限文本框
win_one.Edit2.set_text("0.5")

# 铺层比定义弹窗-》上限文本框
win_one.Edit3.set_text("0.5")

# 铺层比定义弹窗-》与其他铺层关联复选框
win_one.RadioButton2.click_input()


# 铺层比定义弹窗-》C0文本框
win_one.Edit4.set_text("0.5")

# 铺层比定义弹窗-》CMULT文本框
win_one.Edit5.set_text("0.5")

# 铺层比定义弹窗-》其他铺层框下拉框
win_one.ComboBox.select("3")

# 铺层比定义弹窗-》系数文本框
win_one.Edit6.set_text("0.5")

# 铺层比定义弹窗-》DLINK方程文本框
win_one.Edit7.set_text("0.5")

# 铺层比定义弹窗-》确认按钮
win_one.Button3.click_input()

# 铺层比定义弹窗-》取消按钮
# win_one.Button4.click_input()















