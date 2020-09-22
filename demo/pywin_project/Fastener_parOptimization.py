from tool import KeyboardMouse,Check_winControl
from src.utils.otherMethods.initialize import pywin_openAProgram



testdicts={"所在模块":"紧固件优化->紧固件参数优化"}


aero_window, module_window = pywin_openAProgram().menuOpen(testdicts)


work = module_window.scrolledpanelwxWindowNR2   # 切换到被测工作


workField1=work.child_window(title="panel", class_name="wxWindowNR")

workField1.print_control_identifiers()