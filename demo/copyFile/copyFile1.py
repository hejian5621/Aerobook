
from config.relative_location import  path

import os
import shutil




relativeAddress = path.location()  # 获取项目相对位置
target = relativeAddress + r"src\testCase\projectFile\自动化测试相关文件"  # 被复制文件的详细路径
source= relativeAddress + r"\src\testCase\projectFile\automateFile"  # 被复制文件的详细路径

# source_path = os.path.abspath(target)
# target_path = os.path.abspath(source)
#
# if not os.path.exists(target_path):
#     os.makedirs(target_path)
#
# if os.path.exists(source_path):
#     # root 所指的是当前正在遍历的这个文件夹的本身的地址
#     # dirs 是一个 list，内容是该文件夹中所有的目录的名字(不包括子目录)
#     # files 同样是 list, 内容是该文件夹中所有的文件(不包括子目录)
#     for root, dirs, files in os.walk(source_path):
#         for file in files:
#             src_file = os.path.join(root, file)
#             shutil.copy(src_file, target_path)
#             print(src_file)
#
# print('copy files finished!')

# my_file = os.path.isfile(source)  # 判断文件是否存在

print("source:",source)

if os.path.isdir(r"F:\Aerobook\\src\testCase\projectFile\automateFile"):
    print("文件存在！")
else:
    print("文件不存在！")

# print("my_file:",my_file)
# shutil.rmtree(source)

