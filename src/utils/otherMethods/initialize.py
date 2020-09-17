# 初始化

from pywinauto.application import Application
import uiautomation
from config.configurationFile import ProfileDataProcessing
from src.utils.commonality.ExcelFile import read_excel
import time,os
from OperatingControls.enterModule import specialWay_OperatingControls




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
        操作Aerobook控制台
        :return:
        """
        main_window = Application().connect(title_re=self.aero_title, timeout=10)
        Aerobook_main = main_window.window(title_re=self.aero_title)
        Aerobook_main.maximize()
        Aerobook_main.print_control_identifiers()
        return Aerobook_main



    def entrance_subroutine_title(self):
        """
        进入子程序,通过标题链接
        :return:
        """
        main_window = Application().connect(title_re="Aerobook v1.0.4", timeout=10)
        Aerobook_main = main_window.window(title_re=self.aero_title)
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
        son_window = dlg_spec.child_window(title=self.aerocheck_title, class_name="wxWindowNR")
        MenuOptions = testdicts["所在模块"]  # 取出菜单栏操作路径
        son_window.menu_select(MenuOptions) # 点击菜单选项
        print("通过菜单栏正常打开被测模块")
        print(" ")
        return aero_window,son_window


    def menuOpen_switchingWin_UIA(self, testdicts,operationWindow):
        """
        在执行测试用例前，首先通过菜单栏打开被测模块
        然后通过uiautomation框架中的方法切换窗口，针对工作栏
        :return:
        """
        aero_window, son_window=pywin_openAProgram().menuOpen(testdicts)
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
        # 连接Aerobook控制台窗口进程
        Use = uiautomation.WindowControl(searchDepth=1, Name=self.aero_title )
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
        son_window = dlg_spec1.child_window(title=self.aerocheck_title, class_name="wxWindowNR")
        return son_window



    def clear_editWorkingCondition(self):
        """
        编辑工况测试前清除所有的包络工况
        :return:

        """
        from tool import folderFile_dispose, Check_winControl
        from OperatingControls.enterModule import BeingMeasured_popupWin
        Check_winControl("编辑工况", "关闭").popUp_Whether_close()
        self.dict["所在模块"]="载荷信息->编辑工况"
        pywin_openAProgram().menuOpen(self.dict)
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
        from OperatingControls.enterModule import specialWay_OperatingControls,BeingMeasured_work
        from config.relative_location import path
        from PIL import Image
        from PIL import ImageChops
        relativeAddress = path.location()  # 获取相对位置
        operationWindow="编辑材料许用值"
        self.dict["所在模块"]="材料信息->定义复合材料参数"
        aero_window, son_window = pywin_openAProgram().menuOpen(self.dict)
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



    def LaminatedataPopup(self):
        """
        尺寸信息--铺层数据库制作工具
        在测试尺寸信息模块时需要进行铺层数据库的制作
        :return:
        """
        from src.testCase.b_testCaseStep.Aerocheck.TestCaseStep import UseCase_step
        # 从Excel中获取测试用例
        ProjectPath = ProfileDataProcessing("commonality", "ProjectSave_path").config_File()  # 获取配置文件中项目的路径
        testCase_attribute= {
            '选择铺层Excel文件文本框': {'控件类型': '文本框', '唯一标识': 'Edit', '唯一标识方法': '方式一', '所操作实例': '窗口一',
                            '操作控件后等待时间': 0.0, '是否有弹窗出现': '否', '弹窗标题': '无', '弹窗中输入文件名': '无', '弹窗类型': '无',
                            '关闭弹窗按钮名称': '无', '是否有嵌套弹窗': '否', '嵌套弹窗标题': '无', '嵌套弹窗类型': '无', '嵌套弹窗关闭按钮名称': '无'},
             '铺层数据保存路径文本框': {'控件类型': '文本框', '唯一标识': 'Edit2', '唯一标识方法': '方式一', '所操作实例': '窗口二',
                             '操作控件后等待时间': 0.0, '是否有弹窗出现': '否', '弹窗标题': '无', '弹窗中输入文件名': '无', '弹窗类型': '无',
                             '关闭弹窗按钮名称': '无', '是否有嵌套弹窗': '否', '嵌套弹窗标题': '无', '嵌套弹窗类型': '无', '嵌套弹窗关闭按钮名称': '无'},
            '选择铺层Excel文件按钮': {'控件类型': '按钮', '唯一标识': 'Button1', '唯一标识方法': '方式一', '所操作实例': '窗口一', '操作控件后等待时间': 0.0,
                              '是否有弹窗出现': '是', '弹窗标题': '选择Excel铺层文件', '弹窗中输入文件名': 'PlyLibDb_352_541.xlsx',
                              '弹窗类型': '路径弹窗', '关闭弹窗按钮名称': '打开', '是否有嵌套弹窗': '否', '嵌套弹窗标题': '无', '嵌套弹窗类型': '无', '嵌套弹窗关闭按钮名称': '无'},
            '铺层数据库保存路径按钮': {'控件类型': '按钮', '唯一标识': 'Button2', '唯一标识方法': '方式一', '所操作实例': '窗口二', '操作控件后等待时间': 0.0,
                            '是否有弹窗出现': '是', '弹窗标题': '选择铺层数据库保存路径', '弹窗中输入文件名': 'plylib.db', '弹窗类型': '路径弹窗', '关闭弹窗按钮名称': '保存',
                            '是否有嵌套弹窗': '是', '嵌套弹窗标题': '确认另存为', '嵌套弹窗类型': '警告弹窗', '嵌套弹窗关闭按钮名称': '是'},
            '模板文件按钮': {'控件类型': '按钮', '唯一标识': 'Button3', '唯一标识方法': '方式一', '所操作实例': '窗口三', '操作控件后等待时间': 5.0, '是否有弹窗出现': '否',
                       '弹窗标题': '无', '弹窗中输入文件名': '无', '弹窗类型': '无', '关闭弹窗按钮名称': '无', '是否有嵌套弹窗': '无', '嵌套弹窗标题': '无', '嵌套弹窗类型': '无',
                       '嵌套弹窗关闭按钮名称': '无'},
            '开始制作按钮': {'控件类型': '按钮', '唯一标识': 'Button4', '唯一标识方法': '方式一', '所操作实例': '窗口三', '操作控件后等待时间': 1.0,
                       '是否有弹窗出现': '否', '弹窗标题': '无', '弹窗中输入文件名': '无', '弹窗类型': '无', '关闭弹窗按钮名称': '无', '是否有嵌套弹窗': '无',
                       '嵌套弹窗标题': '无', '嵌套弹窗类型': '无', '嵌套弹窗关闭按钮名称': '无'},
            '关闭按钮': {'控件类型': '按钮', '唯一标识': 'Button5', '唯一标识方法': '方式一', '所操作实例': '窗口三',
                     '操作控件后等待时间': 0.0, '是否有弹窗出现': '否', '弹窗标题': '无', '弹窗中输入文件名': '无', '弹窗类型': '无',
                     '关闭弹窗按钮名称': '无', '是否有嵌套弹窗': '无', '嵌套弹窗标题': '无', '嵌套弹窗类型': '无', '嵌套弹窗关闭按钮名称': '无'}}

        testCase_dict ={'用例编号': 'pck001', '测试点': '铺层数据库制作', '所在模块': '铺层信息->铺层数据库制作工具',
                        '选择铺层Excel文件文本框': r'\PlyLibDb_352_541.xlsx', '铺层数据保存路径文本框': r'\plylib.db',
                        '选择铺层Excel文件按钮': '默认', '铺层数据库保存路径按钮': '默认', '模板文件按钮': '默认',
                        '开始制作按钮': '点击', '关闭按钮': '默认', '预期结果文本信息': '铺层数据库制作已完成!', '用例状态': '执行',
                        '预期值信息类型': '信息窗口', '操作窗口标题': '铺层数据库制作工具', '操作子窗口标题': '铺层数据库制作工具',
                        '初始化级别': '整个被测模块', '测试结果等待时间': 3.0, '其他': '拼接路径', '用例集名称': '铺层信息--铺层数据库制作工具弹窗',
                        '被测程序文件地址': r'F:\Aerobook\src\testCase\projectFile\automateFile'}


        actual_result = UseCase_step(testCase_attribute, testCase_dict). \
            Perform_useCase_Steps()  # 铺层信息--铺层库优化工作栏测试用例




    def sizeInformation(self):
        """
        尺寸信息--一维单元尺寸定义（模板）、二维单元尺寸定义（模板）
        在测试尺寸信息模块时需要进行铺层数据库的制作
        :return:
        """
        from src.testCase.b_testCaseStep.Aerocheck.TestCaseStep import sizeInfo_1D2DXlsTemplate_execute
        # 从Excel中获取测试用例
        ProjectPath = ProfileDataProcessing("commonality", "ProjectSave_path").config_File()   # 获取配置文件中项目的路径
        site = {"详细地址": r"src\testCase\c_useCase_file\Aerocheck\initialize\自动化测试用例初始化.xlsx",
                  "表单名称": "自动化一维二维单元尺寸定义（模板）", "初始行": 1,"初始列":1}
        list_dicts = read_excel(site).readExcel_testCase()  # 读取测试用例
        # 从Excel中获取控件操作属性
        site1 = {"详细地址": r"src\testCase\c_useCase_file\Aerocheck\initialize\控件属性已经操作方法初始化.xlsx",
                "表单名称": "自动化一维二维单元尺寸定义（模板）", "初始行": 1, "初始列": 1}
        list_dicts1 = read_excel(site1).readExcel_ControlProperties()  # 读取测试用例
        for  dicts in list_dicts:
            dicts["被测程序文件地址"] = ProjectPath
            actual_result = UseCase_step(testCase_attribute, testCase_dict). \
                Perform_useCase_Steps()  # 铺层信息--铺层库优化工作栏测试用例
            print("actual_Text:",actual_result)

















