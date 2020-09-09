#求解计算->求解计算


from src.utils.otherMethods.initialize import execute_useCase_initialize,pywin_openAProgram
from OperatingControls.enterModule import BeingMeasured_work
import sys,os,time




inModule="求解计算->求解计算"


txet=r"F:\Aerobook\demo\pywin_ToFindControl"

testdicts={}

testdicts["所在模块"] = "尺寸信息->一维单元尺寸定义（模板）"


aero_window, son_window = pywin_openAProgram().execute_useCase_enterInto(testdicts)


dlg_spec=BeingMeasured_work(son_window).workField_general()

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
# dlg_spec.属性更新Button.click()
# time.sleep(2)
#
# # 点击求解计算按钮
# dlg_spec.求解计算.click()
# time.sleep(4)

# # 点击载荷提取按钮
# dlg_spec.载荷提取Button.click()
