# 尺寸定义

from OperatingControls.enterModule import ctrW_AeroAerochcek



from src.utils.otherMethods.initialize import pywin_openAProgram



testCase_attribute={"所在模块":"尺寸信息->一维单元尺寸定义（模板）"}


module="Aerobook-Aerocheck"
aero_window, son_window = pywin_openAProgram(module).menuOpen(testCase_attribute)

print(1)
# 切入铺层数据库工具弹窗中
module_window = ctrW_AeroAerochcek(son_window).workField_sizeInfo()

print(2)
module_window.print_control_identifiers()

# 材料类型单选框，勾选金属材料
# module_window.RadioButton2.click()
#
# #材料类型单选框，勾选复合材料
#
# module_window.RadioButton.click()

# 选择路径按钮

module_window.Button.click()

# 选择路径文本框

module_window.Edit.set_text("aa")