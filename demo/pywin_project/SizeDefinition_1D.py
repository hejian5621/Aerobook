


from src.utils.otherMethods.initialize import pywin_openAProgram
from OperatingControls.enterModule import BeingMeasured_popupWin


testdicts={"所在模块":"尺寸信息->一维单元尺寸定义"}


aero_window, module_window = pywin_openAProgram().menuOpen(testdicts)






























workField = module_window.scrolledpanelwxWindowNR2   # 切换到被测工作
work=workField.截面形状_wx_SysTabCtl321
workField1=work.panelwxWindowNR0



work15=workField1.panelwxWindowNR13

workField1.print_control_identifiers()


# 进入截面参数文本框中
work2=workField1.grid1
workField2=work2.GridWindowwxWindowNR0




# 进入复合材料表格窗口中
work4=workField1.复合材料_wx_SysTabCtl32
work5=work4.panelwxWindowNR1
work6=work5.gridwxWindowNR
workField3=work6.wxWindowNR6





# 进入金属材料
work4=workField1.复合材料_wx_SysTabCtl32
work5=work4.panel5
workField4=work5.GridWindow2












# ork10 = workField1.child_window(title="panel", class_name="wxWindowNR")
#
# work10.ComboBox2.select("Y轴")


# work10=workField1.child_window(title="X轴", class_name="ComboBox").select("Y轴")


# work10.select("Y轴")
#
# txt=work10.window_text()
#
# print("txt:",txt)
#
# workField1.child_window(title="全局坐标系", class_name="ComboBox").select("全局坐标系")







# workField5.print_control_identifiers()


# 选择截面形状

# workField.ComboBox0.select("L型")


# # 第一行
# workField2.double_click_input(coords=(150,10 ), button="left")
#
# workField2.Edit.set_text("555")
#
#
# # 第二行
#
# workField2.double_click_input(coords=(150,30 ), button="left")
#
# workField2.Edit.set_text("555")
#
#
# # 第三行
#
# workField2.double_click_input(coords=(150,50 ), button="left")
#
# workField2.Edit.set_text("555")
#
#
# # 第四行
#
# workField2.double_click_input(coords=(150,70 ), button="left")
#
# workField2.Edit.set_text("555")



# 选择金属材料
workField1.RadioButton2.click_input()

# 选择复合材料
# workField1.RadioButton1.click_input()


# 进入复合材料表格窗口中
# work4=workField1.复合材料_wx_SysTabCtl32
# work5=work4.panelwxWindowNR1
# work6=work5.gridwxWindowNR
# workField3=work6.wxWindowNR6












#第一行
# workField3.double_click_input(coords=(150,10 ), button="left")


# 第二行
# workField3.double_click_input(coords=(150,30 ), button="left")

# 第三行

# workField3.double_click_input(coords=(150,50 ), button="left")





#第一行
workField4.double_click_input(coords=(30,10 ), button="left")
workField4.Edit.set_text("777")




#第二行
workField4.click_input(coords=(30,30), button="left")
workField4.double_click_input(coords=(30,30), button="left")
workField4.Edit.set_text("888")




#第三行
workField4.click_input(coords=(30,50), button="left")
workField4.double_click_input(coords=(30,50), button="left")
workField4.Edit.set_text("999")