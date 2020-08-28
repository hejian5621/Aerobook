# 初始化

from pywinauto.application import Application
import uiautomation
from config.configurationFile import ProfileDataProcessing
from src.utils.commonality.ExcelFile import read_excel
import time
from src.utils.otherMethods.controlOperationSuite import ControlOperationSuite




class programInitialization:
    """程序初始化"""


    def __init__(self,windowTitle):
        # 窗口标题
        self.windowTitle=windowTitle


    def open_accredit(self):
        """
        打开程序做授权操作，并打开Aerobook控制台
        :return:
        """
        # 读取配置文档信息
        aero_title = ProfileDataProcessing("commonality", "exe").config_File()  # 从配置文件获取Aerobook窗口标题
        app = Application().start(aero_title) # 通过exe打开程序
        dlg_spec = app['Aerobook平台启动器']   # 连接Aerobook授权窗口
        # 点击请求授权按钮
        dlg_spec1 = dlg_spec1=dlg_spec.child_window(title="本地授权", auto_id="groupBox_local",
                                control_type="System.Windows.Forms.GroupBox").window(title="请求授权").\
            wait("exists", timeout=10, retry_interval=0.1).click()
        dlg_spec2 = app.window(title=r'成功') # 切换到授权成功窗口
        dlg_spec2.child_window(title="确定").wait("exists", timeout=10, retry_interval=0.1).click()
        # 在授权成功窗口点击确定按钮
        # 切回到Aerobook平台启动器窗口并点击运行按钮
        app.window(title=r'Aerobook平台启动器').window(title=r'运行').wait("exists", timeout=10, retry_interval=0.1).click()
        # 切换到Aerobook主窗口
        Aerobook_main = app.window(title=self.windowTitle)
        Aerobook_main.wait("exists",timeout=60,retry_interval=0.01)
        Aerobook_main.maximize()
        return Aerobook_main



    def entrance_subroutine_coord(self):
        """
        进入子程序，通过坐标的方法进入
        :return:
        """




    def entrance_subroutine_title(self):
        """
        进入子程序,通过标题链接
        :return:
        """
        Aero_window = Application().connect(title_re=self.windowTitle).window(title=self.windowTitle)  # 通过Aerobook标题连接Aerobook
        return Aero_window



    def EntrySubapplication(self,childApp_Title):
        """
        进入子应用
        点击“Aerocheck”按钮
        :param childApp_Title:
        :return:
        """
        # 连接Aerobook控制台窗口进程
        Use = uiautomation.WindowControl(searchDepth=1, Name=self.windowTitle)
        # 点击子应用，进入子应用
        Use.Control(searchDepth=4,Name=childApp_Title).Click()
        return Use


class execute_useCase_initialize:
    """执行用例初始化"""

    def __init__(self):
        pass



    def execute_useCase_enterInto(self, testdicts):
        """
        执行用例
        :param testdicts:
        :return:
        """
        from OperatingControls.enterModule import open_module
        MenuOptions = testdicts["所在模块"]
        # 读取配置文档信息
        aero_title = ProfileDataProcessing("commonality", "AerobookEdition").config_File()  # 从配置文件获取Aerobook窗口标题
        aerocheck_title = ProfileDataProcessing("commonality", "AerocheckEdition").config_File()  # 从配置文件获取Aerocheck窗口标题
        # 通过Aerobook标题链接Aerobook进行，并切换到Aerobook窗口
        aero_window = programInitialization(aero_title).entrance_subroutine_title()
        # 进行菜单栏操作
        son_window = ControlOperationSuite(None).menuBar_operation(aero_window, MenuOptions, aerocheck_title)
        return aero_window,son_window



class  module_initialize:
    """各模块测试之前数据初始化"""


    def __init__(self):
        pass



    def sizeInformation(self):
        """
        尺寸信息--一维单元尺寸定义、二维单元尺寸定义、一维单元尺寸定义（模板）、二维单元尺寸定义（模板）
        在测试尺寸信息模块时需要进行铺层数据库的制作
        :return:
        """
        from src.testCase.b_testCaseStep.Aerocheck.TestCaseStep import Laminatedata_execute
        dict_Laminatedata={}
        # 获取配置文件中项目的路径
        ProjectPath = ProfileDataProcessing("commonality", "ProjectSave_path").config_File()
        site = {"详细地址": r"src\testCase\c_useCase_file\Aerocheck\initialize\模块初始化.xlsx",
                  "表单名称": "一维二维单元尺寸定义（模块）", "初始行": 1}
        list_dicts = read_excel(site).readExcel_testCase()  # 读取测试用例
        for dicts in list_dicts:
            if dicts["用例编号"] =="铺层数据库制作":
                dict_Laminatedata=  dicts
        dict_Laminatedata["被测程序文件地址"] = ProjectPath
        actual_Text,edit_list = Laminatedata_execute().SelectFile(dict_Laminatedata)  # 调用测试步骤


    def editWorkingCondition(self):
        """
        编辑工况测试前清除所有的包络工况
        :return:

        """
        from OperatingControls.enterModule import open_module
        testdicts={}
        testdicts["所在模块"]="载荷信息->编辑工况"
        aero_window,son_window =execute_useCase_initialize().execute_useCase_enterInto(testdicts)
        # 切换到编辑工况弹窗
        module_window = open_module().menu_editWorkingCondition()
        while True:
            txt = module_window.ComboBox.window_text()
            if txt:
                module_window.编辑工况Button.click()
            else:
                break















