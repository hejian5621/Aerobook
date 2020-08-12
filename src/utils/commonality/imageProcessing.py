# 通过百度API获取图片的文本信息

from config.configurationFile import ProfileDataProcessing
from aip import AipOcr

class  picture_text:
    """图片处理"""


    def __init__(self,dlg_spec):
        self.dlg_spec=dlg_spec

    def get_file_content(self,filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()


    def screenshot(self, path):
        """
        截取实际值
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
        result = aipOcr.basicGeneral(picture_text(None).get_file_content(path), options)
        words_result = result['words_result']
        for i in range(len(words_result)):
            list1.append(words_result[i]['words'])
        # 合并列表
        str = ''.join(list1)
        return str

# str2=picture_text(None).screenshot("F:\\Aerobook\\src\\testCase\\useCase_screenshot\\Aerocheck\\word.png")
# print("str2:",str2)
