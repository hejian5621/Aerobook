from src.utils.otherMethods.initialize import pywin_openAProgram
from OperatingControls.enterModule import BeingMeasured_popupWin


testdicts={"所在模块":"尺寸信息->二维单元尺寸定义"}


aero_window, module_window = pywin_openAProgram().menuOpen(testdicts)


workField = module_window.scrolledpanelwxWindowNR2   # 切换到被测工作

# workField.print_control_identifiers()


workField = module_window.scrolledpanelwxWindowNR2   # 切换到被测工作
work=workField.截面形状_wx_SysTabCtl321
workField1=work.panelwxWindowNR0



work4=workField1.复合材料_wx_SysTabCtl32
workField2=work4.wxWindowNR6




#
#
#
#
#
#
# # 选择金属材料
workField1.RadioButton2.click_input()
#
#
#
#
# # 选择复合材料
# # workField1.RadioButton1.click_input()
#
# workField3.print_control_identifiers()
#
#
# workField2.Edit.set_text("aa")

# 第一行
# workField2.double_click_input(coords=(100,10 ), button="left")



