#求解计算->求解计算


from src.utils.otherMethods.initialize import execute_useCase_initialize,pywin_openAProgram
from OperatingControls.enterModule import ctrW_AeroAerochcek
import sys,os,time





txet=r"F:\Aerobook\demo\pywin_ToFindControl"

testdicts ={"所在模块":"求解计算->求解计算"}

module="Aerobook-Aerocheck"
aero_window, son_window = pywin_openAProgram(module).menuOpen(testdicts)


dlg_spec=ctrW_AeroAerochcek(son_window).workField_general()


dlg_spec.print_control_identifiers()


# 属性更新对应的路径的文本框
# dlg_spec.Edit.set_text(txet)


# 载荷提取对应的路径文本框
# dlg_spec.Edit2.set_text(txet)


# 点击属性更新路径对应的浏览按钮
# dlg_spec.Button2.click()
# time.sleep(2)

# # 点击载荷提取对应的浏览按钮
# dlg_spec.Button3.click()
# time.sleep(2)

# # 点击属性更新按钮
# dlg_spec.Button4.click()
# time.sleep(2)
#
# # 点击求解计算按钮
# dlg_spec.求解计算.click()
# time.sleep(4)

# # 点击载荷提取按钮
# dlg_spec.载荷提取Button.click()
