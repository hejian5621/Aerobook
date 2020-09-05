

from src.utils.otherMethods.initialize import programInitialization
from src.utils.otherMethods.controlOperationSuite import ControlOperationSuite
from config.configurationFile import ProfileDataProcessing
from tool import instrument
from config.relative_location import path
from pywinauto.application import Application
import uiautomation









# # 读取配置文档信息里的Aerobook和Aerocheck窗口的标题
# aero_title = ProfileDataProcessing("commonality", "AerobookEdition").config_File()  # 从配置文件获取Aerobook窗口标题
# aerocheck_title = ProfileDataProcessing("commonality", "AerocheckEdition").config_File()  # 从配置文件获取Aerocheck窗口标题
#
#
# app=Application().connect(title=aero_title) # 通过exe打开程序
# py_app=app.window(title=aero_title)
# # 连接应用程序，并切换到进入模型树
# # 独立显示底部蒙皮
# ControlOperationSuite(py_app).pywin_ShowSkinSeparately()




ControlOperationSuite(None).select_workingCondition()
