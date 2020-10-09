# 工具
from pykeyboard import PyKeyboard
from pywinauto import mouse
from config.configurationFile import ProfileDataProcessing
from aip import AipOcr
import win32clipboard as wc
import os,shutil,win32con,time,os,sys
from pywinauto.application import Application
import re,datetime
from os import listdir
from pathlib import Path
from src.utils.commonality.ExcelFile import read_excel
from src.utils.otherMethods.dataFormatConversion import FormatConversion
from pywinauto import  findwindows






"""工具类"""
class  instrument:
    """工具类"""


    def __init__(self):
        pass


    # 获取剪切板里的数据
    def getCopyText(self):
        """
        获取剪切板里的数据
        :return:
        """
        wc.OpenClipboard()   # 打开剪贴板
        copy_text = wc.GetClipboardData(win32con.CF_TEXT)   # 获取剪切板里的数据
        wc.EmptyClipboard()     # 清楚剪贴板的数据
        wc.CloseClipboard()     # 关闭剪贴板
        text=copy_text.decode('GB2312')    # 转化获取数据的显示格式
        return text


    def infoWindow(self, aero_window):
        """
        通过全选/复制信息窗口里的数据，获取实际值
        :return:
        """
        wc.OpenClipboard()
        wc.EmptyClipboard()
        wc.CloseClipboard()
        dlg_spec = aero_window.richText2  # 切换到信息窗口
        dlg_spec.send_keystrokes("^a")  # 全选信息窗口的文本信息
        dlg_spec.send_keystrokes("^c")  # 复制信息窗口的文本信息到粘贴板


"""键盘鼠标操作"""
class KeyboardMouse:
    """键盘鼠标操作"""



    def __init__(self):
        self.k = PyKeyboard()   # 键盘操作方法实例化


    #在Aerobook--Aerocheck的图形区通过键盘和鼠标的操作方式选中全部的结构单元
    def selectionModel(self):
        """
        在Aerobook--Aerocheck的图形区通过键盘和鼠标的操作方式选中全部的结构单元
        选择结构单元
        """
        self.k.press_key(self.k.shift_key)   # 按下键盘上的shift键
        mouse.press(coords=(345, 167))   # 鼠标长按
        mouse.release(coords=(1488, 727))  # 释放鼠标位置
        self.k.release_key(self.k.shift_key) # 释放键盘上的shift键


"""图片处理"""
class pictureProcessing:
    """图片处理"""


    def __init__(self,path,location=None):
        self.path=path   # 图片的位置
        self.location = location  # 图片的位置
        self.list1=[]


    def get_file_content(self):
        with open(self.path, 'rb') as fp:
            return fp.read()


    #通过百度的API读取图片中的文本信息
    def screenshot(self):
        """
        通过百度的API读取图片中的文本信息
        :return:编译出的文本信息
        """
        # 在配置文件中读取百度API的账号信息
        APP_ID=ProfileDataProcessing("commonality","APP_ID").config_File()
        API_KEY = ProfileDataProcessing("commonality","API_KEY").config_File()
        SECRET_KEY = ProfileDataProcessing("commonality","SECRET_KEY").config_File()
        # 定义参数变量
        options = {'detect_direction': 'true','language_type': 'CHN_ENG',}
        # 初始化AipFace对象
        aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)
        # 调用通用文字识别接口
        result = aipOcr.basicGeneral(pictureProcessing(self.path).get_file_content(), options)
        words_result = result['words_result']
        for i in range(len(words_result)):
            self.list1.append(words_result[i]['words'])
        # 合并列表
        str = ''.join(self.list1)
        return str

    def BeingMeasured_system_screenshot(self):
        """
        被测系统截图
        :return:
        """
        from src.utils.otherMethods.initialize import pywin_openAProgram
        print("\033[0;34m对被测系统进行截图\033[0m", __file__, sys._getframe().f_lineno)
        aero_window = pywin_openAProgram().entrance_subroutine_title()
        location = r"F:\Aerobook\src\testCase\a_useCaseSet\Aerockeck\img\test_1.png"   # 截图的保存位置
        aero_window.capture_as_image().save(location)  # 获取警告弹窗的文本截图
        print("")


    def imageComparison(self,):
        """
        图片对比
        :return:
        """
        from PIL import Image
        from PIL import ImageChops
        image_one = Image.open(self.path)  # 获取图片信息
        image_two = Image.open(self.location)  # 获取图片信息
        diff = ImageChops.difference(image_one, image_two)  # 对比图片
        if diff.getbbox() is None:  # 图片一样
            result="图片一样"
        else:  # 如果不图片一样，就说明材料许用值曲线表里有内容，就删除内容
            result = "图片不一样"
        return result




"""文件、文件夹的复制、新建和删除"""
class folderFile_dispose:
    """文件、文件夹的复制、新建和删除"""


    def __init__(self,sourceDir):
        self.sourceDir=sourceDir  # 文件夹的路径


    # 复制文件夹，包括文件夹里嵌套的文件夹，但是嵌套的文件夹不能为空
    def copyFile(self, targetDir):
        """
        复制文件夹，包括文件夹里嵌套的文件夹，但是嵌套的文件夹不能为空
        :param targetDir: 复制文件夹的存放路径，以及新的名称
        :return:
        """
        copyFileCounts = 0
        for f in os.listdir(self.sourceDir):
            sourceF = os.path.join(self.sourceDir, f)
            targetF = os.path.join(targetDir, f)
            if os.path.isfile(sourceF):
                if not os.path.exists(targetDir):
                    os.makedirs(targetDir)
                copyFileCounts += 1
                if not os.path.exists(targetF) or (
                        os.path.exists(targetF) and (os.path.getsize(targetF) != os.path.getsize(sourceF))):
                    open(targetF, "wb").write(open(sourceF, "rb").read())
            if os.path.isdir(sourceF):
                folderFile_dispose(sourceF).copyFile(targetF)


    # 强制删除文件夹
    def delfolder(self):
        """
        强制删除文件夹
        :return:
        """
        if os.path.isdir(r"F:\Aerobook\\src\testCase\projectFile\automateFile"):
            shutil.rmtree(self.sourceDir )
            print('文件“%s“删除完毕' % self.sourceDir )


    #  批量删除文件
    def delfile(self, dict_testCase):
        """
        批量删除文件
        :param dict_testCase:
        :return:
        """
        print("\033[0;32;34m开始清除执行用例前需要清除的文件\033[0m")
        print("")
        if "清除文件" in dict_testCase:  # 用例执行前，删除相关文件
            filePath_name = dict_testCase["清除文件"]
            if filePath_name =="" or filePath_name =="默认":   # 如果“清除文件”的值等于空或者默认
                pass
            else:                                              # 如果“清除文件”的值不等于空或者默认
                if "；" in filePath_name:
                    list_filePath_name = filePath_name.split("；")
                    # 拼接文件名和路径
                    for path1 in list_filePath_name:  # 取出文件路径
                        list_path = self.sourceDir + "\\" + path1
                        my_file = Path(list_path)
                        if my_file.is_file():  # 先检查文件是否存在
                            # 指定的文件存在，就删除
                            os.remove(list_path)
                else:
                    list_path = self.sourceDir + "\\" + filePath_name
                    my_file = Path(list_path)
                    if my_file.is_file():  # 先检查文件是否存在
                        # 指定的文件存在，就删除
                        os.remove(list_path)


    # 取出文件夹里文件所有的名称
    def FetchFileName(self,InitialTime):
        """
        取出文件夹里文件所有的名称,并且根据实际筛选出符合时间条件的文件名称
        :return:
        """
        list_fileNames=[]
        # 获取实时时间
        now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # 获取文件夹里的所有文件名
        list_fileName=os.listdir(self.sourceDir)
        if list_fileName:
            for fileName in list_fileName:
                site=self.sourceDir+r"\\"+fileName    # 拼接文件路径
                t = os.path.getmtime(site)     #  获取文件的修改时间
                amend_time = datetime.datetime.fromtimestamp(t).strftime("%Y-%m-%d %H:%M:%S")
                if now_time>amend_time>InitialTime:
                    list_fileNames.append(fileName)
        return list_fileNames



"""定义的异常类，用于主动抛出异常"""
class MyException(Exception):
    def __init__(self,name):
        self.name = name


"""检查窗口或者控件，是否存在"""
class  Check_winControl:
    """检查窗口或者控件，是否存在"""


    def __init__(self,title=None, triggerButton=None,cycleIndex=10,CircleInitial=1):
        self.title=title  # 窗口标题
        self.triggerButton = triggerButton  # 控制实体
        self.cycleIndex = cycleIndex    # 循环最终次数
        self.CircleInitial = CircleInitial # 循环初始次数
        self.state=None



    #检查触发摸一个事件（点击按钮），应该出现的弹窗或者控件是否出现
    def window_WhetherOpen(self):
        """
        检查触发摸一个事件（点击按钮），应该出现的弹窗或者控件是否出现
        通过弹窗标题获取句柄
        如果出现，程序正常运行
        如果没有出现，程序停止运行
        :param title: 预期弹出弹窗的标题
        :param event_button: 触发的按钮操作
        :return:
        """
        import win32gui
        self.triggerButton.click_input()   # 点击触发弹窗的按钮
        # 判断弹窗是否弹窗，如果没有弹出，就继续点击
        while self.CircleInitial <= self.cycleIndex:  # 如果没有找到控件，就继续点击触发按钮
            try:
                hwnd = win32gui.FindWindow(None, self.title)  # 通过弹窗的标题获取弹窗的句柄
                if hwnd != 0:                                 # 如果句柄不为零证明找到了该弹窗
                    raise MyException("没有找到弹窗")           # 如果找到了该弹窗，则主动抛出异常
            except Exception:                                 # 捕捉到该异常，证明弹窗已经找到，就退出循环
                break
            else:
                if (self.CircleInitial % 5) == 0:
                    self.triggerButton.click_input()           # 如果没有找到弹窗，再次点击触发出现弹窗的按钮
                elif self.CircleInitial == 1:                  # 如果第一次链接不上，在点击一次
                    self.triggerButton.click_input()
            self.CircleInitial = self.CircleInitial + 1
        if self.CircleInitial == (self.cycleIndex + 1):
            raise MyException("%r窗口没有找到" % self.title)


    """检查触发摸一个事件（点击按钮），应该出现的弹窗或者控件是否出现"""
    def window_handle_WhetherOpen(self,handle,identification):
        """
        检查触发摸一个事件（点击按钮），应该出现的弹窗或者控件是否出现
        因为有些文本框根本就没有标题，只有通过句柄判断弹窗是否存在
        如果出现，程序正常运行
        如果没有出现，程序停止运行
        :param handle: 预期弹出弹窗的标题
        :param identification: 触发的按钮操作
        :return:
        """
        self.triggerButton.click_input()  # 点击触发弹窗的按钮
        # 判断弹窗是否弹窗，如果没有弹出，就继续点击
        while self.CircleInitial <= self.cycleIndex:  # 如果没有找到控件，就继续点击触发按钮
            result = None
            state=Check_winControl(handle).handle_popUp_exist(identification)   # 通过弹窗的类名获取弹窗的句柄
            if state:
                break
            else:
                if (self.CircleInitial % 5) == 0:  # 如果循环次数数10的倍数，就再次点击按钮
                    self.triggerButton.click_input()
                elif self.CircleInitial == 1:  # 如果第一次链接不是，在点击一次
                    self.triggerButton.click_input()
            if self.CircleInitial == (self.cycleIndex + 1):
                raise MyException("%r窗口没有找到" % self.title)
            self.CircleInitial = self.CircleInitial + 1


    """处理带有嵌套弹窗的弹窗"""
    def nest_popUpWindows(self,nest_title,nest_triggerButton):
        """
        处理带有嵌套弹窗的弹窗
        检查点击按钮后窗口是否关闭，如果没有关闭，继续点击按钮
        :return:
        """
        while self.CircleInitial <= self.cycleIndex:
            close_result=Check_winControl(self.title,self.triggerButton,1,1).popUp_Whether_close()   # 然后在检查弹窗有没有关闭
            if close_result=="窗口已正常关闭":
                break
            time.sleep(0.5)
            Check_winControl(nest_title, nest_triggerButton).popUp_Whether_close()  # 检查有没有嵌套弹框,有嵌套弹框就关掉
            self.CircleInitial = self.CircleInitial + 1
            if self.CircleInitial == (self.cycleIndex + 1):
                raise MyException("%r窗口没有关闭" % self.title)


    """检查点击按钮后窗口是否关闭，如果没有关闭，继续点击按钮"""
    def popUp_Whether_close(self):
        """
        检查点击按钮后窗口是否关闭，如果没有关闭，继续点击按钮
        首先通过获取句柄的形式来判断是否有弹窗，因为以句柄的形式会快一点
        :return:
        """
        import win32gui
        while self.CircleInitial <= self.cycleIndex:
            try:
                hwnd = win32gui.FindWindow(None, self.title)  # 通过弹窗的标题获取弹窗的句柄
                if hwnd == 0:
                    raise MyException("没有找到弹窗")  # 实例化一个异常,实例化的时候需要传参数
            except Exception as obj:  # 万能捕获，之前的可能捕获不到，这里添加Exception作为保底
                self.state = "窗口已正常关闭"
                break
            else:
                try:
                    app1=Application().connect(title_re=self.title)
                    py_app1 = app1.window(title_re=self.title)
                except findwindows.ElementAmbiguousError:
                    app2 = Application().connect(handle=hwnd)
                    py_app2 = app2.window(handle=hwnd)  # 切换到需要关闭的窗口
                    if py_app2[self.triggerButton].exists():  # 如果控件存在
                        py_app2[self.triggerButton].click()
                    else:
                        raise MyException("没有找到关闭窗口的按钮:%r"%self.title)
                except findwindows.ElementNotFoundError:
                    break
                else:
                    if py_app1[self.triggerButton].exists():  # 如果控件存在
                        py_app1[self.triggerButton].click_input()
                    else:
                        raise MyException("没有找到关闭窗口的按钮:%r"%self.title)
                self.CircleInitial = self.CircleInitial + 1
        return self.state



    """强行关闭弹窗"""
    def Force_close_popUp(self):
        """
        强行关闭弹窗
        :return:
        """
        import win32gui
        while self.CircleInitial <= self.cycleIndex:
            try:
                hwnd = win32gui.FindWindow(None, self.title)  # 通过弹窗的标题获取弹窗的句柄
                if hwnd == 0:                                 # 通过句柄判断窗口是否存在
                    raise MyException("没有找到弹窗")           # 如果不存在就主动抛出异常
            except Exception as obj:                          # 捕捉到异常
                print("根据弹窗标题获得的句柄判断弹窗已经关闭,窗口标题：%r,窗口句柄：%r"%(self.title,hwnd), __file__, sys._getframe().f_lineno)
                self.state = "窗口已正常关闭"                   # 用于有嵌套弹窗的情况
                break                                          # 退出循环
            else:
                try:                                          # 根据标题在次连接弹窗
                    app1 = Application().connect(title_re=self.title)
                    py_app1 = app1.window(title_re=self.title)
                except findwindows.ElementAmbiguousError:      # 抛出有多个相同标题的异常，就根据句柄一个一个的关闭弹窗
                    app2 = Application().connect(handle=hwnd)
                    py_app2 = app2.window(handle=hwnd)  # 切换到需要关闭的窗口
                    if py_app2.exists():  # 如果控件存在
                        py_app2.close()
                    else:
                        raise MyException("没有找到关闭窗口的按钮:%r"%self.title)
                except findwindows.ElementNotFoundError:
                    print("根据弹窗标题判断弹窗已经关闭：",hwnd, __file__, sys._getframe().f_lineno)
                    break
                else:
                    if py_app1.exists():  # 如果控件存在
                        py_app1.close()   # 强制关掉弹窗
                    else:
                        raise MyException("没有找到关闭窗口的按钮:%r"%self.title)
                self.CircleInitial = self.CircleInitial + 1
        return self.state


    """通过窗口的类名获取句柄，通句柄判断窗口是否存在"""
    def handle_popUp_exist(self,identification):
        """
        通过窗口的类名获取句柄，通句柄判断窗口是否存在
        :return:
        """
        import win32gui
        hwnd=win32gui.FindWindow(self.title,None)   # 通过弹窗的类名获取弹窗的句柄
        app = Application().connect(handle=hwnd,timeout=20)
        dlg_spec = app.window(handle=hwnd)  # 切换到选择文件弹窗窗口
        if dlg_spec[identification].exists():
            retur=True
        else:
            retur=False
        return retur


    """确认勾选框是否勾选，如果没有勾选，就勾选"""
    def Verify_CheckBox_Status(self):
        """
        确认勾选框是否勾选，如果没有勾选，就勾选
        :return:
        """
        self.triggerButton.click_input()  # 勾选勾选框
        while self.CircleInitial<self.cycleIndex:
            State=self.triggerButton.get_check_state()   # 返回勾选框的勾选状态
            if State==0:  # 0 表示没有勾选上
                self.triggerButton.click_input()
            else:
                break
            self.CircleInitial = self.CircleInitial + 1


    def Verify_inputBox(self,data):
        """
        验证输入框是否输入正确的数据，如果还没有输入就再次输入，一直到输入成功为止
        :return:
        """
        if type(data) == float:  # 如果需要输入的参数的数据类型为浮点
            data = '{:g}'.format(data)   # 去掉浮点数最后的零
        print("向文本框内的输入的数据：", data, __file__, sys._getframe().f_lineno)
        self.triggerButton.set_text(data)  # 向文本框内输入数据
        while self.CircleInitial<self.cycleIndex:
            State = self.triggerButton.window_text()  # 返回输入的文本
            if str(State) == str(data):  # 0
                break
            else:
                print("循环次数")
                self.triggerButton.set_text(data)
            self.CircleInitial = self.CircleInitial + 1


    def Verify_dropDownBox(self,data):
        """
        选择下拉框
        :return:
        """
        print("data:",data)
        self.triggerButton.select(data)  # 下拉框
        while self.CircleInitial < self.cycleIndex:
            State = self.triggerButton.window_text()  # 是否选择预期数据
            if str(State) == str(data):  #
                break
            else:
                self.triggerButton.select(data)
            self.CircleInitial = self.CircleInitial + 1


    """选择下拉框,没有检查"""
    def Verify_dropDownBox_change(self,data):
        """
        选择下拉框
        :return:
        """
        self.triggerButton.select(data)  # 下拉框



    """检查被系统是否在被模块（Aerocherk、frmbook等）"""
    def examine_LocatedModule(self):
        """
        检查被系统是否在被模块（Aerocherk、frmbook等）
        :return:
        """
        titleName=None;moduleName=None
        if self.title=="Aerobook-Aerocheck":
            titleName= ProfileDataProcessing("commonality", "AerocheckEdition").config_File()  # 从配置文件获取Aerocheck窗口标题
            moduleName="Aerocheck"
        elif self.title=="Aerobook-Fiberbook":
            titleName = ProfileDataProcessing("commonality", "FiberbookEdition").config_File()  # 从配置文件获取Aerocheck窗口标题
            moduleName = "Fiberbook"
        else:
            raise MyException("没有找到需要检查的模块：%r"%self.title)
        # 通过Aerobook标题链接Aerobook进程，并切换到Aerobook窗口
        from src.utils.otherMethods.initialize import pywin_openAProgram
        aero_window = pywin_openAProgram().entrance_subroutine_title()
        dlg_spec = aero_window.child_window(auto_id="panel_Graph", control_type="System.Windows.Forms.Panel")
        try:   # 是否能找到被测模块
            dlg_spec.child_window(title=titleName, class_name="wxWindowNR").verify_enabled()
        except Exception:   # 如果没有找到抛出异常
            # 如果没有找到被测模块
            from src.utils.otherMethods.initialize import  UIA_link
            uia_app = UIA_link().EntrySubapplication(moduleName)  # 然后点击进入被测模块的按钮
            try:
                dlg_spec.child_window(title=titleName, class_name="wxWindowNR",).wait("exists", timeout=60, retry_interval=0.5)  # 等待被测模块出现
            except Exception:   # 如果抛出异常说明没有找到被测模块
                raise MyException("没有找到被测试模块:%r"%titleName)















"""窗口置顶"""
class WindowTop:
    """窗口置顶"""

    def __init__(self,window_name):
        self.window_name=window_name

    def console(self,):
        """
        弹窗置顶操作
        :return:
        """
        print("\033[0;31m%r弹窗置顶"%self.window_name, __file__, sys._getframe().f_lineno)
        print("")
        # 首先判断控件是否是最大化
        main_window = Application().connect(title_re=self.window_name, timeout=10)
        Aerobook_main = main_window.window(title_re=self.window_name)
        WindowState=Aerobook_main.is_maximized()  # 判断窗口是否是最大化
        if WindowState:  # 如果是
            pass
        else:            # 如果不是最大化
            Aerobook_main.maximize()  # 窗口最大化
        WindowTop(self.window_name).EnumWindows()  # 窗口置顶显示

    def window_enum_callback(self,hwnd, wildcard):
        """
        窗口置顶
        :param hwnd:
        :param wildcard:
        :return:
        """
        import win32gui, win32com.client,re
        if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) is not None:
            win32gui.BringWindowToTop(hwnd)
            # 先发送一个alt事件，否则会报错导致后面的设置无效：pywintypes.error: (0, 'SetForegroundWindow', 'No error message is available')
            shell = win32com.client.Dispatch("WScript.Shell")
            shell.SendKeys('%')
            # 设置为当前活动窗口
            win32gui.SetForegroundWindow(hwnd)


    def EnumWindows(self):
        import win32gui
        win32gui.EnumWindows(WindowTop(None).window_enum_callback, ".*%s.*" % self.window_name)  # 此处为你要设置的活动窗口名



"""Html格式转化"""
class htmlFormat:
    """Html格式转化"""

    def __init__(self):
        self.str_Name=None
        self.list_Name=[]

    def takeOut_html_label(self,html_location,txt_location):
        """
        取出Html文件中指定标签里的文本
        :param html_location:源文件地址
        :param txt_location: 保存文件地址
        :return:
        """
        with open(html_location, "r", encoding="utf-8") as strf:
            str = strf.read()
        filtrate_1 = r'(?<=<strong>).*?(?=</strong><br /><hr />)'
        filtrate_2 = r'(?<=<span style="color:#bb3d00;">).*?(?=</span>)'
        filtrate2_2 = r'<span style='
        list1 = re.findall(filtrate_1, str)
        for li1 in list1:
            if filtrate2_2 in li1:
                list2 = re.findall(filtrate_2, li1)
                if list2:
                    list2 = list2[0]
                    self.list_Name.append(list2)
            else:
                self.list_Name.append(li1)
        with open(txt_location, "w") as wstr:
            for s in self.list_Name:
                wstr.write(s)
                wstr.write("")
                wstr.write("\n")
        with open(txt_location, 'r') as f:
            self.str_Name = list(f)
        return self.str_Name


    def Filter_nonChinese(self, txt_location,txt_NewLocation):
        """
        过滤没有中文的行
        :param  txt_location: 需要过滤文件地址
        :param  txt_NewLocation: 生成新的文件地址
        :return:
        """
        with open(txt_location, 'r') as f:
            content = list(f)
        for con in content:

            zhmodel = re.compile(u'[\u4e00-\u9fa5]')  # 检查中文
            # zhmodel = re.compile(u'[^\u4e00-\u9fa5]')  #检查非中文
            match = zhmodel.search(con)
            if match:
                con.replace('\n', u'')
                self.list_Name.append(con)
        with open(txt_NewLocation, 'w') as file_object:
            for li in self.list_Name:
                file_object.write(li)


    def MatchingFolders_name(self,filepath,Name):
        """
        匹配文件夹里的名称
        :param  filepath: 文件夹地址
        :param  Name: 需要匹配的文件名称
        :return:
        """
        # 将文件夹内的文件名读进列表m
        filename_list = listdir(filepath)
        # 可以同过简单后缀名判断，筛选出你所需要的文件(这里以.jpg为例)
        for filename in filename_list:  # 依次读入列表中的内容
            if filename.endswith(Name):  # 后缀名'jpg'匹对
                self.list_Name.append(filename)  # 如果是'jpg'文件就添加进列表h
        return self.list_Name



    def compile_HTMl(self,source,Name):
        """
        编译HTML文件，生成TXT格式文件
        :param  source: 文件夹地址
        :param  Name: 需要匹配的文件名称
        :return:
        """
        # 获取生成html文件名称
        list_Name=htmlFormat().MatchingFolders_name(source,Name)
        if list_Name:
            self.str_Name = list_Name[0]
        else:
            raise MyException("没有找到“%r”的文件" % Name)
        HTML_address=source+"/"+self.str_Name
        layoffPeriod_TXT=source+"/"+self.str_Name+".txt"
        ultimately_TXT=source+"/"+"Now_"+self.str_Name+".txt"
        # 取出html里的特定标签里的文本
        htmlFormat().takeOut_html_label(HTML_address, layoffPeriod_TXT)
        # 过滤没有中文的行
        htmlFormat(). Filter_nonChinese(layoffPeriod_TXT, ultimately_TXT)

        return ultimately_TXT



"""控制台打印进度条方法"""
class ProgressBar:
    """控制台打印进度条方法"""

    def __init__(self,Entries,amount=None):
        self.Entries=Entries      # 个数
        self.amount = amount       # 总数


    def progressBar_number(self):
        """
        进度条打印，打印个数
        :return:
        """
        sumTotal = None;rateOfProgress = None
        if self.Entries < self.amount:
            sumTotal = "总“" + str(self.amount) + "”条"
            rateOfProgress = "第“%r”条" % self.Entries
            per_str = "\033[1;34;40m\r%r[%s%s]%r" % (sumTotal, "*" * self.Entries, "-" * (self.amount - self.Entries), rateOfProgress)
            print(per_str, end='', flush=True)
        else:
            sumTotal = "总“" + str(self.amount) + "”条"
            rateOfProgress = "数据处理完毕"
            per_str = "\033[1;34;40m\r%r[%s%s]%r" % (sumTotal, "*" * self.Entries, "-" * (self.amount - self.Entries), rateOfProgress)
            print(per_str)
        # time.sleep(0.3)


    def progressBar_percent(self):
        """
        进度条打印，打印百分比
        :return:
        """
        print('percent: {:.0%}'.format(self.Entries /  self.amount), flush=True)


"""用例参数化"""
class UseCase_parameterization:
    """用例参数化"""

    def __init__(self):
        self.list_dict_site=[]
        self.list_testPoint=[]
        self.location = None

    def parameterization_location(self,moduleName,sole_ModuleIdentifier,list_tableName):
        """
        获取读取电子表格的路径和相关参数
        :return:
        """
        location=None
        if moduleName=="Aerobook-Aerocheck":
            if sole_ModuleIdentifier=="程序初始化用例":
                location = ProfileDataProcessing("testCase", "initializeUsecase").config_File()
            elif sole_ModuleIdentifier=="铺层信息--铺层库优化":
                location = ProfileDataProcessing("testCase", "LaminateOptimize").config_File()
            elif sole_ModuleIdentifier=="铺层信息--铺层数据库制作工具":
                location = ProfileDataProcessing("testCase", "LaminatedataPopup").config_File()
            elif sole_ModuleIdentifier == "尺寸信息--一维单元尺寸定义":
                location = ProfileDataProcessing("testCase", "SizeDefinition_1D").config_File()
            elif sole_ModuleIdentifier == "尺寸信息--二维单元尺寸定义":
                location = ProfileDataProcessing("testCase", "SizeDefinition_2D").config_File()
            elif sole_ModuleIdentifier=="尺寸信息--一维单元尺寸定义（模板）":
                location = ProfileDataProcessing("testCase", "sizeInfo_1DXls").config_File()
            elif sole_ModuleIdentifier=="尺寸信息--二维单元尺寸定义（模板）":
                location = ProfileDataProcessing("testCase", "sizeInfo_2DXls").config_File()
            elif sole_ModuleIdentifier == "求解计算--求解计算":
                location = ProfileDataProcessing("testCase", "solveCalculation").config_File()
            elif sole_ModuleIdentifier == "载荷信息--载荷数据库制作工具":
                location = ProfileDataProcessing("testCase", "loaddatabase_popUp").config_File()
            elif sole_ModuleIdentifier == "载荷信息--编辑工况":
                location = ProfileDataProcessing("testCase", "editWorkingCondition").config_File()
            elif sole_ModuleIdentifier == "材料信息--定义复合材料参数":
                location = ProfileDataProcessing("testCase", "compositeMaterial").config_File()
            elif sole_ModuleIdentifier == "材料信息--定义金属材料参数":
                location = ProfileDataProcessing("testCase", "definitionMetalMaterial").config_File()
            elif sole_ModuleIdentifier == "复材结构强度校核--复合材料强度校核1D":
                 location= ProfileDataProcessing("testCase", "CompoundStrengthCheck_1D").config_File()
            elif sole_ModuleIdentifier == "复材结构强度校核--复合材料强度校核2D":
                location = ProfileDataProcessing("testCase", "CompoundStrengthCheck_2D").config_File()
            elif sole_ModuleIdentifier == "紧固件强度校核--紧固件信息输入":
                location = ProfileDataProcessing("testCase", "fastener_parameterInput").config_File()
            elif sole_ModuleIdentifier == "紧固件强度校核--紧固件参数设置":
                location = ProfileDataProcessing("testCase", "fastener_parameterSetting").config_File()
            elif sole_ModuleIdentifier == "紧固件强度校核--紧固件强度校核":
                location = ProfileDataProcessing("testCase", "fastener_intensityCheck").config_File()
            elif sole_ModuleIdentifier == "紧固件优化--紧固件参数优化":
                location = ProfileDataProcessing("testCase", "fastener_parOptimization").config_File()
            elif sole_ModuleIdentifier == "金属结构强度校核--金属一维单元强度校核":
                location = ProfileDataProcessing("testCase", "metal_intensityCheck1D").config_File()
            elif sole_ModuleIdentifier == "金属结构强度校核--金属二维单元强度校核":
                location = ProfileDataProcessing("testCase", "metal_intensityCheck2D").config_File()
            elif sole_ModuleIdentifier == "金属结构强度校核--金属加筋板强度校核":
                location = ProfileDataProcessing("testCase", "metal_stiffenedPlate").config_File()
            elif sole_ModuleIdentifier == "金属结构强度校核--金属曲板后驱曲强度校核":
                location = ProfileDataProcessing("testCase", "metal_rearGuard").config_File()
            else:
                raise MyException("没有地址:%r"%sole_ModuleIdentifier)
        elif moduleName=="Aerobook-Aerocheck":
            pass
        else:
            raise MyException("没有找到执行模块的用例:%r"%moduleName)
        if list_tableName:
            for tableName in list_tableName:
                dict_site={"详细地址": location,"表单名称": tableName, "初始行": 1,"初始列":1}
                self.list_dict_site.append(dict_site)
        return self.list_dict_site


    def parameterization_data(self,moduleName,list_dicti_argument):
        """
         用例参数化
        :return:
        """
        for dicti_argument in list_dicti_argument :
            for  sole_ModuleIdentifier, tableName in dicti_argument.items():
                # 获取读取电子表格的路径和相关参数
                list_dict=UseCase_parameterization().parameterization_location(moduleName,sole_ModuleIdentifier,tableName)
                for site in list_dict:
                    dicts = read_excel(site).readExcel_testCase()  # 读取测试用例
                    ar_testdicts = FormatConversion().RemoveSubscript(dicts)
                    self.list_dict_site = self.list_dict_site + ar_testdicts
        for dict_site in self.list_dict_site:
            dict = {}
            dict["测试点"] = dict_site["测试点"]
            self.list_testPoint.append(dict)
        return self.list_dict_site,self.list_testPoint


