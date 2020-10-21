
# 平板稳定性响应约束


from src.utils.otherMethods.initialize import pywin_openAProgram
import time

from OperatingControls.enterModule import ctrW_AeroFiberbook


time.sleep(2)

testdicts={"所在模块":"优化->优化设置->稳定性设计响应->平板稳定性响应约束"}
module="Aerobook-Fiberbook"


aero_window, son_window = pywin_openAProgram(module).menuOpen(testdicts)


win_one =ctrW_AeroFiberbook(son_window).workField_general()

win_one.print_ctrl_ids ()


win_one.RadioButton10.click_input()

win_one.Edit5.set_text("11")