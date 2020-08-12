# 获取项目文件的相对位置
import os

class  path:

    @staticmethod
    def location():
        address  = os.path.dirname(os.path.realpath(__file__))
        address=address[:-6]
        return address


# a=ProjectFolderLocation.ToObtainPosition()
# print("a:",a)