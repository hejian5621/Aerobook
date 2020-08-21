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



    def SelectFile_Popover(self,PopupWindowTitle,location,pitchOn_button,operation=None,filename=None,
                           examine="不检查",windowTitle=None):
        """
        在保存和选择文件路径弹窗中操作
        :param PopupWindowTitle: 选择文件弹窗标题
        :param location: 地址
        :param examine: 需不要检查另外的弹窗
        :param pitchOn_button: 点击选中、打开或者保存按钮等
        :param windowTitle: 弹窗标题
        :param operation: 操作方式
        :param filename: 文件名称
        :return:
        """
        dlg_spec7=None
        app = Application().connect(title=PopupWindowTitle)
        dlg_spec = app.window(title=PopupWindowTitle)           # 切换到选择文件弹窗窗口
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
        if operation=="选择文件":  # 在文件夹或者文件名文本框输入文件名称
            dlg_spec.Edit.set_text(filename)
        # 在选择文件弹窗中点击打开、选择文件夹或者保存按钮
        if pitchOn_button=="打开":
            dlg_spec7=dlg_spec.打开
        elif pitchOn_button=="选择文件夹":
            dlg_spec7=dlg_spec.选择文件夹
        elif pitchOn_button == "保存":
            dlg_spec7=dlg_spec.保存
        else:
            print("在选择文件弹窗中没有打开、保存、或者选择文件夹按钮")
        # 点击打开、保存或者选择文件夹按钮，并确保窗口关闭
        if examine=="检查":
            app1 = Application().connect(title=windowTitle)
            dlg_spec8 = app1.window(title=windowTitle)
            dlg_spec9 = dlg_spec8.是
            instrument().window_WhetherClose(dlg_spec7,dlg_spec,"%s没有关闭"%PopupWindowTitle,dlg_spec9,dlg_spec8,examine)
        else:
            instrument().window_WhetherClose(dlg_spec7, dlg_spec, "%s没有关闭" % PopupWindowTitle)



    def childApp_newProject(self, entity, MenuOptions, source):
        """
        在子应用中新建项目
        :return:
        """
        dlg_app = entity.child_window(title=self.windowTitle, class_name="wxWindowNR"). \
            wait("exists", timeout=60, retry_interval=0.5)
        dlg_app.menu_select(MenuOptions)  # 点击菜单选项
        # 选择项目的保存路径
        ControlOperationSuite(None).SelectFile_Popover("新建项目: 指定项目保存路径", source, "保存", "选择文件", "test_01")
        # 项目设置，增加有限元模型路径
        dlg2_app = Application().connect(title="项目设置")  # 连接项目设置弹窗
        dlg2_app1 = dlg2_app.window(title="项目设置")
        dlg2_app.window(title="项目设置").Maximize()  # 项目弹窗最大化
        mouse.click(button='left', coords=(198, 152))  # 点击有限元模型路径对应的文本框，显示出文本框
        DetailedPath = source + "\Htail.fem"
        dlg2_app1.Edit.wait("exists", timeout=60, retry_interval=1).set_text(DetailedPath)  # 在有限元模型路径对应的文本框中输入数据
        dlg2_app1.完成.click()  # 点击完成按钮



    def ShowSkinSeparately(self):
        """
        独立显示蒙皮
        :return:
        """
        # app = Application().connect(title=r'Aerobook v1.0.4')
        # py_app = app.window(title=r'Aerobook v1.0.4')
        n=1
        v=2
        time.sleep(3)
        py_Tree = self.windowTitle.TreeView  # 切换到树结构
        py_Tree.select(
            "\\模型\部件(1)\HTail_W28(1)\STRUCTURE MODEL(1)\STRUCTURE NATURALMESH(3)\Skin(2)\SkinBottom(1)") # 切换树结构
        mouse.right_click(coords=(182, 285))  # 鼠标移动到SkinBottom中，并点击鼠标右键
        # 选择右键下拉框的“独立显示”
        k = PyKeyboard()
        while n<=v :
            k.press_key(k.down_key)
            time.sleep(0.5)
            n=n+1
        k.press_key(k.enter_key)
