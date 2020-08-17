# 数据处理

from src.utils.commonality.ExcelFile import read_excel
import numpy as np


class FormatConversion:
    """数据处理"""

    def __init__(self):
        pass

    def RemoveSubscript(self,testdicts):
        """
        取出列表嵌套字典，取出不需要执行用例的下标
        :return:
        """
        list1=[]
        for date in testdicts:
            if date["用例状态"] == "不执行":
                Angle = testdicts.index(date)
                del testdicts[Angle]
        return testdicts






