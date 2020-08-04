# -*- coding: UTF-8 -*-
from aip import AipOcr

# 定义常量
APP_ID = '21783573'
API_KEY = 'vVajoUGEw7Hzv8Akj5qHd48k'
SECRET_KEY = 'rSkhRmMI6Q5HzfPz89fTWj6q26GG0GuH'

# 初始化AipFace对象
aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)

# 读取图片
filePath = "456.png"


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


# 定义参数变量
options = {
    'detect_direction': 'true',
    'language_type': 'CHN_ENG',
}

# 调用通用文字识别接口
result = aipOcr.basicGeneral(get_file_content(filePath), options)
print(result)
words_result = result['words_result']
for i in range(len(words_result)):
    print(words_result[i]['words'])