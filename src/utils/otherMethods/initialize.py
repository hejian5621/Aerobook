# 初始化

from pywinauto.application import Application
import uiautomation
from config.configurationFile import ProfileDataProcessing
import time,os
from OperatingControls.enterModule import specialWay_OperatingControls
import win32gui


"""打开Arobook"""
class pywin_openAProgram:
    """打开Arobook"""


    def __init__(self, module=None):
        # 从配置文件中获取应用程序地址
        self.module=module
        self.location = ProfileDataProcessing("commonality", "exe").config_File()
        self.aero_title = ProfileDataProcessing("commonality", "AerobookEdition").config_File()  # 从配置文件获取Aerobook窗口标题
        if  module =="Aerobook-Aerocheck":
            self.aero_module_title = ProfileDataProcessing("commonality", "AerocheckEdition").config_File()  # 从配置文件获取Aerocheck窗口标题
        elif module =="Aerobook-Fiberbook":
            self.aero_module_title = ProfileDataProcessing("commonality", "FiberbookEdition").config_File()  # 从配置文件获取Aerocheck窗口标题
        elif module == "Aerobook-Fembook":
            self.aero_module_title = ProfileDataProcessing("commonality", "FembookEdition").config_File()  # 从配置文件获取Aerocheck窗口标题
        else:
            self.aero_module_title =None





    def open_accredit(self):
        """
        打开程序做授权操作，并打开Aerobook控制台
        :return:
        """
        app_window=pywin_openAProgram().passExe_open('Aerobook平台启动器')  # 打开Aerobook应用程序
        pywin_openAProgram().AuthorizedOperation(app_window)              # 进行授权操作
        time.sleep(1)
        Aerobook_main=pywin_openAProgram().AeroB_console()      # 链接Aerbook控制台并最大化
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
        son_window.window(title="请求授权").wait("exists", timeout=10, retry_interval=0.1).click_input()
        succeed_window=Application().connect(title_re=r'成功',timeout=10)
        succeed1_window=succeed_window.window(title_re=r'成功')
        # succeed1_window.print_control_identifiers()
        succeed1_window.child_window(title="确定").wait("exists", timeout=10, retry_interval=0.1).click_input()  # 点击确定按钮
        # 切回到Aerobook平台启动器窗口并点击运行按钮
        app_window.window(title=r'运行').wait("exists", timeout=10, retry_interval=0.1).click_input()



    def AeroB_console(self):
        """
        操作Aerobook控制台,并且最大化北侧系统
        :return:
        """
        Aerobook_main=pywin_openAProgram().entrance_subroutine_title()
        Aerobook_main.maximize()
        # Aerobook_main.print_control_identifiers()
        return Aerobook_main



    def entrance_subroutine_title(self):
        """
        进入子程序,通过标题链接
        :return:
        """
        time.sleep(0.2)
        hwnd = win32gui.FindWindow(None, self.aero_title)
        main_window = Application().connect(handle=hwnd, timeout=10)
        Aerobook_main = main_window.window(handle=hwnd)
        return Aerobook_main



    def menuOpen(self, testdicts):
        """
        在执行测试用例前，首先通过菜单栏打开被测模块
        链接Aercheck，并点击菜单按钮
        :param testdicts:
        :return:
        """
        # 通过Aerobook标题链接Aerobook进程，并切换到Aerobook窗口
        aero_window = pywin_openAProgram().entrance_subroutine_title()
        # 切换到菜单栏
        dlg_spec = aero_window.child_window(auto_id="panel_Graph", control_type="System.Windows.Forms.Panel")
        son_window = dlg_spec.child_window(title=self.aero_module_title, class_name="wxWindowNR")
        MenuOptions = testdicts["所在模块"]  # 取出菜单栏操作路径
        son_window.menu_select(MenuOptions) # 点击菜单选项
        print("\033[0;32;34m通过菜单栏正常打开被测模块\033[0m")
        print(" ")
        return aero_window,son_window






    def menuOpen_switchingWin_UIA(self, testdicts,operationWindow):
        """
        在执行测试用例前，首先通过菜单栏打开被测模块
        然后通过uiautomation框架中的方法切换窗口，针对工作栏
        :return:
        """
        aero_window, son_window=pywin_openAProgram(self.module).menuOpen(testdicts)
        specialWay_OperatingControls(operationWindow).uia_OperatingControls()  # 使用uiautomation框架点击切换模块
        return aero_window, son_window





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
        hwnd = win32gui.FindWindow(None, self.aero_title)
        # 连接Aerobook控制台窗口进程
        Use = uiautomation.WindowControl(searchDepth=1, handle=hwnd)
        # 点击子应用，进入子应用
        Use.Control(searchDepth=4, Name=childApp_Title).Click()
        return Use





class execute_useCase_initialize:
    """执行用例之前初始化"""



    def __init__(self, module=None):
        # 从配置文件中获取应用程序地址
        self.module=module
        self.dict = {}
        self.aero_title = ProfileDataProcessing("commonality", "AerobookEdition").config_File()  # 从配置文件获取Aerobook窗口标题
        if  module =="Aerobook-Aerocheck":
            self.aero_module_title = ProfileDataProcessing("commonality", "AerocheckEdition").config_File()  # 从配置文件获取Aerocheck窗口标题
        elif module =="Aerobook-Fiberbook":
            self.aero_module_title = ProfileDataProcessing("commonality", "FiberbookEdition").config_File()  # 从配置文件获取Aerocheck窗口标题
        elif module == "Aerobook-Fembook":
            self.aero_module_title = ProfileDataProcessing("commonality", "FembookEdition").config_File()  # 从配置文件获取Aerocheck窗口标题
        else:
            self.aero_module_title =None


    def  link_window(self):
        """
        链接被测程序
        :return:
        """
        # 通过Aerobook标题链接Aerobook进行，并切换到Aerobook窗口
        aero_window = pywin_openAProgram().entrance_subroutine_title()
        # 从Aerobook切换到子应用
        dlg_spec1 = aero_window.child_window(auto_id="panel_Graph", control_type="System.Windows.Forms.Panel")
        son_window = dlg_spec1.child_window(title=self.aero_module_title, class_name="wxWindowNR")
        return son_window



    def clear_editWorkingCondition(self,moduleName):
        """
        编辑工况测试前清除所有的包络工况
        :return:

        """
        from tool import  Check_winControl
        from OperatingControls.enterModule import BeingMeasured_popupWin
        Check_winControl("编辑工况", "关闭").popUp_Whether_close()
        self.dict["所在模块"]="载荷信息->编辑工况"
        pywin_openAProgram(moduleName).menuOpen(self.dict)
        # 切换到编辑工况弹窗
        module_window = BeingMeasured_popupWin("编辑工况").menu_LetsGoTopopover()
        while True:
            txt = module_window.ComboBox.window_text()
            if txt:
                module_window.编辑工况Button.click_input()
            else:
                break
        Check_winControl("编辑工况", "关闭").popUp_Whether_close()


    def clear_AllowableCurve(self):
        """
        清除所有的许用值曲线
        :return:
        """
        from OperatingControls.enterModule import specialWay_OperatingControls,ctrW_AeroAerochcek
        from config.relative_location import path
        from PIL import Image
        from PIL import ImageChops
        relativeAddress = path.location()  # 获取相对位置
        operationWindow="编辑材料许用值"
        self.dict["所在模块"]="材料信息->定义复合材料参数"
        module = "Aerobook-Aerocheck"
        aero_window, son_window = pywin_openAProgram(module).menuOpen(self.dict)
        specialWay_OperatingControls(operationWindow).uia_OperatingControls()
        module_window= ctrW_AeroAerochcek(son_window).workField_composite_information()
        dlg_spec=module_window.child_window(title="GridWindow", class_name="wxWindowNR")
        # 进行图片对比，来判断材料许用值曲线表是否为空
        # 预期截图位置location_expect
        location_expect = relativeAddress + r"src\testCase\d_useCase_screenshot\Aerocheck\expectScreenshots\aaa.png"
        # 实际截图位置
        location_actual=relativeAddress+r"src\testCase\d_useCase_screenshot\Aerocheck\ActualScreenshots\\"+"实际材料许用值曲线表截图.png"
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





















