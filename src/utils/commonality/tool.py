# 工具
from pykeyboard import PyKeyboard
from pywinauto import mouse
from config.configurationFile import ProfileDataProcessing
from aip import AipOcr
import win32clipboard as wc
import os,shutil,win32con,time,os,sys
from pywinauto.application import Application
from pywinauto  import findwindows,timings
import re
from os import listdir
from pathlib import Path




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
        """
        self.k.press_key(self.k.shift_key)   # 按下键盘上的shift键
        mouse.press(coords=(345, 167))   # 鼠标长按
        mouse.release(coords=(1488, 727))  # 释放鼠标位置
        self.k.release_key(self.k.shift_key) # 释放键盘上的shift键


"""图片处理"""
class pictureProcessing:
    """图片处理"""


    def __init__(self,path):
        self.path=path   # 图片的位置
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


    def delfile(self, list_filename):
        """
        批量删除文件
        :param list_filename:
        :return:
        """
        # 拼接文件名和路径
        for path1 in list_filename:  # 取出文件路径
            list_path = self.sourceDir + "\\" + path1
            my_file = Path(list_path)
            if my_file.is_file():  # 先检查文件是否存在
                # 指定的文件存在，就删除
                os.remove(list_path)


"""检查窗口或者控件，是否存在"""
class  Check_winControl:
    """检查窗口或者控件，是否存在"""


    def __init__(self,title, triggerButton,cycleIndex=10,CircleInitial=1):
        self.title=title  # 窗口标题
        self.triggerButton = triggerButton  # 控制实体
        self.cycleIndex = cycleIndex    # 循环最终次数
        self.CircleInitial = CircleInitial # 循环初始次数
        self.state=None



    #检查触发摸一个事件（点击按钮），应该出现的弹窗或者控件是否出现
    def window_WhetherOpen(self):
        """
        检查触发摸一个事件（点击按钮），应该出现的弹窗或者控件是否出现
        如果出现，程序正常运行
        如果没有出现，程序停止运行
        :param title: 预期弹出弹窗的标题
        :param event_button: 触发的按钮操作
        :return:
        """
        self.triggerButton.click()    # 点击触发弹窗的按钮
        # 判断弹窗是否弹窗，如果没有弹出，就继续点击
        while self.CircleInitial <= self.cycleIndex:  # 如果没有找到控件，就继续点击触发按钮
            result =None
            try:
                Application().connect(title=self,timeout=0.5)
            except findwindows.ElementAmbiguousError:  # 捕获如果有多个重复的弹窗的异常
                break
            except (findwindows.ElementNotFoundError,timings.TimeoutError):  # 如果找不到弹窗
                if (self.CircleInitial % 10) == 0:    #  如果循环次数数10的倍数，就再次点击按钮
                    self.triggerButton.click()
                elif  self.CircleInitial==1 :    # 如果第一次链接不是，在点击一次
                    self.triggerButton.click()
            except findwindows.ElementNotFoundError or timings.TimeoutError:  # 如果找不到弹窗
                if (self.CircleInitial % 10) == 0:  # 如果循环次数数10的倍数，就再次点击按钮
                    self.triggerButton.click()
                elif self.CircleInitial == 1:  # 如果第一次链接不是，在点击一次
                    self.triggerButton.click()
            else:
                break                                 # 如果找到了弹窗就退出弹窗
            if self.CircleInitial == (self.cycleIndex + 1):
                print("%s窗口没有找到"%self.title, __file__, sys._getframe().f_lineno)
                os._exit(0)
            self.CircleInitial=self.CircleInitial+1



    def nest_popUpWindows(self,nest_title,nest_triggerButton):
        """
        处理带有嵌套弹窗的弹窗
        检查点击按钮后窗口是否关闭，如果没有关闭，继续点击按钮
        :return:
        """
        while self.CircleInitial <= self.cycleIndex:
            close_result=Check_winControl(self.title,self.triggerButton,1,1).popUp_Whether_close("嵌套")   # 然后在检查弹窗有没有关闭
            if close_result=="窗口已正常关闭":
                break
            Check_winControl(nest_title, nest_triggerButton).popUp_Whether_close()  # 检查有没有嵌套弹框
            self.CircleInitial = self.CircleInitial + 1
            if self.CircleInitial == (self.cycleIndex + 1):
                print("%s窗口没有关闭" % self.title, __file__, sys._getframe().f_lineno)
                os._exit(0)



    def popUp_Whether_close(self, nest=None):
        """
        检查点击按钮后窗口是否关闭，如果没有关闭，继续点击按钮
        :param nest: 判断掉该方法是否在有嵌套弹窗的情况下
        :param nest_win: 控件操作方法
        :param nestWin_Dicti: 嵌套标题
        :return:
        """
        while self.CircleInitial <= self.cycleIndex:
            try:
                app = Application().connect(title=self.title, timeout=0.1)
                py_app = app.window(title=self.title)  # 切换到需要关闭的窗口
            except findwindows.ElementAmbiguousError:  # 捕获如果有多个重复的弹窗的异常
                print("多个重复的弹窗", __file__, sys._getframe().f_lineno)
                os._exit(0)
            except (findwindows.ElementNotFoundError,timings.TimeoutError): # 如果窗口不存在就退出循环
                self.state="窗口已正常关闭"
                break
            else:     # 如果没有异常执行下面的代码，说明窗口并没有关闭
                if py_app[self.triggerButton].exists():  # 如果控件存在
                    py_app[self.triggerButton].click()
                else:
                    print("没有找到关闭窗口的按钮", __file__, sys._getframe().f_lineno)
                    os._exit(0)
            self.CircleInitial = self.CircleInitial + 1
            if self.CircleInitial == (self.cycleIndex + 1) and nest!="嵌套":
                print("%s窗口没有关闭" % self.title, __file__, sys._getframe().f_lineno)
                os._exit(0)
        return self.state



    def Verify_CheckBox_Status(self):
        """
        确认勾选框是否勾选，如果没有勾选，就勾选
        :return:
        """
        self.triggerButton.click()  # 勾选勾选框
        while self.CircleInitial<self.cycleIndex:
            State=self.triggerButton.get_check_state()   # 返回勾选框的勾选状态
            if State==0:  # 0 表示没有勾选上
                self.triggerButton.click()
            else:
                break
            self.CircleInitial = self.CircleInitial + 1



    def Verify_inputBox(self,data):
        """
        验证输入框是否输入正确的数据，如果还没有输入就再次输入，一直到输入成功为止
        :return:
        """
        self.triggerButton.set_text(data)  # 文本框
        while self.CircleInitial<self.cycleIndex:
            State = self.triggerButton.window_text()  # 返回勾选框的勾选状态
            if State == data:  # 0 表示没有勾选上
                break
            else:
                self.triggerButton.set_text(data)
            self.CircleInitial = self.CircleInitial + 1

    def Verify_dropDownBox(self,data):
        """
        验证输入框是否输入正确的数据，如果还没有输入就再次输入，一直到输入成功为止
        :return:
        """
        self.triggerButton.select(data)  # 下拉框
        while self.CircleInitial < self.cycleIndex:
            State = self.triggerButton.window_text()  # 返回勾选框的勾选状态
            if State == data:  # 0 表示没有勾选上
                break
            else:
                self.triggerButton.select(data)
            self.CircleInitial = self.CircleInitial + 1


"""窗口置顶"""
class WindowTop:
    """窗口置顶"""

    def window_enum_callback(hwnd, wildcard):
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


    def EnumWindows(window_name):
        import win32gui
        win32gui.EnumWindows(WindowTop.window_enum_callback, ".*%s.*" % window_name)  # 此处为你要设置的活动窗口名


"""Html格式转化"""
class htmlFormat:
    """Html格式转化"""

    def __init__(self):
        self.str_Name=None
        self.list_Name=[]

    def takeOut_html_label(self,html_location,txt_location):
        """
        取出Html文件中指定标签里的文本
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
            print("没有找到“%s”的文件" % Name, __file__, sys._getframe().f_lineno)
            os._exit(0)
        HTML_address=source+"/"+self.str_Name
        layoffPeriod_TXT=source+"/"+self.str_Name+".txt"
        ultimately_TXT=source+"/"+"Now_"+self.str_Name+".txt"
        # 取出html里的特定标签里的文本
        list_Name = htmlFormat().takeOut_html_label(HTML_address, layoffPeriod_TXT)
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






