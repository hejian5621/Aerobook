
from src.utils.otherMethods.initialize import pywin_openAProgram

from OperatingControls.enterModule import ctrW_AeroAerochcek
import time




# 全局设置

from OperatingControls.enterModule import ctrW_AeroFiberbook

testdicts={"所在模块":"优化->优化设置->全局设置"}
# testdicts={"所在模块":"优化->优化设置->设计变量->二维单元设计变量"}
module="Aerobook-Fiberbook"



aero_window, son_window = pywin_openAProgram(module).menuOpen(testdicts)


win_one =ctrW_AeroFiberbook(son_window).workField_general()




win_one.print_control_identifiers()

# # 截面尺寸上线文本框
win_one.Edit1.set_text(15)
#
# # 角度设置文本框
win_one.Edit2.set_text(15)
#
# # 全局安全系数文本框
win_one.Edit3.set_text(15)
#
# # RESPRINT复选框
win_one.RESPRINTCheckBox.click_input()
#
# # #STRESS复选框
win_one.STRESSCheckBox.click_input()
# # #
# # # #STRAIN复选框
win_one.STRAINCheckBox.click_input()
#
#
# #输出到include文件地址
win_one.输出到include文件Edit.set_text(17)
#
#
# # 创建按钮
win_one.Button3.click_input()





