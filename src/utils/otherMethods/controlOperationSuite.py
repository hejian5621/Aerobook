# 控件操作套件
import time
from pywinauto.application import Application
from pywinauto.keyboard import send_keys
from tool import instrument,Check_winControl
from pywinauto import mouse
from pykeyboard import PyKeyboard
from pywinauto  import  findwindows
from OperatingControls.enterModule import BeingMeasured_popupWin


class  ControlOperationSuite:
    """控件操作套件"""



    def __init__(self, windowTitle):
        # 窗口标题
        self.windowTitle = windowTitle
        self.dlg_spec=None




    def SelectFile_Popover(self,parWin_Dicti,examine="不检查",nestWin_Dicti=None):
        """
        在保存和选择文件路径弹窗中操作
        :param parWin_Dicti: 选择文件弹窗的属性参数;
        parWin_Dicti={"窗口标题":"","关闭窗口控件名称":"","关闭窗口控件操作方法":"","地址":"","文件夹输入状态":"","文件夹输入内容":""}
        :param examine: 需不要检查嵌套的窗口
        :param nestWin_Dicti: 嵌套弹窗标题
        :return:
        """
        PopWinTitle  =     parWin_Dicti["窗口标题"]
        control_Name =     parWin_Dicti["关闭窗口控件名称"]
        location     =     parWin_Dicti["地址"]
        filename_content=  parWin_Dicti["文件夹输入内容"]
        try :
            app = Application().connect(title=PopWinTitle,timeout=20)
            self.dlg_spec = app.window(title=PopWinTitle)  # 切换到选择文件弹窗窗口
        except findwindows.ElementNotFoundError:
            import sys, os
            print("没有找到“%r“窗口"%PopWinTitle, __file__, sys._getframe().f_lineno)
            os._exit(0)
        else:
            # 切换控件
            dlg_spec1 = self.dlg_spec.child_window(class_name="WorkerW")
            dlg_spec2 = dlg_spec1.child_window(class_name="ReBarWindow32")
            dlg_spec3 = dlg_spec2.child_window(class_name="Address Band Root")
            dlg_spec4 = dlg_spec3.child_window(class_name="msctls_progress32")  # 切换到选择文件弹窗中的地址栏
            dlg_spec5 = dlg_spec4.child_window(class_name="Breadcrumb Parent")
            dlg_spec6 = dlg_spec5.Toolbar
            dlg_spec6.click()    # 点击地址栏，让地址栏输入框显示出来
            dlg_spec4.Edit.set_text(location)     # 在地址栏输入地址
            send_keys('{ENTER}')   # 点击回车键
            self.dlg_spec["Edit"].set_text(filename_content)   # 在文件名中输入内容
            if examine=="检查":
                nest_PopWinTitle=nestWin_Dicti["嵌套窗口标题"]
                nest_control_Name = nestWin_Dicti["嵌套控件名称"]
                Check_winControl(PopWinTitle, control_Name).nest_popUpWindows(nest_PopWinTitle,nest_control_Name) # 检查嵌套弹窗是否关闭
            else:
                Check_winControl(PopWinTitle, control_Name).popUp_Whether_close()


    """在子应用中新建项目"""
    def childApp_newProject(self, entity, MenuOptions, source):
        """
        在子应用中新建项目
        :return:
        """
        from config.configurationFile import ProfileDataProcessing
        dlg_app = entity.child_window(title=self.windowTitle, class_name="wxWindowNR"). \
            wait("exists", timeout=60, retry_interval=0.5)
        dlg_app.menu_select(MenuOptions)  # 点击菜单选项
        Check_winControl("提示", "是").popUp_Whether_close()
        # 选择项目的保存路径
        parWin_Dicti = {"窗口标题": "新建项目: 指定项目保存路径", "关闭窗口控件名称": "保存","地址": source,  "文件夹输入内容": "test_01"}
        nestWin_Dicti = {"嵌套窗口标题": "确认另存为", "嵌套控件名称": "是"}
        ControlOperationSuite(None).SelectFile_Popover(parWin_Dicti,"检查",nestWin_Dicti )
        # 项目设置，增加有限元模型路径
        try:
            app = Application().connect(title="项目设置",timeout=20)  # 连接项目设置弹窗
            self.dlg_spec = app.window(title="项目设置")
            app.window(title="项目设置").maximize()  # 项目弹窗最大化
        except findwindows.ElementNotFoundError:
            import sys, os
            print("没有找到“%r“窗口" % PopWinTitle, __file__, sys._getframe().f_lineno)
            os._exit(0)
        else:
            x = int(ProfileDataProcessing("commonality", "coord1_x").config_File()) # 从配置文件获取鼠标点击坐标
            y = int(ProfileDataProcessing("commonality", "coord1_y").config_File())  # 从配置文件获取鼠标点击坐标
            mouse.click(button='left', coords= (x, y) )  # 点击有限元模型路径对应的文本框，显示出文本框
            DetailedPath = source + "\Htail.fem"
            self.dlg_spec.Edit.wait("exists", timeout=60, retry_interval=1).set_text(DetailedPath)  # 在有限元模型路径对应的文本框中输入数据
            Check_winControl("项目设置", "完成").nest_popUpWindows("警告", "OK")  # 检查嵌套弹窗是否关闭



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
    def select_AllowableCurve(self,list_argument):
        """
        材料信息--定义复合材料参数--拉伸、压缩、剪切对应的增加按钮
        选择材料许用值曲线
        :return:
        """
        list_AfterParsing = list_argument.split("；")
        print("list_AfterParsing:",list_AfterParsing)
        coord_X = int(list_AfterParsing[0])
        coord_Y = int(list_AfterParsing[1])
        # 连接“选择材料许用值曲线”弹窗
        app_window = BeingMeasured_popupWin("选择材料许用值曲线").menu_LetsGoTopopover()
        dlg_spec=app_window.child_window(title="GridWindow", class_name="wxWindowNR")
        # 勾选数据
        dlg_spec.double_click_input(coords=(coord_X, coord_Y), button="left")
        # 数据勾选完毕点击“确认”按钮
        app_window.确认.click()
        # 检查“选择材料许用值曲线”窗口是否关闭
        Check_winControl("选择材料许用值曲线", "确认").popUp_Whether_close()


    """在工作栏中选择工况"""
    def select_workingCondition(self):
        """
        在工作栏中选择工况
        :return:
        """
        app = Application().connect(title="选择校核工况",timeout=20)  # 连接校核工况弹窗
        dlg_spec = app.window(title="选择校核工况")
        # dlg_spec.print_control_identifiers()
        txt=dlg_spec.ComboBox.window_text()  # 检查是否已经有工况组合
        if txt:  # 如果txt不为空，说明有工况组合数据
            dlg1_spec=dlg_spec.RadioButton2
            Check_winControl(None,dlg1_spec).Verify_CheckBox_Status()  # 点击工况组合选中工况组合
            Check_winControl("选择校核工况","确认").popUp_Whether_close()
        else:  # 如果txt为空，说明没有工况组合数据，就增加数据
            dlg1_spec = dlg_spec.RadioButton3
            Check_winControl(None,dlg1_spec).Verify_CheckBox_Status()  # 点击工况组合选中工况组合
            dlg2_spec = dlg_spec.Edit2
            Check_winControl(None, dlg2_spec).Verify_inputBox("all")
            dlg3_spec = dlg_spec.新建工况组合Button
            Check_winControl(None, dlg3_spec).Verify_CheckBox_Status()  # 点击工况组合选中工况组合
            Check_winControl("选择校核工况", "确认").popUp_Whether_close()


