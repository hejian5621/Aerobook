# 获取配置文件内容

import configparser
import os
import time
from configobj import ConfigObj

class ProfileDataProcessing:
    """读取配置文件"""

    def __init__(self,column ,programa =None):
        """

        :param column :
        :param programa :
        """
        self.column = column
        self.programa  = programa
        self.argument=None


    def config_File(self):
        """
        读取配置文件信息
        参数:
        self.parameter:配置文件里标签
        self.argument：标签下面的键
        :return:配置文件的值
        """
        cf = configparser.ConfigParser()  # 对象实体化
        # 获取当前位置
        curpath = os.path.dirname(os.path.realpath(__file__))
        location = os.path.join(curpath, "config.ini")
        # 找到配置文件
        cf.read(location, encoding='utf-8')
        self.argument = cf.get(self.column, self.programa)
        # print("从配置文件取出的参数:", self.argument)
        return self.argument


    def config_File_amend(self,deploy_value):
        """
        修改配置文件内容
        :return:
        """
        cf = configparser.ConfigParser()  # 对象实体化
        curpath = os.path.dirname(os.path.realpath(__file__))  # 获取当前位置
        location = os.path.join(curpath, "config.ini")   # 配置文件路径
        config = ConfigObj(location, encoding='UTF8')
        config[self.column][ self.programa] = deploy_value
        config.write()














