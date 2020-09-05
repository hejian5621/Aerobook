# 初始化

from pywinauto.application import Application
import uiautomation
from config.configurationFile import ProfileDataProcessing
from src.utils.commonality.ExcelFile import read_excel
import time,os





class pywin_openAProgram:
    """打开Arobook"""


    def __init__(self):
        # 从配置文件中获取应用程序地址
        self.location = ProfileDataProcessing("commonality", "exe").config_File()
        self.aerocheck_title = ProfileDataProcessing("commonality", "AerocheckEdition").config_File()  # 从配置文件获取Aerocheck窗口标题
        self.aero_title = ProfileDataProcessing("commonality", "AerobookEdition").config_File()  # 从配置文件获取Aerobook窗口标题


    def open_accredit(self):
        """
        打开程序做授权操作，并打开Aerobook控制台
        :return:
        """
        app_window=pywin_openAProgram().passExe_open('Aerobook平台启动器')  # 打开Aerobook应用程序
        pywin_openAProgram().AuthorizedOperation(app_window)              # 进行授权操作
        Aerobook_main=pywin_openAProgram().AeroB_console(app_window)      # 链接Aerbook控制台并最大化
        return Aerobook_main



    def passExe_open(self,windowTitle):
        """
        通过exe打开被测程序,并连接窗口
        :return:
        """
        app = Application().start(self.location)  # 通过exe打开程序
        app_window = app[windowTitle]  # 连接应用程序授权窗口
        return app_window



    def AuthorizedOperation(self,app_window):
        """
        进行授权操作
        :return:
        """
        # 点击请求授权按钮
        son_window=app_window.child_window(title="本地授权",
                                           auto_id="groupBox_local", control_type="System.Windows.Forms.GroupBox")
        son_window.window(title="请求授权").wait("exists", timeout=10, retry_interval=0.1).click()
        time.sleep(0.5)
        son1_window = app_window.window(title=r'成功').wait("exists", timeout=10, retry_interval=0.1)  # 切换到授权成功窗口
        son1_window.child_window(title="确定").wait("exists", timeout=10, retry_interval=0.1).click()  # 点击确定按钮
        # 切回到Aerobook平台启动器窗口并点击运行按钮
        son2_window=app_window.window(title=r'Aerobook平台启动器').wait("exists", timeout=10, retry_interval=0.1)
        son2_window.window(title=r'运行').wait("exists", timeout=10, retry_interval=0.1).click()



    def AeroB_console(self,app_window):
        """
        操作Aerobook控制台
        :return:
        """
        Aerobook_main = app_window.window(title=self.aero_title)
        Aerobook_main.wait("exists", timeout=60, retry_interval=0.01)
        Aerobook_main.maximize()
        return Aerobook_main



    def entrance_subroutine_title(self):
        """
        进入子程序,通过标题链接
        :return:
        """
        Aero_window = Application().connect(title_re=self.aero_title,timeout=10)  # 通过Aerobook标题连接Aerobook
        Aero_window.window(title=self.aero_title).wait("exists", timeout=10, retry_interval=0.1)
        return Aero_window



    def execute_useCase_enterInto(self, testdicts):
        """
        在进行用例步骤操作时的初始化
        链接Aercheck，并点击菜单按钮
        :param testdicts:
        :return:
        """
        MenuOptions = testdicts["所在模块"]
        # 通过Aerobook标题链接Aerobook进行，并切换到Aerobook窗口
        aero_window = pywin_openAProgram().entrance_subroutine_title()
        # 进行菜单栏操作
        dlg_spec = aero_window.child_window(auto_id="panel_Graph", control_type="System.Windows.Forms.Panel")
        son_window = dlg_spec.child_window(title=self.aerocheck_title, class_name="wxWindowNR")
        son_window.menu_select(MenuOptions)# 点击菜单选项
        return aero_window,son_window


class UIA_link:


    def __init__(self):
        # 从配置文件中获取应用程序地址
        self.aero_title = ProfileDataProcessing("commonality", "AerobookEdition").config_File()  # 从配置文件获取Aerobook窗口标题


    def EntrySubapplication(self,childApp_Title):
        """
        进入子应用
        点击“Aerocheck”按钮
        :param childApp_Title:
        :return:
        """
        # 连接Aerobook控制台窗口进程
        Use = uiautomation.WindowControl(searchDepth=1, Name=self.aero_title)
        # 点击子应用，进入子应用
        Use.Control(searchDepth=4,Name=childApp_Title).Click()
        return Use






class execute_useCase_initialize:
    """执行用例之前初始化"""

    def __init__(self):
        # 读取配置文档信息
        self.aero_title = ProfileDataProcessing("commonality", "AerobookEdition").config_File()  # 从配置文件获取Aerobook窗口标题
        self.aerocheck_title = ProfileDataProcessing("commonality", "AerocheckEdition").config_File()  # 从配置文件获取Aerocheck窗口标题
        self.dict = {}


    def  link_window(self):
        """
        链接被测程序
        :return:
        """
        # 通过Aerobook标题链接Aerobook进行，并切换到Aerobook窗口
        aero_window = pywin_openAProgram().entrance_subroutine_title()
        # 从Aerobook切换到子应用
        dlg_spec1 = aero_window.child_window(auto_id="panel_Graph", control_type="System.Windows.Forms.Panel")
        dlg_spec2 = dlg_spec1.child_window(title=self.aerocheck_title, class_name="wxWindowNR")
        return dlg_spec2



    def clear_editWorkingCondition(self):
        """
        编辑工况测试前清除所有的包络工况
        :return:

        """
        from OperatingControls.enterModule import BeingMeasured_popupWin
        self.dict["所在模块"]="载荷信息->编辑工况"
        pywin_openAProgram().execute_useCase_enterInto(self.dict)
        # 切换到编辑工况弹窗
        module_window = BeingMeasured_popupWin("编辑工况").menu_LetsGoTopopover()
        while True:
            txt = module_window.ComboBox.window_text()
            if txt:
                module_window.编辑工况Button.click()
            else:
                break


    def clear_AllowableCurve(self):
        """
        清除所有的许用值曲线
        :return:
        """
        from OperatingControls.enterModule import specialWay_OperatingControls,BeingMeasured_work
        from config.relative_location import path
        from PIL import Image
        from PIL import ImageChops
        relativeAddress = path.location()  # 获取相对位置
        operationWindow="编辑材料许用值"
        self.dict["所在模块"]="材料信息->定义复合材料参数"
        aero_window, son_window = pywin_openAProgram().execute_useCase_enterInto(self.dict)
        specialWay_OperatingControls(operationWindow).uia_OperatingControls()
        module_window= BeingMeasured_work(son_window).workField_composite_information()
        dlg_spec=module_window.child_window(title="GridWindow", class_name="wxWindowNR")
        # 进行图片对比，来判断材料许用值曲线表是否为空
        # 预期截图位置location_expect
        location_expect = relativeAddress + r"src\testCase\d_useCase_screenshot\Aerocheck\expectScreenshots\aaa.png"
        # 实际截图位置
        location_actual=relativeAddress+r"src\testCase\d_useCase_screenshot\Aerocheck\ActualScreenshots\\"\
                        +"实际材料许用值曲线表截图.png"
        while True:
            # 判断实际值截图是否存在，如果存在就删掉
            result = os.path.exists(location_actual)
            if result:  # 如果存在就删除实际图片
                os.remove(location_actual)
            dlg_spec.capture_as_image().save(location_actual)  # 截取实际值图片
            # 对比截图
            image_one = Image.open(location_expect)
            image_two = Image.open(location_actual)
            diff = ImageChops.difference(image_one, image_two)
            if diff.getbbox() is None:  # 如果图片一样，就说明材料许用值曲线表里没有内容
                break
            else:  # 如果不图片一样，就说明材料许用值曲线表里有内容，就删除内容
                i=1
                dlg_spec.right_click_input(coords = (10, 10))  # 点击鼠标右键
                from pykeyboard import PyKeyboard  # 选择删除按钮
                # 选择右键下拉框的“独立显示”
                k = PyKeyboard()
                while i <=2 :
                    k.press_key(k.down_key)
                    time.sleep(0.5)
                    i = i + 1
                k.press_key(k.enter_key)
                # 删除实际截图
                result = os.path.exists(location_actual)
                if result:  # 如果存在就删除实际图片
                    os.remove(location_actual)




class  module_initialize:
    """各模块测试之前数据初始化"""


    def __init__(self):
        self.dict={}



    def sizeInformation(self):
        """
        尺寸信息--一维单元尺寸定义、二维单元尺寸定义、一维单元尺寸定义（模板）、二维单元尺寸定义（模板）
        在测试尺寸信息模块时需要进行铺层数据库的制作
        :return:
        """
        from src.testCase.b_testCaseStep.Aerocheck.TestCaseStep import Laminatedata_execute
        # 获取配置文件中项目的路径
        ProjectPath = ProfileDataProcessing("commonality", "ProjectSave_path").config_File()
        site = {"详细地址": r"src\testCase\c_useCase_file\Aerocheck\initialize\模块初始化.xlsx",
                  "表单名称": "一维二维单元尺寸定义（模块）", "初始行": 1}
        list_dicts = read_excel(site).readExcel_testCase()  # 读取测试用例
        for dicts in list_dicts:
            if dicts["用例编号"] =="铺层数据库制作":
                self.dict=  dicts
        self.dict["被测程序文件地址"] = ProjectPath
        Laminatedata_execute(self.dict).SelectFile( )  # 调用测试步骤




















