from tool import WindowTop
from config.configurationFile import ProfileDataProcessing
from src.utils.otherMethods.actual import Information_Win
from src.utils.commonality.ExcelFile import read_excel
from tool import folderFile_dispose,Check_winControl
from src.utils.otherMethods.initialize import execute_useCase_initialize
from utils.commonality.tool import UseCase_parameterization
from src.utils.otherMethods.dataFormatConversion import FormatConversion
from tool import pictureProcessing
import os,sys
from config.relative_location import path
from src.utils.otherMethods.initialize import pywin_openAProgram
from src.utils.otherMethods.controlOperationSuite import ControlOperationSuite_Aercheck







import time





class Initializing:
    """用例执行前需要做的操作"""

    def __init__(self):
        self.testCase=None


    def controller(self,dictSet,dict_testCase ):
        """
        在执行用例前需要要准备的操作
        dict={"全局参数":"","全局用例集名称":"","当前用例集名称":"","删除文件名列表":[],"详细地址":"","关闭弹窗":[],"控件属性已经操作方法":testCase_attribute}
        :param dictSet:
        :param dict_testCase:
        :return:
        """
        print("\033[0;32;33m《开始进行执行用例前的准备工作》\033[0m", __file__, sys._getframe().f_lineno)
        print("")
        """取出参数"""
        global_hostModule = dictSet["全局主模块名称"]
        real_hostModule = dict_testCase["测试主模块"]
        title=ProfileDataProcessing("commonality", "AerobookEdition").config_File()  # 读取配置文件信息
        """在全部用例运行前，检查Aerobook窗口是否打开"""
        handlingMethod().inspect_Aerobook(title, dictSet)
        """在执行每一条用例之前，首先把被测窗口置顶"""
        WindowTop(title).console()
        """在主模块第一次运行用例前需要做的准备工作（Aerocheck、Fiberbook等为主模块）"""
        global_hostModule = handlingMethod().host_Module_one(real_hostModule, global_hostModule)
        """在子模块第一次运行用例前需要做的准备工作"""
        testCase, global_sonmoduleName = handlingMethod().son_Module_one(dictSet, dict_testCase)
        """ 用例运行前首先检查有没有弹窗没有关闭"""
        handlingMethod().Loop_closeWindow(global_sonmoduleName,real_hostModule)
        """获取项目所在路径 """
        ProjectPath =handlingMethod().Get_Project_path(real_hostModule)
        """ 用例在执行前，首先获取信息窗口的文本信息，用于获取最新的信息窗口文本信息"""
        old_content = Information_Win().acquire_HTML_TXT(ProjectPath)
        """在用例执行前取出信息窗口里面最新的日期时间"""
        newTime=handlingMethod().infoWin_new_dateAndTime(ProjectPath)
        """用例运行前删除指定的文件"""
        folderFile_dispose(ProjectPath).delfile(dict_testCase)
        """打包参数"""
        pack_dict={"全局子模块名称":global_sonmoduleName,"全局主模块名称":global_hostModule,"项目保存路径":ProjectPath,
                   "信息窗口旧的数据":old_content,"控件属性已经操作方法":testCase,"信息窗口最新的日期时间":newTime}
        return pack_dict



class finish_clear:
    """结束清理"""

    def controller(self, dictSet):
        """
        用例步骤操作结束后
        准备如果测试失败后的截图
        关闭所有在用例执行中出现的的弹窗
        统一格式预期值和实际值
        :param dictSet:字典类型的数据集
        :return: 返回格式规范化的实际值和预期值
        """
        print("\033[0;32;33m《开始进行用例的收尾工作》\033[0m", __file__, sys._getframe().f_lineno)
        print("")
        actual_result = dictSet["实际值"]
        sole_ModuleIdentifier = dictSet["模块唯一标识"]
        moduleName=dictSet["测试主模块"]
        """在关闭弹窗前首先截图，用于如果断言失败后，在测试报告上显示测试失败的截图"""
        actuals = pictureProcessing(None).BeingMeasured_system_screenshot()
        """ 收尾，如果有警告弹框就关掉"""
        handlingMethod().Loop_closeWindow(sole_ModuleIdentifier,moduleName)
        """处理预期结果和实际结果，用以实际结果和预期结果文本对比"""
        print("\033[0;34m格式化实际值和预期值\033[0m", __file__, sys._getframe().f_lineno)
        print("")
        expect_result,location = FormatConversion().expect_dataProcessing(dictSet, actual_result)  # 格式化实际值
        print("\033[0;34m预期值：\033[0m", expect_result)
        actual_result = FormatConversion().Actual_dataProcessing(dictSet,actual_result,location)  # 格式化实际值
        print("\033[0;34m实际值：\033[0m", actual_result)
        print("")
        print("\033[0;32;35m用例收尾工作完成\033[5;33m", __file__, sys._getframe().f_lineno)
        print("")
        print(" ")
        return  expect_result,actual_result





class handlingMethod:



    def __init__(self):
        self.list_CloseWindows=[]
        self.ProjectPath=None


    def initialize_globalVariable(self, global_UseCase_Name, real_UseCase_Name):
        """
        在每一次运行用例集之前都初始化一次全局变量
        :param global_UseCase_Name: 全局变量
        :param real_UseCase_Name:  实时变量
        :return:
        """
        if global_UseCase_Name == real_UseCase_Name :
            real_arg= False
        else:
            global_UseCase_Name = real_UseCase_Name
            real_arg = True
        print("\033[0;32;34m初始化全局变量，全局变量参数：%r，全局变量模块名称：%r\033[0m" % (real_arg, global_UseCase_Name), __file__, sys._getframe().f_lineno)
        print("")
        return real_arg, global_UseCase_Name


    def Loop_closeWindow(self,sole_ModuleIdentifier,moduleName):
        """
        循环关闭窗口
        根据被测模块，检查特定模块的特定窗口
        :return:
        """
        site = {"详细地址": r"src\testCase\c_useCase_file\initialize\自动化测试公共属性.xlsx", "表单名称": moduleName,
                 "初始行": 1,"初始列":1}
        dicts_title = read_excel(site).readExcel_common()  # 从Excel表格中取出要关闭窗口的标题
        # 根据模块名称取出对应模块应该检查的弹窗标题
        if sole_ModuleIdentifier in dicts_title:
            CloseWindows=dicts_title[sole_ModuleIdentifier]
            if "；" in CloseWindows:    # 如果字典的值里有“；”，就转化成列表
                self.list_CloseWindows = CloseWindows.split("；")
            else:  # 如果字典的值里没有“；”，就强行转化成列表
                self.list_CloseWindows.append(CloseWindows)
            print("\033[0;32;34m检查%r模块，弹窗是否关闭,需要检查的弹窗标题：%r\033[0m" % (sole_ModuleIdentifier, self.list_CloseWindows), __file__, sys._getframe().f_lineno)
            for title in self.list_CloseWindows:  # 依次取出预期关闭的弹窗的标题
                Check_winControl(title).Force_close_popUp()  # 关闭弹窗
        else:
            if "全部模块" in  dicts_title:  # 如果没有找到对应模块的关闭窗口，就全部找一遍
                CloseWindows = dicts_title["全部模块"]
                if "；" in CloseWindows:  # 如果字典的值里有“；”，就转化成列表
                    self.list_CloseWindows = CloseWindows.split("；")
                else:  # 如果字典的值里没有“；”，就强行转化成列表
                    self.list_CloseWindows.append(CloseWindows)
                print("\033[0;32;34m因为该被测模块名没有找到对应关闭窗口的名称，所以全部关闭一遍，被测模块名称：%r\033[0m" % sole_ModuleIdentifier, __file__, sys._getframe().f_lineno)
                time.sleep(0.1)
                for title in self.list_CloseWindows:  # 依次取出预期关闭的弹窗的标题
                    Check_winControl(title).Force_close_popUp()  # 关闭弹窗
        print("\033[0;32;34m%r模块弹窗检查完毕\033[0m" % sole_ModuleIdentifier, __file__, sys._getframe().f_lineno)
        print("")


    def Get_Project_path(self,moduleName):
        """
        获取项目的所在路径
        :return:
        """
        # 获取项目所在路径
        if moduleName=="Aerobook-Aerocheck":
            self.ProjectPath = ProfileDataProcessing("commonality-Aerobook-Aerocheck", "ProjectSave_path").config_File()
        elif moduleName=="Aerobook-Fiberbook":
            self.ProjectPath = ProfileDataProcessing("commonality-Aerobook-Fiberbook", "ProjectSave_path").config_File()
        return  self.ProjectPath



    def host_Module_one(self,moduleName,host_Module):
        """
        在主模块第运行第一条用例时需要做的准备工作
        :return:
        """
        real_arg, global_Name = handlingMethod().initialize_globalVariable(host_Module, moduleName)  # 初始化全局变量
        if real_arg :
            """检查窗口是否在被测组模块（Aerocheck、Fiberbook等为主模块）"""
            Check_winControl(moduleName).examine_LocatedModule()
            """检查模型是否导入，老判断项目有没有你新建"""
            handlingMethod().inspect_model()  # 检查模型是否被导入
            """在每个主模块运行前先检查是否有窗口没有关闭"""
            handlingMethod().Loop_closeWindow("全部模块", moduleName)
        return global_Name


    def son_Module_one(self,dictSet,dict_testCase):
        """

        :return:
        """
        global_sonmoduleName = dictSet["全局用例集名称"]
        real_sonmoduleName = dict_testCase["模块唯一标识"]  # 实际的子模块名称
        real_hostModule = dict_testCase["测试主模块"]
        testCase = dictSet["控件属性已经操作方法"]
        """在执行子模块第一条用例前执行下面操作"""
        real_arg, global_sonmoduleName = handlingMethod().initialize_globalVariable(global_sonmoduleName, real_sonmoduleName)
        if real_arg :   # real_arg等于True，说明该模块是运行的第一条用例
            """ 取出“控件属性已经操作方法”"""
            tableName=["控件属性已经操作方法"]
            site = UseCase_parameterization().parameterization_location(real_hostModule,real_sonmoduleName, tableName)
            testCase = read_excel(site[0]).readExcel_ControlProperties()  # 读取该测试用例中控件的操作属性
            print("\033[0;32;34m获取到的Excel文档中控件属性和操作方法：\033[0m",testCase, __file__, sys._getframe().f_lineno)
            print(" ")
            """ 在模块开始前数据清理 """
            if real_sonmoduleName=="载荷信息--编辑工况":
                print("\033[0;32;34m清除包络工况：\033[0m", __file__, sys._getframe().f_lineno)
                print(" ")
                execute_useCase_initialize().clear_editWorkingCondition(real_hostModule)    # 清除所有的包络工况
        return testCase,global_sonmoduleName



    def inspect_Aerobook(self,title,dictSet):
        """
        检查Aerobook窗口是否打开
        :return:
        """
        from src.utils.otherMethods.initialize import pywin_openAProgram
        sum_number=dictSet["用例运行总次数"]
        if sum_number==0 :   # 用例运行第一次
            state = Check_winControl(title).handle_win()  # 通过弹窗的类名获取弹窗的句柄
            if state:  # 如果state的值是True,就说明Aerobook窗口没有打开
                print("启动%r模块"%title)
                pywin_openAProgram().open_accredit()  # 启动Aerobook应用程序



    def inspect_model(self):
        """
        检查模型是否被导入
        :return:
        """
        title = ProfileDataProcessing("commonality", "AerobookEdition").config_File()  # 从配置文件获取Aerobook窗口标题
        control_Name = "部件(1)"
        state = Check_winControl(title).uia_examine_control(control_Name)  # 通过弹窗的类名获取弹窗的句柄
        if state: # 如果模型没有导入就说明没有新建项目，下面就新建项目
            relativeAddress = path.location()  # 获取项目相对位置
            # 初始化项目的存放位置
            sourceDir = relativeAddress + r"src\testCase\projectFile\自动化测试相关文件"  # 项目有关的模板文件
            source = relativeAddress + r"src\testCase\projectFile\automateFile"  # 新建项目的保存地址
            folderFile_dispose(source).delfolder()  # 删除已有的项目文件夹
            folderFile_dispose(sourceDir).copyFile(source)  # 生成新的项目文件夹，并返回文件夹路径
            # 读取配置文档信息里的Aerobook和Aerocheck窗口的标题
            aero_title = ProfileDataProcessing("commonality", "AerobookEdition").config_File()  # 从配置文件获取Aerobook窗口标题
            aerocheck_title = ProfileDataProcessing("commonality", "AerocheckEdition").config_File()  # 从配置文件获取Aerocheck窗口标题
            # 链接被测系统
            # 通过Aerobook标题链接Aerobook进行，并切换到Aerobook窗口
            py_app = pywin_openAProgram().entrance_subroutine_title()
            # 新建项目
            ControlOperationSuite_Aercheck(aerocheck_title).childApp_newProject(py_app, "文件->项目->新建", source)
            # 独立显示底部蒙皮
            ControlOperationSuite_Aercheck(py_app).uia_ShowSkinSeparately(aero_title)
            #  修改配置文件内容用于执行用例的时候获取项目所在地址
            ProfileDataProcessing("commonality-Aerobook-Aerocheck", "ProjectSave_path").config_File_amend(source)


    def infoWin_new_dateAndTime(self,ProjectPath):
        """
        取出信息窗口最新的时间
        :return:
        """
        import datetime
        from utils.commonality.tool import htmlFormat
        today = str(datetime.date.today())  # datetime.date类型当前日期
        HTML_address = ProjectPath+"\\"+"Aerocheck_prjLog_" + today + ".html"
        list_time=htmlFormat().takeOut_html_dateAndtime(HTML_address)
        if list_time :
            newTime=list_time[-1]
        else:
            newTime=today
        return newTime