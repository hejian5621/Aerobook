

from src.utils.otherMethods.initialize import UIA_link,pywin_openAProgram
from src.utils.otherMethods.controlOperationSuite import ControlOperationSuite
from tool import folderFile_dispose
from config.relative_location import path
from config.configurationFile import ProfileDataProcessing
from src.utils.commonality.ExcelFile import read_excel
from utils.commonality.tool import UseCase_parameterization
from src.testCase.b_testCaseStep.Aerocheck.TestCaseStep import UseCase_step
# 用例集执行前的初始化



class  module_initialize:
    """各模块测试之前数据初始化"""


    def __init__(self):
        self.testCase_dict=None
        self.testCase_attribute=None


    def TestCase_Data(self,UseCaseNumber,attribute_tableName):
        """
        测试用例数据
        :return:
        """
        ProjectPath = ProfileDataProcessing("commonality", "ProjectSave_path").config_File()  # 获取配置文件中项目的路径
        # 获取属性信息
        real_UseCase_Name = "程序初始化用例"
        site = UseCase_parameterization().parameterization_location(real_UseCase_Name, attribute_tableName)
        site = site[0]
        self.testCase_attribute = read_excel(site).readExcel_ControlProperties()  # 读取该测试用例中控件的操作属性
        # 获取初始化用例
        list_dicti_argument = [{"程序初始化用例": ["测试用例步骤"]}]
        list_dict_site, list_testPoint = UseCase_parameterization().parameterization_data(list_dicti_argument)  # 读取测试用例
        for dict_site in list_dict_site:  # 取出对应模块的测试用例
            if dict_site["用例编号"] == UseCaseNumber:
                self.testCase_dict = dict_site
                break
        self.testCase_dict["被测程序文件地址"]=ProjectPath
        return self.testCase_attribute,self.testCase_dict





    def start_Aerobook_Aercheck(self):
        """
        启动Aerobook_Aercheck
        :param self:
        :return:
        """
        relativeAddress = path.location()  # 获取项目相对位置
        # 初始化项目的存放位置
        sourceDir = relativeAddress + r"src\testCase\projectFile\自动化测试相关文件"   # 项目有关的模板文件
        source = relativeAddress + r"src\testCase\projectFile\automateFile"          # 新建项目的保存地址
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
        ProfileDataProcessing("commonality", "ProjectSave_path").config_File_amend(source)



    def LaminatedataPopup(self,UseCaseNumber,attribute_tableName):
        """

        :param UseCaseNumber:模块标识
        :param attribute_tableName:带属性的表名称
        :return:
        """
        # 获取初始测试用例参数
        self.testCase_attribute,self.testCase_dict=module_initialize().TestCase_Data(UseCaseNumber,attribute_tableName)
        # 执行初始化测试用例
        UseCase_step(self.testCase_attribute,self.testCase_dict).Perform_useCase_Steps()




# 执行初始化

module_initialize().start_Aerobook_Aercheck()

module_initialize().LaminatedataPopup("csh001",["铺层数据库制作工具"])  # 铺层信息->铺层数据库制作工具

module_initialize().LaminatedataPopup("csh002",["1D单元尺寸定义（模板）"]) # 尺寸信息->一维单元尺寸定义（模板）

module_initialize().LaminatedataPopup("csh003",["2D单元尺寸定义（模板）"]) # 尺寸信息->二维单元尺寸定义（模板）

module_initialize().LaminatedataPopup("csh004",["求解计算"])             # 求解计算->求解计算

module_initialize().LaminatedataPopup("csh005",["载荷数据库制作工具"])     # 载荷信息->载荷数据库制作工具

module_initialize().LaminatedataPopup("csh006",["定义材料许用值"])        # 材料信息->定义复合材料参数

module_initialize().LaminatedataPopup("csh007",["定义材料许用值"])        # 材料信息->定义复合材料参数

module_initialize().LaminatedataPopup("csh008",["定义材料许用值"])        # 材料信息->定义复合材料参数

module_initialize().LaminatedataPopup("csh009",["定义材料许用值"])        # 材料信息->定义复合材料参数