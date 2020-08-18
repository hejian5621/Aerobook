# -*- coding: UTF-8 -*-
from aip import AipOcr
from config.configurationFile import ProfileDataProcessing
# # 定义常量
# APP_ID = '21783573'
# API_KEY = 'vVajoUGEw7Hzv8Akj5qHd48k'
# SECRET_KEY = 'rSkhRmMI6Q5HzfPz89fTWj6q26GG0GuH'

# print(tuple(API_KEY))
APP_ID=ProfileDataProcessing("commonality","APP_ID").config_File()
API_KEY = ProfileDataProcessing("commonality","API_KEY").config_File()
SECRET_KEY = ProfileDataProcessing("commonality","SECRET_KEY").config_File()
print(tuple(API_KEY))
# 初始化AipFace对象
aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)

# 读取图片
filePath = "/useCase_screenshot/Aerocheck1\\word.png"


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


# 定义参数变量
options = {
    'detect_direction': 'true',
    'language_type': 'CHN_ENG',
}
list1=[]
str1=None
# 调用通用文字识别接口
result = aipOcr.basicGeneral(get_file_content(filePath), options)
words_result = result['words_result']
for i in range(len(words_result)):
    print(words_result[i]['words'])
    list1.append(words_result[i]['words'])
print("list1:",list1)

str1=''.join(list1)
print("str1:",str1)