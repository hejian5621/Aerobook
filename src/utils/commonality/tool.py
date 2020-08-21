# 工具
from pykeyboard import PyKeyboard
from pywinauto import mouse
from config.configurationFile import ProfileDataProcessing
from aip import AipOcr
import win32clipboard as wc
import os,shutil,win32con,time,os,sys
from config.relative_location import path


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
        wc.CloseClipboard()
        text=copy_text.decode('GB2312')
        return text



    def copyFile(self):
        """
        复制文件夹或者文件
        :return:
        """
        relativeAddress = path.location()  # 获取项目相对位置
        target = relativeAddress + r"src\testCase\projectFile\自动化测试相关文件"  # 被复制文件的详细路径
        source = relativeAddress + r"src\testCase\projectFile\automateFile"  # 被复制文件的详细路径
        source_path = os.path.abspath(target)
        target_path = os.path.abspath(source)
        if not os.path.exists(target_path):
            os.makedirs(target_path)
        if os.path.exists(source_path):
            # root 所指的是当前正在遍历的这个文件夹的本身的地址
            # dirs 是一个 list，内容是该文件夹中所有的目录的名字(不包括子目录)
            # files 同样是 list, 内容是该文件夹中所有的文件(不包括子目录)
            for root, dirs, files in os.walk(source_path):
                for file in files:
                    src_file = os.path.join(root, file)
                    shutil.copy(src_file, target_path)
            print('被测文件“%s“生成完成'%source)
        return source



    def delFile(self):
        """
        强制删除文件夹
        :return:
        """
        relativeAddress = path.location()  # 获取项目相对位置
        source = relativeAddress + r"\src\testCase\projectFile\automateFile"  # 被复制文件的详细路径
        if os.path.isdir(r"F:\Aerobook\\src\testCase\projectFile\automateFile"):
            shutil.rmtree(source)
            print('文件“%s“删除完毕' % source)



    def window_WhetherExist(self,dlg_spec,app,promptMessage,frequency=3, wait_time=1 ):
        """
        确定窗口是否存在
        :param dlg_spec: 触发窗口出现的按钮
        :param app: 窗口对象
        :param promptMessage: 如果没有找到控件的提示信息
        :param frequency: 如果没有找到控件的提示信息
        :param wait_time: 每次等待时间
        :return:
        """
        frequency=int(frequency)
        wait_time=int(wait_time)
        control = 0  # 循环初始次数
        while control <= frequency :  # 如果没有找到控件，就继续点击触发按钮
            control = control + 1
            if app.exists(): #  判断窗口是否存在
                break
            else:       # 如果不存在点击触发按钮
                dlg_spec.click()
                time.sleep(wait_time)
        if control == (frequency + 1):
            print(promptMessage,__file__, sys._getframe().f_lineno)
            os._exit(0)


    def window_WhetherClose(self,dlg_spec,app,promptMessage,
                            dlg_spec1=None,app1=None,operation="不检查",windowTitle=None,frequency=3, wait_time=1):
        """
        判断窗口是否关闭
        :return:
        """
        frequency = int(frequency)
        wait_time = int(wait_time)
        control = 0  # 循环初始次数
        while control <= frequency:  # 如果没有找到控件，就继续点击触发按钮
            control = control + 1
            if app.exists():  # 判断窗口是否存在
                if operation=="检查":
                    if app1.exists():  # 判断窗口是否存在
                        dlg_spec1.click()
                        time.sleep(wait_time)
                    else:
                        dlg_spec.click()
                        time.sleep(wait_time)
                else:
                    dlg_spec.click()
                    time.sleep(wait_time)
            else:  # 如果不存在点击触发按钮
                break
        if control == (frequency + 1):
            print(promptMessage, __file__, sys._getframe().f_lineno)
            os._exit(0)


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



