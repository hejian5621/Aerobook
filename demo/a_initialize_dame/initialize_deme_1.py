from src.utils.otherMethods.initialize import UIA_link,pywin_openAProgram
from src.utils.otherMethods.controlOperationSuite import ControlOperationSuite
from config.configurationFile import ProfileDataProcessing
from tool import folderFile_dispose
from config.relative_location import path
from pywinauto.application import Application



# # 链接Aerobook
# app = Application().connect(title="Aerobook v1.0.4") # 通过exe打开程序
# py_app = app.window(title="Aerobook v1.0.4")
#
# py_app.print_control_identifiers()




relativeAddress = path.location()  # 获取项目相对位置

sourceDir = relativeAddress +r"src\testCase\projectFile\自动化测试相关文件"
source =relativeAddress +r"src\testCase\projectFile\automateFile"


folderFile_dispose(source).delfolder()    # 删除已有的项目文件夹
folderFile_dispose(sourceDir).copyFile(source)   # 生成新的项目文件夹，并返回文件夹路径
print("项目所在地址:",source)



# 读取配置文档信息里的Aerobook和Aerocheck窗口的标题
aero_title = ProfileDataProcessing("commonality", "AerobookEdition").config_File()  # 从配置文件获取Aerobook窗口标题
aerocheck_title = ProfileDataProcessing("commonality", "AerocheckEdition").config_File()  # 从配置文件获取Aerocheck窗口标题



print("aero_title:",aero_title )
print("aerocheck_title:",aerocheck_title)


# 变量
childApp_Name="Aerocheck"  # 被侧子模块名称
MenuOptions="文件->项目->新建"   # 菜单栏点击按钮




# # 启动应用程序并进入被测子模块页面
py_app=pywin_openAProgram().open_accredit()    # 启动Aerobook应用程序
uia_app=UIA_link().EntrySubapplication(childApp_Name)  # 点击Aerocheck进入Aerocheck页面





# 新建项目
ControlOperationSuite(aerocheck_title).childApp_newProject(py_app,MenuOptions,source)


# 独立显示底部蒙皮
ControlOperationSuite(py_app).uia_ShowSkinSeparately(aero_title)




#  修改配置文件内容
ProfileDataProcessing("commonality","ProjectSave_path").\
    config_File_amend(source)