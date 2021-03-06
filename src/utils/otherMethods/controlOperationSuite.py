# 控件操作套件
import time
from pywinauto.application import Application
from pywinauto.keyboard import send_keys
from tool import instrument,Check_winControl
from pywinauto import mouse
from pykeyboard import PyKeyboard
from pywinauto  import  findwindows
from OperatingControls.enterModule import BeingMeasured_popupWin
from tool import MyException
import  win32gui,sys


"""Aercheck控件操作套件"""
class  ControlOperationSuite_Aercheck:
    """Aercheck控件操作套件"""



    def __init__(self, windowTitle):
        # 窗口标题
        self.windowTitle = windowTitle
        self.dlg_spec=None




    def SelectFile_Popover(self,list_Popup_parameter,location,Popup_type,Popup_parameter=None,window_one=None):
        """
        在保存和选择文件路径弹窗中操作
        :param list_Popup_parameter:弹窗参数信息
        :param location: 路径
        :param window_one: 关闭弹窗按钮名称
        :param Popup_type: 弹窗类型
        :param Popup_parameter: 在文件名文本框输入的内容
        :return:
        """
        hwnd=0
        Popup_Title = list_Popup_parameter[0]  # 取出弹窗标题
        file_name = list_Popup_parameter[1]  # 取出输入的文件名
        close_Name = list_Popup_parameter[2]  # 取出关闭弹窗的按钮名称
        if window_one:
            Check_winControl(Popup_Title, window_one).window_WhetherOpen()  # 保证弹窗出现
        try :
            n=0
            i=10
            while n<=i:
                time.sleep(0.2)
                hwnd = win32gui.FindWindow(None, Popup_Title)
                if hwnd !=0:
                    break
                n+=1
            if hwnd == 0:  # 如果句柄不为零证明找到了该弹窗
                raise MyException("没有找到弹窗")
        except Exception:
            print("没有找到“%r“窗口，获取的句柄为：%r"%(Popup_Title,hwnd), __file__, sys._getframe().f_lineno)
            raise MyException("没有找到“%r“窗口"%Popup_Title)
        else:
            app = Application().connect(handle=hwnd, timeout=20)
            self.dlg_spec = app.window(handle=hwnd)  # 切换到选择文件弹窗窗口
            # self.dlg_spec.print_control_identifiers()
            # 切换控件
            dlg_spec1 = self.dlg_spec.child_window(class_name="WorkerW")
            dlg_spec2 = dlg_spec1.child_window(class_name="ReBarWindow32")
            dlg_spec3 = dlg_spec2.child_window(class_name="Address Band Root")
            dlg_spec4 = dlg_spec3.child_window(class_name="msctls_progress32")  # 切换到选择文件弹窗中的地址栏
            dlg_spec5 = dlg_spec4.child_window(class_name="Breadcrumb Parent")
            dlg_spec6 = dlg_spec5.Toolbar
            dlg_spec6.click_input(coords = (10, 10))   # 点击地址栏，让地址栏输入框显示出来
            dlg_spec4.Edit.set_text(location)     # 在地址栏输入地址
            send_keys('{ENTER}')   # 点击回车键
            self.dlg_spec["Edit"].set_text(file_name)   # 在文件名中输入内容
            if Popup_type=="" or Popup_type=="无":
                Check_winControl(Popup_Title, close_Name).popUp_Whether_close() # 检查点击按钮后窗口是否关闭，如果没有关闭，继续点击按钮
            else:
                list_AfterParsing = Popup_parameter.split("；")
                nest_PopWinTitle=list_AfterParsing[0]
                nest_control_Name = list_AfterParsing[1]
                Check_winControl(Popup_Title, close_Name).nest_popUpWindows(nest_PopWinTitle,nest_control_Name)  # 检查嵌套弹窗是否关闭


    """在子应用中新建项目"""
    def childApp_newProject(self, entity, MenuOptions, source):
        """
        在子应用中新建项目
        :return:
        """
        from config.configurationFile import ProfileDataProcessing
        dlg_app = entity.child_window(title=self.windowTitle, class_name="wxWindowNR").wait("exists", timeout=60, retry_interval=0.2)
        dlg_app.menu_select(MenuOptions)  # 点击菜单选项
        Check_winControl("提示", "是").popUp_Whether_close()
        # 选择项目的保存路径
        Popup_type2="无"
        list_AfterParsing = ["新建项目: 指定项目保存路径", "test_1", "保存"]
        ControlOperationSuite_Aercheck(None).SelectFile_Popover(list_AfterParsing, source,Popup_type2)
        # 项目设置，增加有限元模型路径
        try:
            app = Application().connect(title="项目设置",timeout=5)  # 连接项目设置弹窗
            self.dlg_spec = app.window(title="项目设置")
            # app.window(title="项目设置").maximize()  # 项目弹窗最大化
        except findwindows.ElementNotFoundError:
            raise MyException("没有找到“项目设置“窗口")
        else:
            x = int(ProfileDataProcessing("commonality-Aerobook-Aerocheck", "coord1_x").config_File()) # 从配置文件获取鼠标点击坐标
            y = int(ProfileDataProcessing("commonality-Aerobook-Aerocheck", "coord1_y").config_File())  # 从配置文件获取鼠标点击坐标
            self.dlg_spec.click_input(button='left', coords= (x, y) )  # 点击有限元模型路径对应的文本框，显示出文本框
            DetailedPath = source + "\Htail.fem"
            self.dlg_spec.Edit.wait("exists", timeout=60, retry_interval=1).set_text(DetailedPath)  # 在有限元模型路径对应的文本框中输入数据
            self.dlg_spec.wxPropertyGrid.click_input()
            Check_winControl("项目设置", "完成").nest_popUpWindows("警告", "OK",4)  # 检查嵌套弹窗是否关闭


    """PYWIN独立显示蒙皮"""
    def pywin_ShowSkinSeparately(self):
        """
        独立显示蒙皮
        :return:
        """
        from config.configurationFile import ProfileDataProcessing
        n=1
        v=3
        time.sleep(3)
        py_Tree = self.windowTitle.TreeView  # 切换到树结构
        py_Tree.select(
            "\\模型\部件(1)\HTail_W28(1)\STRUCTURE MODEL(1)\STRUCTURE NATURALMESH(3)\Skin(2)\SkinBottom(1)") # 切换树结构
        x = int(ProfileDataProcessing("commonality", "coord2_x").config_File())  # 从配置文件获取鼠标点击坐标
        y = int(ProfileDataProcessing("commonality", "coord2_y").config_File())  # 从配置文件获取鼠标点击坐标
        mouse.right_click(coords=(x, y))  # 鼠标移动到SkinBottom中，并点击鼠标右键
        # 选择右键下拉框的“独立显示”
        k = PyKeyboard()
        while n<=v :
            k.press_key(k.down_key)
            time.sleep(0.5)
            n=n+1
        k.press_key(k.enter_key)


    """UIA独立显示蒙皮"""
    def uia_ShowSkinSeparately(self,aero_title,):
        """
        独立显示蒙皮
        :return:
        """
        import uiautomation
        # 切换模型树结构
        Use1 = None;Use2 = None;Use3 = None;Use4 = None;Use5 = None;Use6 = None;Use7 = None;Use8 = None
        # 连接应用程序，并切换到进入模型树
        Use = uiautomation.WindowControl(searchDepth=1, Name=aero_title)
        Use1 = Use.Control(searchDepth=8, Name="模型")
        try:
            Use2 = Use.Control(searchDepth=9, Name="部件(1)")
            Use2.DoubleClick()
        except  LookupError:
            Use1.DoubleClick()
            Use2 = Use.Control(searchDepth=9, Name="部件(1)")
            Use2.DoubleClick()
        try:
            Use3 = Use.Control(searchDepth=10, Name="HTail_W28(1)")
            Use3.DoubleClick()
        except  LookupError:
            Use2.DoubleClick()
            Use3 = Use.Control(searchDepth=10, Name="HTail_W28(1)")
            Use3.DoubleClick()
        try:
            Use4 = Use.Control(searchDepth=11, Name="STRUCTURE MODEL(1)")
            Use4.DoubleClick()
        except  LookupError:
            Use3.DoubleClick()
            Use4 = Use.Control(searchDepth=11, Name="STRUCTURE MODEL(1)")
            Use4.DoubleClick()
        try:
            Use5 = Use.Control(searchDepth=12, Name="STRUCTURE NATURALMESH(3)")
            Use5.DoubleClick()
        except  LookupError:
            Use4.DoubleClick()
            Use5 = Use.Control(searchDepth=12, Name="STRUCTURE NATURALMESH(3)")
            Use5.DoubleClick()
        try:
            Use6 = Use.Control(searchDepth=13, Name="Skin(2)")
            Use6.DoubleClick()
        except  LookupError:
            Use5.DoubleClick()
            Use6 = Use.Control(searchDepth=13, Name="Skin(2)")
            Use6.DoubleClick()
        try:
            Use7 = Use.Control(searchDepth=14, Name="SkinBottom(1)")
            Use7.RightClick()
        except  LookupError:
            Use6.DoubleClick()
            Use7 = Use.Control(searchDepth=14, Name="SkinBottom(1)")
            Use7.RightClick()
        # 在鼠标右键生产的菜单中选择独立显示
        n = 1;v = 3
        import time
        from pykeyboard import PyKeyboard
        # 选择右键下拉框的“独立显示”
        k = PyKeyboard()
        while n <= v:
            k.press_key(k.down_key)
            time.sleep(0.5)
            n = n + 1
        k.press_key(k.enter_key)


    """材料信息--定义复合材料参数--拉伸、压缩、剪切对应的增加按钮"""
    def select_AllowableCurve(self,str_coord):
        """
        材料信息--定义复合材料参数--拉伸、压缩、剪切对应的增加按钮
        选择材料许用值曲线
        :return:
        """
        list_AfterParsing = str_coord.split("；")
        coord_X = int(list_AfterParsing[0])
        coord_Y = int(list_AfterParsing[1])
        # 连接“选择材料许用值曲线”弹窗
        app_window = BeingMeasured_popupWin("选择材料许用值曲线").menu_LetsGoTopopover()
        dlg_spec=app_window.child_window(title="GridWindow", class_name="wxWindowNR")
        # 勾选数据
        dlg_spec.double_click_input(coords=(coord_X, coord_Y), button="left")
        #钮 数据勾选完毕点击“确认”按
        app_window.确认.click_input()
        # 检查“选择材料许用值曲线”窗口是否关闭
        Check_winControl("选择材料许用值曲线", "确认").popUp_Whether_close()


    """在工作栏中选择工况"""
    def select_workingCondition(self,title_name):
        """
        在工作栏中选择工况
        :return:
        """
        hwnd = win32gui.FindWindow(None, title_name)
        app = Application().connect(handle=hwnd,timeout=20)  # 连接校核工况弹窗
        dlg_spec = app.window(handle=hwnd)
        # dlg_spec.print_control_identifiers()
        txt=dlg_spec.ComboBox.window_text()  # 检查是否已经有工况组合
        if txt:  # 如果txt不为空，说明有工况组合数据
            dlg1_spec=dlg_spec.RadioButton2
            Check_winControl(None,dlg1_spec).Verify_CheckBox_Status()  # 点击工况组合选中工况组合
            Check_winControl(title_name,"确认").popUp_Whether_close()
        else:  # 如果txt为空，说明没有工况组合数据，就增加数据
            dlg1_spec = dlg_spec.RadioButton3
            Check_winControl(None,dlg1_spec).Verify_CheckBox_Status()  # 点击工况组合选中工况组合
            dlg2_spec = dlg_spec.Edit2
            Check_winControl(None, dlg2_spec).Verify_inputBox("all")
            dlg3_spec = dlg_spec.新建工况组合Button
            Check_winControl(None, dlg3_spec).Verify_CheckBox_Status()  # 点击工况组合选中工况组合
            Check_winControl(title_name, "确认").popUp_Whether_close()


    """Aerocheck--尺寸信息--1D尺寸定义--选择铺层库信息"""
    def select_Laminatedata(self,line):
        """
        尺寸信息--1D尺寸定义--选择铺层库信息
        :return:
        """
        try:
            hwnd = win32gui.FindWindow(None, "选择铺层库信息")
            if hwnd ==0:
                raise MyException("没有找到窗口")  # 实例化一个异常,实例化的时候需要传参数
        except Exception:
            print("没有找到“选择铺层库信息“窗口"% __file__, sys._getframe().f_lineno)
        else:
            app = Application().connect(handle=hwnd, timeout=20)
            self.dlg_spec = app.window(handle=hwnd)  # 切换到选择文件弹窗窗口
            dlg_spec=self.dlg_spec.child_window(title="GridWindow", class_name="wxWindowNR")  # 切换到网格窗口
            if line=="第一行":
                dlg_spec.double_click_input(coords=(150, 10), button="left")  # 选择第一行数据
            elif line=="第二行":
                dlg_spec.double_click_input(coords=(150, 30), button="left")  # 选择第一行数据
            elif line=="第三行":
                dlg_spec.double_click_input(coords=(150, 50), button="left")  # 选择第一行数据
            elif line=="第三行":
                dlg_spec.double_click_input(coords=(150, 50), button="left")  # 选择第一行数据
            else:
                dlg_spec.double_click_input(coords=(150, 70), button="left")  # 选择第一行数据
            # self.dlg_spec.print_control_identifiers()
            self.dlg_spec.Button0.click_input()


"""Fiberbook控件操作套件"""
class ControlOperationSuite_Fiberbook:
    """Fiberbook控件操作套件"""


    def __init__(self, windowTitle):
        # 窗口标题
        self.windowTitle = windowTitle
        self.dlg_spec=None


    """设计变量--一维单元设计变量（截面尺寸）--1D截面参数定义"""
    def designVariableSection_definition(self, title):
        """
        设计变量--一维单元设计变量（截面尺寸）--1D截面参数定义
        :return:
        """
        try:
            wnd = win32gui.FindWindow(None,  title)  # 通过弹窗的类名获取弹窗的句柄
            if wnd==0:                                       # 如果句柄是0，就说明没有找到窗口，就抛出异常
                raise MyException("没有找到弹窗“%r”"% title)
        except Exception:
            pass
        else:
            app = Application().connect(handle=wnd)
            self.dlg_spec = app.window(handle=wnd)  # 切换到选择文件弹窗窗口
            self.dlg_spec.Button3.click_input()

    """设计变量--一维单元设计变量（截面尺寸）--铺层比定义"""
    def designVariableSection_LayUp(self):
        """
        设计变量--一维单元设计变量（截面尺寸）--铺层比定义
        :return:
        """
        try:
            wnd = win32gui.FindWindow(None, "铺层比定义")  # 通过弹窗的类名获取弹窗的句柄
            if wnd == 0:  # 如果句柄是0，就说明没有找到窗口，就抛出异常
                raise MyException("没有找到弹窗“1D截面参数定义”")
        except Exception:
            pass
        else:
            app = Application().connect(handle=wnd)
            self.dlg_spec = app.window(handle=wnd)  # 切换到选择文件弹窗窗口
            self.dlg_spec.Button3.click_input()


