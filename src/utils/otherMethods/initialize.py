# 初始化

from pywinauto.application import Application
import uiautomation
from config.configurationFile import ProfileDataProcessing
from src.utils.commonality.ExcelFile import read_excel
import time,os





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
        time.sleep(0.5)
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
        # 读取配置文档信息
        self.aero_title = ProfileDataProcessing("commonality", "AerobookEdition").config_File()  # 从配置文件获取Aerobook窗口标题
        self.aerocheck_title = ProfileDataProcessing("commonality", "AerocheckEdition").config_File()  # 从配置文件获取Aerocheck窗口标题


    def  link_window(self):
        """
        链接被测程序
        :return:
        """
        # 通过Aerobook标题链接Aerobook进行，并切换到Aerobook窗口
        aero_window = programInitialization(self.aero_title).entrance_subroutine_title()
        # 从Aerobook切换到子应用
        dlg_spec1 = aero_window.child_window(auto_id="panel_Graph", control_type="System.Windows.Forms.Panel")
        dlg_spec2 = dlg_spec1.child_window(title=self.aerocheck_title, class_name="wxWindowNR")
        return dlg_spec2


    def execute_useCase_enterInto(self, testdicts):
        """
        执行用例
        :param testdicts:
        :return:
        """
        MenuOptions = testdicts["所在模块"]
        # 通过Aerobook标题链接Aerobook进行，并切换到Aerobook窗口
        aero_window = programInitialization(self.aero_title).entrance_subroutine_title()
        # 进行菜单栏操作
        dlg_spec = aero_window.child_window(auto_id="panel_Graph", control_type="System.Windows.Forms.Panel")
        son_window = dlg_spec.child_window(title=self.aerocheck_title, class_name="wxWindowNR")
        # 点击菜单选项
        son_window.menu_select(MenuOptions)
        return aero_window,son_window









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
        actual_Text,edit_list = Laminatedata_execute(self.dict).SelectFile( )  # 调用测试步骤








    def clear_editWorkingCondition(self):
        """
        编辑工况测试前清除所有的包络工况
        :return:

        """
        from OperatingControls.enterModule import BeingMeasured_popupWin
        self.dict["所在模块"]="载荷信息->编辑工况"
        execute_useCase_initialize().execute_useCase_enterInto(self.dict)
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
        testdicts={}
        testdicts["所在模块"]="材料信息->定义复合材料参数"
        aero_window, son_window = execute_useCase_initialize().execute_useCase_enterInto(testdicts)
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














