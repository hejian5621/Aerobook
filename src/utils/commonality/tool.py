# 工具
from pykeyboard import PyKeyboard
from pywinauto import mouse
from config.configurationFile import ProfileDataProcessing
from aip import AipOcr
import win32clipboard as wc
import win32con


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

