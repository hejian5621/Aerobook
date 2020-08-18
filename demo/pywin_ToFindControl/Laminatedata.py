
from src.utils.otherMethods.Initialize import programInitialization
from pywinauto.application import Application
from config.configurationFile import ProfileDataProcessing
from OperatingControls.EnterModule import open_module



import time

inModule="铺层信息->铺层数据库制作工具"

aero_title = ProfileDataProcessing("commonality", "AerobookEdition").config_File()  # 从配置文件获取Aerobook窗口标题
aerocheck_title = ProfileDataProcessing("commonality", "AerocheckEdition").config_File()  # 从配置文件获取Aerocheck窗口标题

# 通过Aerobook标题链接Aerobook进行，并切换到Aerobook窗口
aero_window = programInitialization().entrance_subroutine_title(aero_title)
# 通过操作菜单栏，打开被测模块，然后切换到被测模块
module_window = open_module().menu_Laminatedata(inModule, aero_window, aerocheck_title)





