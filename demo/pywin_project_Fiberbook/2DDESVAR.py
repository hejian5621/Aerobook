

# 二维单元设计参数


from src.utils.otherMethods.initialize import pywin_openAProgram

from OperatingControls.enterModule import ctrW_AeroAerochcek
import time
from src.utils.OperatingControls.moduleControlOperation import OperatingControls

from OperatingControls.enterModule import BeingMeasured_popupWin


from OperatingControls.enterModule import ctrW_AeroFiberbook
#
#
# testdicts={"所在模块":"优化->优化设置->设计变量->二维单元设计参数"}
# module="Aerobook-Fiberbook"
#
#

# aero_window, son_window = pywin_openAProgram(module).menuOpen(testdicts)
#
#
win_one =ctrW_AeroFiberbook(son_window).workField_general()
#
#
win_two=win_one.child_window(title="grid", class_name="wxWindowNR")
#
# win_one.print_control_identifiers()

# # 厚度下限文本框
# win_one.Edit1.set_text("22")
#
# # 厚度上限文本框
# win_one.Edit2.set_text("33")
#
# # 金属材料复选框
# win_one.RadioButton2.click_input()
#
# # 复合材料复选框
# win_one.RadioButton1.click_input()




# 复合材料表第一行双击弹窗
# win_two.double_click_input(coords=(100, 40), button="left")

# 复合材料表第二行双击弹窗
# win_two.double_click_input(coords=(100, 60), button="left")

#  复合材料表第三行双击弹窗
# win_two.double_click_input(coords=(100, 80), button="left")


#  复合材料表第四行双击弹窗
# win_two.double_click_input(coords=(100, 100), button="left")


# # 铺层比可变复选框
# win_one.CheckBox.click_input()
#
#
#
# # 复合材料表第一行文本框
# win_two.double_click_input(coords=(100, 40), button="left")
#
# # 复合材料表第二行文本框
# win_two.double_click_input(coords=(100, 60), button="left")
#
# #  复合材料表第三行文本框
# win_two.double_click_input(coords=(100, 80), button="left")
#
#
# #  复合材料表第四行文本框
# win_two.double_click_input(coords=(100, 100), button="left")


# # 不共享复选框
# win_one.RadioButton4.click_input()
#
# # 所有选中单元共享复选框
# win_one.RadioButton5.click_input()
#
# # 属性卡片起始ID文本框
# win_one.Edit3.set_text("11")
#
#
# # 选择结构单元
# win_one.child_window(title="选择结构单元", class_name="Button").click_input()
#
# # 输出到include文本框
# win_one.Edit4.set_text("55")
#
# # 创建按钮
# win_one.Button2.click_input()
#
# # 关闭按钮
# # win_one.Button3.click_input()



"""铺层厚度/铺层比定义"""

testdicts={"所在模块":"优化->优化设置->设计变量->二维单元设计参数"}
module="Aerobook-Fiberbook"



# aero_window, son_window = pywin_openAProgram(module).menuOpen(testdicts)


# win_one =ctrW_AeroFiberbook(son_window).workField_1DSection_popUps()


win_one = BeingMeasured_popupWin("铺层厚度/铺层比定义").menu_LetsGoTopopover()

win_one.print_control_identifiers()



# 优化变量复选框
win_one.RadioButton1.click_input()

# 下限文本框
win_one.Edit2.set_text("55")

# 上限文本框
win_one.Edit3.set_text("55")

# 与其他铺层厚度关联复选框
win_one.RadioButton2.click_input()

# C0文本框
win_one.Edit4.set_text("55")

# CMULT文本框
win_one.Edit5.set_text("55")

# 其他铺层下拉框
win_one.ComboBox.select("2")

# 系数文本框
win_one.Edit6.set_text("55")

# 加号按钮
win_one.Button.click_input()

# 减号按钮
win_one.Button2.click_input()

# DLINK文本框
win_one.Edit7.set_text("55")

# 铺层比下限文本框
win_one.Edit8.set_text("55")

# 铺层比上限文本框
win_one.Edit9.set_text("55")


# 确定按钮
win_one.Button3.click_input()

# 取消按钮
# win_one.Button4.click_input()

