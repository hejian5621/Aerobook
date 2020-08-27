# 控件操作套件
import time
from pywinauto.application import Application
from pywinauto.keyboard import send_keys
from src.utils.commonality.tool import instrument
from pywinauto import mouse
from pykeyboard import PyKeyboard



class  ControlOperationSuite:
    """控件操作套件"""



    def __init__(self, windowTitle):
        # 窗口标题
        self.windowTitle = windowTitle


    def menuBar_operation(self,Aero_window,MenuOptions,Aerocheck_title):
        """
        菜单栏操作
        :param Aero_window: Aerobook窗口实体
        :param MenuOptions: 菜单栏操作路径
        :param Aerocheck_title: Aerocheck的标题
        :return: Aerocheck子窗口实体
        """
        # 从Aerobook切换到子应用
        dlg_spec1 = Aero_window.child_window(auto_id="panel_Graph", control_type="System.Windows.Forms.Panel")
        dlg_spec2 = dlg_spec1.child_window(title=Aerocheck_title, class_name="wxWindowNR")
        # 点击菜单选项
        dlg_spec2.menu_select(MenuOptions)
        return dlg_spec2




    def SelectFile_Popover(self,parWin_Dicti,examine="不检查",nestWin_Dicti=None):
        """
        在保存和选择文件路径弹窗中操作
        :param parWin_Dicti: 选择文件弹窗的属性参数;
        parWin_Dicti={"窗口标题":"","关闭窗口控件名称":"","关闭窗口控件操作方法":"","地址":"","文件夹输入状态":"","文件夹输入内容":""}
        :param examine: 需不要检查嵌套的窗口
        :param nestWin_Dicti: 嵌套弹窗标题
        :return:
        """
        # 需要传入的弹窗标题，弹窗中的控件名称，该控件的操作方法
        # 一级弹窗
        # parWin_Dicti={"窗口标题":"","关闭窗口控件名称":"","关闭窗口控件操作方法":"","地址":"","文件夹输入状态":"","文件夹输入内容":""}
        PopWinTitle =     parWin_Dicti["窗口标题"]
        location=         parWin_Dicti["地址"]
        filename_content= parWin_Dicti["文件夹输入内容"]
        dlg_spec7=None
        app=None
        try :
            app = Application().connect(title=PopWinTitle)
        except Warning:
            pass
        dlg_spec = app.window(title=PopWinTitle)           # 切换到选择文件弹窗窗口
        # dlg_spec.print_control_identifiers()
        # 切换控件
        dlg_spec1 = dlg_spec.child_window(class_name="WorkerW")
        dlg_spec2 = dlg_spec1.child_window(class_name="ReBarWindow32")
        dlg_spec3 = dlg_spec2.child_window(class_name="Address Band Root")
        dlg_spec4 = dlg_spec3.child_window(class_name="msctls_progress32")  # 切换到选择文件弹窗中的地址栏
        dlg_spec5 = dlg_spec4.child_window(class_name="Breadcrumb Parent")
        dlg_spec6 = dlg_spec5.Toolbar
        dlg_spec6.click()    # 点击地址栏，让地址栏输入框显示出来
        # 在地址栏输入地址
        time.sleep(0.1)
        dlg_spec4.Edit.set_text(location)
        # 点击回车键
        send_keys('{ENTER}')
        dlg_spec["Edit"].set_text(filename_content)
        if examine=="检查":
            instrument().popUp_Whether_close(parWin_Dicti,examine,nestWin_Dicti)  # 检查有没有提示窗口，如果有就点击是按钮
        else:
            instrument().popUp_Whether_close(parWin_Dicti,examine)  # 检查有没有提示窗口，如果有就点击是按钮



    def childApp_newProject(self, entity, MenuOptions, source):
        """
        在子应用中新建项目
        :return:
        """
        dlg_app = entity.child_window(title=self.windowTitle, class_name="wxWindowNR"). \
            wait("exists", timeout=60, retry_interval=0.5)
        # dlg_app = entity.child_window(title=self.windowTitle, class_name="wxWindowNR")
        # dlg_app.print_control_identifiers()
        dlg_app.menu_select(MenuOptions)  # 点击菜单选项
        nestWin_Dicti = {"窗口标题": "提示", "关闭窗口控件名称": "是", "关闭窗口控件操作方法": "click"}
        instrument().popUp_Whether_close(nestWin_Dicti) # 检查有没有提示窗口，如果有就点击是按钮
        # 选择项目的保存路径
        parWin_Dicti = {"窗口标题": "新建项目: 指定项目保存路径", "关闭窗口控件名称": "保存", "关闭窗口控件操作方法": "click",
                        "地址": source,  "文件夹输入内容": "test_01"}
        nestWin_Dicti = {"嵌套窗口标题": "确认另存为", "嵌套控件名称": "是", "嵌套控件操作方法": "click"}
        ControlOperationSuite(None).SelectFile_Popover(parWin_Dicti,"检查",nestWin_Dicti )
        # 项目设置，增加有限元模型路径
        dlg2_app =None
        try:
            dlg2_app = Application().connect(title="项目设置")  # 连接项目设置弹窗
        except Warning:
            pass
        dlg2_app1 = dlg2_app.window(title="项目设置")
        dlg2_app.window(title="项目设置").maximize()  # 项目弹窗最大化
        mouse.click(button='left', coords=(198, 152))  # 点击有限元模型路径对应的文本框，显示出文本框
        mouse.click(button='left', coords=(2753, 147))  # 点击有限元模型路径对应的文本框，显示出文本框
        DetailedPath = source + "\Htail.fem"
        dlg2_app1.Edit.wait("exists", timeout=60, retry_interval=1).set_text(DetailedPath)  # 在有限元模型路径对应的文本框中输入数据
        itemSetting_Dicti = {"窗口标题": "项目设置", "关闭窗口控件名称": "完成", "关闭窗口控件操作方法": "click"}
        nest_warn_Dicti = {"嵌套窗口标题": "警告", "嵌套控件名称": "OK", "嵌套控件操作方法": "click"}
        instrument().popUp_Whether_close(itemSetting_Dicti,"检查",nest_warn_Dicti)  # 检查有没有提示窗口，如果有就点击是按钮




    def ShowSkinSeparately(self):
        """
        独立显示蒙皮
        :return:
        """
        # app = Application().connect(title=r'Aerobook v1.0.4')
        # py_app = app.window(title=r'Aerobook v1.0.4')
        n=1
        v=3
        time.sleep(3)
        py_Tree = self.windowTitle.TreeView  # 切换到树结构
        py_Tree.select(
            "\\模型\部件(1)\HTail_W28(1)\STRUCTURE MODEL(1)\STRUCTURE NATURALMESH(3)\Skin(2)\SkinBottom(1)") # 切换树结构
        mouse.right_click(coords=(182, 285))  # 鼠标移动到SkinBottom中，并点击鼠标右键
        # mouse.right_click(coords=(2729, 287))
        # 选择右键下拉框的“独立显示”
        k = PyKeyboard()
        while n<=v :
            k.press_key(k.down_key)
            time.sleep(0.5)
            n=n+1
        k.press_key(k.enter_key)
