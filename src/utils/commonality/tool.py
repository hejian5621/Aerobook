# 工具
from pykeyboard import PyKeyboard
from pywinauto import mouse
from config.configurationFile import ProfileDataProcessing
from aip import AipOcr
import win32clipboard as wc
import os,shutil,win32con,time,os,sys
from config.relative_location import path
from pywinauto.application import Application,AppNotConnected
from pywinauto  import findbestmatch,findwindows
import re, datetime
from os import listdir
from pathlib import Path


class  instrument:
    """工具类"""


    def __init__(self):
        pass



    def selectionModel(self):
        """
        通过键盘和鼠标操作选择模型
        :return:
        """
        k = PyKeyboard()   # 键盘操作方法实例化
        k.press_key(k.shift_key)   # 按下键盘上的shift键
        mouse.press(coords=(345, 167))   # 鼠标长按
        mouse.release(coords=(1488, 727))  # 释放鼠标位置
        k.release_key(k.shift_key) # 释放键盘上的shift键



    def screenshot(self, path):
        """
        通过百度的API读取图片中的文本信息
        :param path: 实际值图片保存路径
        :return:
        """
        list1=[]
        # 截取实际值图片
        # self.dlg_spec.capture_as_image().save(path)
        # 从配置文件中读取百度API的“APP_ID” 、“API_KEY”、“SECRET_KEY”
        APP_ID=ProfileDataProcessing("commonality","APP_ID").config_File()
        API_KEY = ProfileDataProcessing("commonality","API_KEY").config_File()
        SECRET_KEY = ProfileDataProcessing("commonality","SECRET_KEY").config_File()
        # 定义参数变量
        options = {'detect_direction': 'true','language_type': 'CHN_ENG',}
        # 初始化AipFace对象
        aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)
        # 调用通用文字识别接口
        result = aipOcr.basicGeneral(instrument().get_file_content(path), options)
        words_result = result['words_result']
        for i in range(len(words_result)):
            list1.append(words_result[i]['words'])
        # 合并列表
        str = ''.join(list1)
        return str


    def get_file_content(self,filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()



    def getCopyText(self):
        """
        获取剪切板里的数据
        :return:
        """
        wc.OpenClipboard()
        copy_text = wc.GetClipboardData(win32con.CF_TEXT)
        wc.EmptyClipboard()
        wc.CloseClipboard()
        text=copy_text.decode('GB2312')
        return text


    def copyFile(self, sourceDir, targetDir):
        # 完全连子目录也会复制好，美观
        copyFileCounts = 0
        for f in os.listdir(sourceDir):
            sourceF = os.path.join(sourceDir, f)
            targetF = os.path.join(targetDir, f)
            if os.path.isfile(sourceF):
                if not os.path.exists(targetDir):
                    os.makedirs(targetDir)
                copyFileCounts += 1
                if not os.path.exists(targetF) or (
                        os.path.exists(targetF) and (os.path.getsize(targetF) != os.path.getsize(sourceF))):
                    open(targetF, "wb").write(open(sourceF, "rb").read())
            if os.path.isdir(sourceF):
                instrument().copyFile(sourceF, targetF)


    def delfolder(self):
        """
        强制删除文件夹
        :return:
        """
        relativeAddress = path.location()  # 获取项目相对位置
        source = relativeAddress + r"\src\testCase\projectFile\automateFile"  # 被复制文件的详细路径
        if os.path.isdir(r"F:\Aerobook\\src\testCase\projectFile\automateFile"):
            shutil.rmtree(source)
            print('文件“%s“删除完毕' % source)


    def delfile(self,source,list_filename):
        """
        批量删除文件
        :param list_filename:
        :param source:
        :return:
        """
        # 拼接文件名和路径
        for path1 in list_filename:  # 取出文件路径
            list_path=source+"\\"+path1
            my_file = Path(list_path)
            if my_file.is_file():   # 先检查文件是否存在
                # 指定的文件存在，就删除
                os.remove(list_path)



    def window_WhetherOpen(self,title,event_button):
        """
        点击摸一个按钮后，预期弹出的窗口是否弹出，如果没有弹出，再次点击该按钮，一直等到该窗口出现
        :param title: 预期弹出弹窗的标题
        :param event_button: 触发的按钮操作
        :return:
        """
        typeError_str="a"; predict = "There are 3 elements that match the criteria"
        # 点击触发弹窗的按钮
        event_button.click()
        time.sleep(0.5)
        # 判断弹窗是否弹窗，如果没有弹出，就继续点击
        frequency = 5  # 点击次数
        control = 0  # 循环初始次数
        while control <= frequency:  # 如果没有找到控件，就继续点击触发按钮
            result =None
            try:
                time.sleep(0.5)
                app = Application().connect(title=title)
                result = "找到了窗口"
            except findwindows.ElementAmbiguousError:  # 捕获如果有多个重复的弹窗的异常
                break
            except findwindows.ElementNotFoundError:  # 如果窗口不存在就退出循环
                event_button.click()
                time.sleep(1)
            else:
                break
            if control == (frequency + 1):
                print("%s窗口没有找到"%title, __file__, sys._getframe().f_lineno)
                os._exit(0)
            control=control+1



    def control_WhetherExist(self,dlg_spec, promptMessage,operation,text=None):
        """
        判断控件是否存在
        :param dlg_spec: 触发窗口出现的按钮
        :param text: 文本数据
        :param operation: 对控件的操作方法
        :param promptMessage: 如果没有找到控件的提示信息
        :return:
        """
        edit_box=None
        control = 1  # 循环初始次数
        n=5
        while control<=n:  # 如果没有找到控件，就继续点击触发按钮
            t=1
            if dlg_spec.exists():  # 判断窗口是否存在
                if operation=="window_text":
                    edit_box=dlg_spec.window_text()
                elif operation=="set_text":
                    dlg_spec.set_text(text)
                elif operation=="click":
                    dlg_spec.click()
                break
            else:  # 如果不存在点击触发按钮
                time.sleep(t)
            control=control+t
        if control == (n + 1):
            print("没有找到“%s”"%promptMessage,__file__, sys._getframe().f_lineno)
            os._exit(0)
        return edit_box



    def popUp_Whether_close(self,parWin_Dicti,nest_win="不检查",nestWin_Dicti=None):
        """
        检查弹窗是否存在，如果存在就关闭弹窗,如果不存在就不管
        :param parWin_Dicti: 选择文件弹窗的属性参数
        :param nest_win: 控件操作方法
        :param nestWin_Dicti: 嵌套标题
        :return:
        """
        result = None;app = None;typeError_str = None;nest_result = None
        title = parWin_Dicti["窗口标题"]
        control = parWin_Dicti["关闭窗口控件名称"]
        operation = parWin_Dicti["关闭窗口控件操作方法"]
        while True:
            try:
                app = Application().connect(title=title)
            except findwindows.ElementAmbiguousError:  # 捕获如果有多个重复的弹窗的异常
                pass
            except AppNotConnected: # 捕获如果有多个重复的弹窗的异常
                pass
            except findwindows.ElementNotFoundError: # 如果窗口不存在就退出循环
                break
            else:     # 如果没有异常执行下面的代码
                py_app = app.window(title=title)  # 切换到对应窗口
                if py_app[control].exists():  # 如果控件存在
                    if operation == "click":  # 操作控件
                        py_app[control].click()
                # 检查是否有嵌套窗口——————————————————————————————————————————————
                if nest_win == "检查":
                    nest_title = nestWin_Dicti["嵌套窗口标题"]
                    nest_control = nestWin_Dicti["嵌套控件名称"]
                    nest_oper = nestWin_Dicti["嵌套控件操作方法"]
                    try:
                        app = Application().connect(title=nest_title)
                        nest_result = "找到了嵌套窗口"
                    except findwindows.ElementAmbiguousError:  # 捕获如果有多个重复的弹窗的异常
                        pass
                    except findwindows.ElementNotFoundError:  # 如果窗口不存在就退出循环
                        pass
                    else:
                        if nest_result == "找到了嵌套窗口":  # 窗口存在
                            py_app = app.window(title=nest_title)  # 切换到嵌套窗口
                            if py_app[nest_control].exists():  # 如果嵌套窗口中的控件存在
                                if nest_oper == "click":  # 操作控件
                                    py_app[nest_control].click()
                            else:  # 如果控件不存在
                                print("没有找到“%s”窗口" % nest_title, __file__, sys._getframe().f_lineno)
                                os._exit(0)



class htmlFormat:
    """Html格式转化"""

    def __init__(self):
        pass


    def takeOut_html_label(self,html_location,txt_location):
        """
        取出Html文件中指定标签里的文本
        :return:
        """
        content = None;list3 = []
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
                    list3.append(list2)
            else:
                list3.append(li1)
        with open(txt_location, "w") as wstr:
            for s in list3:
                wstr.write(s)
                wstr.write("")
                wstr.write("\n")
        with open(txt_location, 'r') as f:
            content = list(f)
        return content


    def Filter_nonChinese(self, txt_location,txt_NewLocation):
        """
        过滤没有中文的行
        :param  txt_location: 需要过滤文件地址
        :param  txt_NewLocation: 生成新的文件地址
        :return:
        """
        list2 = []
        with open(txt_location, 'r') as f:
            content = list(f)
        for con in content:
            zhmodel = re.compile(u'[\u4e00-\u9fa5]')  # 检查中文
            # zhmodel = re.compile(u'[^\u4e00-\u9fa5]')  #检查非中文
            match = zhmodel.search(con)
            if match:
                list2.append(con)
        with open(txt_NewLocation, 'w') as file_object:
            for li in list2:
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
        list_Name = []
        # 可以同过简单后缀名判断，筛选出你所需要的文件(这里以.jpg为例)
        for filename in filename_list:  # 依次读入列表中的内容
            if filename.endswith(Name):  # 后缀名'jpg'匹对
                list_Name.append(filename)  # 如果是'jpg'文件就添加进列表h
        return list_Name



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

            str_Name = list_Name[0]
        else:
            print("没有找到“%s”的文件" % Name, __file__, sys._getframe().f_lineno)
            os._exit(0)
        HTML_address=source+"/"+str_Name
        layoffPeriod_TXT=source+"/"+str_Name+".txt"
        ultimately_TXT=source+"/"+"Now_"+str_Name+".txt"
        # 取出html里的特定标签里的文本
        list_Name = htmlFormat().takeOut_html_label(HTML_address, layoffPeriod_TXT)
        htmlFormat(). Filter_nonChinese(layoffPeriod_TXT, ultimately_TXT)
        return ultimately_TXT








# today = str(datetime.date.today())   #datetime.date类型当前日期
# source=r"F:\Aerobook\src\testCase\projectFile\automateFile"
# Name="Aerocheck_prjLog_"+today+".html"
# htmlFormat(). compile_HTMl(source, Name)
