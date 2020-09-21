
from src.utils.OperatingControls.moduleControlOperation import OperatingControls

from src.utils.otherMethods.initialize import pywin_openAProgram


testdicts={"所在模块":"紧固件强度校核->紧固件参数设置"}
aero_window, module_window = pywin_openAProgram().menuOpen(testdicts)


workField1 = module_window.scrolledpanelwxWindowNR2   # 切换到被测工作








discern={"唯一标识":"150；30；GroupBox3","控件类型":"坐标--键盘--文本框"}



arguments="20"

OperatingControls(workField1).coord_click_textbox(discern,arguments)