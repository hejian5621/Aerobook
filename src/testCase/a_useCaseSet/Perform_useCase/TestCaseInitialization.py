

from src.utils.otherMethods.initialize import UIA_link,pywin_openAProgram
from src.utils.otherMethods.controlOperationSuite import ControlOperationSuite
from tool import folderFile_dispose
from config.relative_location import path
from config.configurationFile import ProfileDataProcessing
from src.utils.commonality.ExcelFile import read_excel
from utils.commonality.tool import UseCase_parameterization
from src.testCase.b_testCaseStep.Aerocheck.TestCaseStep import UseCase_step
from src.utils.otherMethods.dataFormatConversion import FormatConversion
# 用例集执行前的初始化



class  module_initialize:
    """各模块测试之前数据初始化"""


    def __init__(self):
        self.property=None
        self.testCase=None

    def start_Aerobook_Aercheck(self):
        """
        启动Aerobook_Aercheck
        :param self:
        :return:
        """
        relativeAddress = path.location()  # 获取项目相对位置
        # 初始化项目的存放位置
        sourceDir = relativeAddress + r"src\testCase\projectFile\自动化测试相关文件"  # 项目有关的模板文件
        source = relativeAddress + r"src\testCase\projectFile\automateFile"  # 新建项目的保存地址
        folderFile_dispose(source).delfolder()  # 删除已有的项目文件夹
        folderFile_dispose(sourceDir).copyFile(source)  # 生成新的项目文件夹，并返回文件夹路径
        # 读取配置文档信息里的Aerobook和Aerocheck窗口的标题
        aero_title = ProfileDataProcessing("commonality", "AerobookEdition").config_File()  # 从配置文件获取Aerobook窗口标题
        aerocheck_title = ProfileDataProcessing("commonality", "AerocheckEdition").config_File()  # 从配置文件获取Aerocheck窗口标题
        # 通过AerobookEXE文件启动Aerobook，并进入进入Aerocheck页面
        py_app = pywin_openAProgram().open_accredit()  # 启动Aerobook应用程序
        uia_app = UIA_link().EntrySubapplication("Aerocheck")  # 点击Aerocheck进入Aerocheck页面
        # 新建项目
        ControlOperationSuite(aerocheck_title).childApp_newProject(py_app, "文件->项目->新建", source)
        # 独立显示底部蒙皮
        ControlOperationSuite(py_app).uia_ShowSkinSeparately(aero_title)
        #  修改配置文件内容用于执行用例的时候获取项目所在地址
        ProfileDataProcessing("commonality-Aerobook-Aerocheck", "ProjectSave_path").config_File_amend(source)


    def LaminatedataPopup(self, moduleName, UseCaseNumber, attribute_tableName):
        """

        :param moduleName:模块标识
        :param UseCaseNumber:模块标识
        :param attribute_tableName:带属性的表名称
        :return:
        """
        """在执行每一条用例之前，首先把被测窗口置顶"""
        from tool import WindowTop
        title = ProfileDataProcessing("commonality", "AerobookEdition").config_File()  # 读取配置文件信息
        WindowTop(title).console()
        # 获取初始测试用例参数
        self.testCase, self.property = module_initialize().TestCase_Data(moduleName, UseCaseNumber, attribute_tableName)
        self.property["测试主模块"]=moduleName
        # 执行初始化测试用例
        UseCase_step(self.testCase, self.property).Perform_useCase_Steps(1)


    def TestCase_Data(self,moduleName,UseCaseNumber,attribute_tableName):
        """
        测试用例数据
        :return:
        """
        ProjectPath=None
        if moduleName =="Aerobook-Aerocheck":
            ProjectPath = ProfileDataProcessing("commonality-Aerobook-Aerocheck", "ProjectSave_path").config_File()  # 获取配置文件中项目的路径
        # 获取属性信息
        real_UseCase_Name = "程序初始化用例"
        site = UseCase_parameterization().parameterization_location(moduleName,real_UseCase_Name, attribute_tableName)
        site = site[0]
        self.testCase = read_excel(site).readExcel_ControlProperties()  # 读取该测试用例中控件的操作属性
        # 获取初始化用例
        list_dicti_argument = [{"程序初始化用例": ["测试用例步骤"]}]
        list_dict_site = module_initialize().read_testCase(moduleName,list_dicti_argument)  # 读取测试用例
        for dict_site in list_dict_site:  # 取出对应模块的测试用例
            if dict_site["用例编号"] == UseCaseNumber:
                self.property = dict_site
                break
        self.property["被测程序文件地址"]=ProjectPath
        return self.testCase,self.property


    def read_testCase(self,host_moduleName,list_dicti_argument):
        """

        :return:
        """
        list_dict_site=[]
        for dicti_argument in list_dicti_argument:
            for moduleName, tableName in dicti_argument.items():
                # 获取读取电子表格的路径和相关参数
                list_dict = UseCase_parameterization().parameterization_location(host_moduleName,moduleName, tableName)
                for site in list_dict:
                    dicts = read_excel(site).readExcel_testCase()  # 读取测试用例
                    ar_testdicts = FormatConversion().RemoveSubscript(dicts,None)
                    list_dict_site = list_dict_site + ar_testdicts
        return list_dict_site
















moduleName= "Aerobook-Aerocheck"
# 执行初始化

module_initialize().start_Aerobook_Aercheck()

# module_initialize().LaminatedataPopup(moduleName,"csh001",["铺层数据库制作工具"])  # 铺层信息->铺层数据库制作工具

module_initialize().LaminatedataPopup(moduleName,"csh002",["1D单元尺寸定义（模板）"]) # 尺寸信息->一维单元尺寸定义（模板）

module_initialize().LaminatedataPopup(moduleName,"csh003",["2D单元尺寸定义（模板）"]) # 尺寸信息->二维单元尺寸定义（模板）

module_initialize().LaminatedataPopup(moduleName,"csh004",["求解计算"])             # 求解计算->求解计算

module_initialize().LaminatedataPopup(moduleName,"csh005",["载荷数据库制作工具"])     # 载荷信息->载荷数据库制作工具

module_initialize().LaminatedataPopup(moduleName,"csh006",["定义材料许用值"])        # 材料信息->定义复合材料参数

module_initialize().LaminatedataPopup(moduleName,"csh007",["定义材料许用值"])        # 材料信息->定义复合材料参数

module_initialize().LaminatedataPopup(moduleName,"csh008",["定义材料许用值"])        # 材料信息->定义复合材料参数

module_initialize().LaminatedataPopup(moduleName,"csh009",["定义材料许用值"])        # 材料信息->定义复合材料参数