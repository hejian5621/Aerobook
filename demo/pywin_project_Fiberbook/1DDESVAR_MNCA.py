# 1D单元设计变量（截面积）



from src.utils.otherMethods.initialize import pywin_openAProgram

from OperatingControls.enterModule import ctrW_AeroAerochcek
import time
from src.utils.OperatingControls.moduleControlOperation import OperatingControls

from OperatingControls.enterModule import BeingMeasured_popupWin


from OperatingControls.enterModule import ctrW_AeroFiberbook


testdicts={"所在模块":"优化->优化设置->设计变量->一维单元设计变量（截面积）"}
module="Aerobook-Fiberbook"



aero_window, son_window = pywin_openAProgram(module).menuOpen(testdicts)


win_one =ctrW_AeroFiberbook(son_window).workField_general()

win_one.print_control_identifiers()


# 截面积下限
win_one.Edit1.set_text("11111")

# 截面积上限
win_one.Edit2.set_text("11111")

# 所有选中单元共享变量
win_one.GroupBox.click_input()

# 属性卡片起始ID
win_one.Edit3.set_text("11111")

# 材料卡片起始ID
win_one.Edit4.set_text("11111")

# 选择结构单元
win_one.child_window(title="选择结构单元", class_name="Button").click()

# 输出到include文件
win_one.Edit5.set_text("11111")

# 创建
win_one.Button2.click_input()

# 关闭
# win_one.Button3.click()
