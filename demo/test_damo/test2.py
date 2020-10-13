
from tool import folderFile_dispose,Check_winControl
from config.configurationFile import ProfileDataProcessing


# title = ProfileDataProcessing("commonality", "AerobookEdition").config_File()  # 从配置文件获取Aerobook窗口标题
#
# print("title:",title)
#
#
# # Use2 = Use.Control(searchDepth=9, Name="部件(1)")
#
# control_Name="部件(1)"
#
# state = Check_winControl(title).uia_examine_control(control_Name)  # 通过弹窗的类名获取弹窗的句柄
#
#
# print("state:",state)


title="Aerobook v1.0.5"

state = Check_winControl(title).handle_win()  # 通过弹窗的类名获取弹窗的句柄