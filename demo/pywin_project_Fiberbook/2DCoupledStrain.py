

from src.utils.otherMethods.initialize import pywin_openAProgram

from OperatingControls.enterModule import ctrW_AeroAerochcek
import time
from src.utils.OperatingControls.moduleControlOperation import OperatingControls

from OperatingControls.enterModule import BeingMeasured_popupWin
# 二维单元应变耦合DRESP3

from OperatingControls.enterModule import ctrW_AeroFiberbook


time.sleep(2)

testdicts={"所在模块":"优化->优化设置->应变设计响应->二维单元应变耦合DRESP3"}
module="Aerobook-Fiberbook"

# dump_tree(depth=None, filename=None)  #打印'标识符'

# print_ctrl_ids  #打印'标识符'

aero_window, son_window = pywin_openAProgram(module).menuOpen(testdicts)


win_one =ctrW_AeroFiberbook(son_window).workField_general()

win_one.print_ctrl_ids ()




# 拉伸许用应文本框
win_one.Edit1.set_text("11")

# 压缩许用应变文本框
win_one.Edit2.set_text("11")

# 剪切许用应变文本框
win_one.Edit3.set_text("11")

# 安全系数文本框
win_one.Edit4.set_text("11")


# 应变位置下拉框
win_one.ComboBox.select("下表面")

# 选择结构单元
win_one.child_window(title="选择单元", class_name="Button").click_input()

# 输出到include文本框
win_one.Edit5.set_text("11")

#  创建按钮
win_one.Button2.click_input()

#  关闭按钮
# win_one.Button3.click_input()