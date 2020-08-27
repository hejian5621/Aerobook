from src.utils.otherMethods.initialize import programInitialization
from src.utils.otherMethods.controlOperationSuite import ControlOperationSuite
from config.configurationFile import ProfileDataProcessing
from src.utils.commonality.tool import instrument
from demo.copyFile.copyFile3 import kk

sourceDir = r"F:\Aerobook\src\testCase\projectFile\自动化测试相关文件"
source = r"F:\Aerobook\src\testCase\projectFile\automateFile"

instrument().delfolder()    # 删除已有的项目文件夹
instrument().copyFile(sourceDir, source)   # 生成新的项目文件夹，并返回文件夹路径
print("项目所在地址:",source)



# 读取配置文档信息里的Aerobook和Aerocheck窗口的标题
aero_title = ProfileDataProcessing("commonality", "AerobookEdition").config_File()  # 从配置文件获取Aerobook窗口标题
aerocheck_title = ProfileDataProcessing("commonality", "AerocheckEdition").config_File()  # 从配置文件获取Aerocheck窗口标题


# 变量
childApp_Name="Aerocheck"  # 被侧子模块名称
MenuOptions="文件->项目->新建"   # 菜单栏点击按钮


# 启动应用程序并进入被测子模块页面
py_app=programInitialization(aero_title).open_accredit()    # 启动Aerobook应用程序
uia_app=programInitialization(aero_title).EntrySubapplication(childApp_Name)  # 点击Aerocheck进入Aerocheck页面


# 新建项目
ControlOperationSuite(aerocheck_title).childApp_newProject(py_app,MenuOptions,source)


# 独立显示底部蒙皮
ControlOperationSuite(py_app).ShowSkinSeparately()

ProfileDataProcessing("commonality","ProjectSave_path").\
    config_File_amend(source)