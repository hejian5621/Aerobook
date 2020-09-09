# 材料信息--复合材料需用值定义

from config.configurationFile import ProfileDataProcessing
from src.utils.otherMethods.initialize import pywin_openAProgram
from src.utils.otherMethods.initialize import execute_useCase_initialize
from OperatingControls.enterModule import BeingMeasured_popupWin,specialWay_OperatingControls,BeingMeasured_work
import uiautomation
from pywinauto.application import Application
import time



testdicts={"所在模块":"材料信息->定义复合材料参数"}

# 在菜单栏中点击"材料信息->定义复合材料参数"
from config.configurationFile import ProfileDataProcessing
aero_window, son_window = pywin_openAProgram().execute_useCase_enterInto(testdicts)

pywin_openAProgram().execute_useCase_enterInto(self.testdicts)


Aero_window = Application().connect(title_re="Aerobook v1.0.4").window(title="Aerobook v1.0.4")  # 通过Aerobook标题连接Aerobook

dlg_spec = Aero_window.选择材料许用值曲线_wx_SysTabCtl32
dlg_spec1 = dlg_spec.panelwxWindowNR0
# dlg_spec1.print_control_identifiers()





# 点击选项卡
aero_title = ProfileDataProcessing("commonality", "AerobookEdition").config_File()  # 从配置文件获取Aerobook窗口标题
Use = uiautomation.WindowControl(searchDepth=1, Name=aero_title)









specialWay_OperatingControls("编辑材料许用值").uia_OperatingControls()

dlg_spec=BeingMeasured_work(son_window).workField_composite_information()

# dlg_spec.print_control_identifiers()




time.sleep(1)

"""切换到编辑材料需用值"""
# 点击”创建材料许用值曲线“按钮
# dlg_spec2=dlg_spec1.child_window(title="创建材料许用值曲线", class_name="Button")
# dlg_spec2.click()




"""切换到“编辑材料许用值曲线”弹框"""
# dlg_spec3=open_module().menu_LetsGoTopopover("编辑材料许用值曲线")


# # 在曲线文本框中输入内容
# dlg_spec3.Edit2.set_text("sa")
#
# # 切换到网格窗口
# dlg_spec5=dlg_spec3.child_window(title="GridWindow", class_name="wxWindowNR")
# # 在第一行,X轴
# dlg_spec5.double_click_input(coords = (40, 20),button ="left")
# dlg_spec5.Edit.set_text("0")
#
# # # 在第一行,Y轴
# dlg_spec5.double_click_input(coords = (180, 20),button ="left")
# dlg_spec5.Edit.set_text("4500")
#
# dlg_spec3.Edit2.set_text("sa")
#
# dlg_spec3.确认.click()



# # 第二行,X轴
# dlg_spec5.double_click_input(coords = (40, 40),button ="left")
# # 第三行,X轴
# dlg_spec5.click_input(coords = (40, 60),double = True)

# # 第二行,Y轴
# dlg_spec5.double_click_input(coords = (180, 40),button ="left")
# # 第三行,Y轴
# dlg_spec5.double_click_input(coords = (180, 60),button ="left")


# dlg_spec5.print_control_identifiers()

print("__________________________________________________")





"""定义材料许用值"""
# 点击"拉伸"对于的"+"按钮
# dlg_spec1.Button0.click()

# dlg_spec1.print_control_identifiers()
#
dlg_spec3=BeingMeasured_popupWin("选择材料许用值曲线").menu_LetsGoTopopover()
#
# dlg_spec4=dlg_spec3.child_window(title="GridWindow", class_name="wxWindowNR")
#
#
#
# dlg_spec4.double_click_input(coords=(50, 10), button="left")
#
dlg_spec3.print_control_identifiers()

dlg_spec3.确认.move_mouse()

# dlg_spec3.确认.click()

#


from tool import instrument

# 选择结构单元
# dlg_spec1.child_window(title="选择结构单元", class_name="Button").click()
#
# instrument().selectionModel()




"""获取”编辑材料许用值--材料许用值曲线表“中的值"""
# #
# # dlg_spec1.print_control_identifiers()
# dlg_spec2=dlg_spec1.child_window(title="GridWindow", class_name="wxWindowNR")
#
#
#
# print("使用方法",dir(dlg_spec2.wrapper_object()))
# #
# dlg_spec2.move_mouse()
# #
# # print("txt:",txt)




