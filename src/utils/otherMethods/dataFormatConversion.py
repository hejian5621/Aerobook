#  数据处理

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


    def SelectFile(self,testdicts,actual_editlist,source):
        """

        :return:
        """
        expect1 = None
        expect2 = None
        actual1 = None
        actual2 = None
        expect1_binrowseButton=testdicts["选择铺层Excel文件浏览按钮对应文本框预期"]
        expect2_binrowseButton = testdicts["铺层数据保存路径浏览对应文本框预期"]
        if expect1_binrowseButton != "默认" and expect2_binrowseButton=="默认":
            expect1 = source + expect1_binrowseButton
            actual1=actual_editlist["选择铺层Excel文件浏览按钮对应文本框实际"]
        elif expect1_binrowseButton == "默认" and expect2_binrowseButton!="默认":
            expect2 = source + expect2_binrowseButton
            actual2 = actual_editlist["铺层数据保存路径浏览对应文本框实际"]
        elif expect1_binrowseButton != "默认" and expect2_binrowseButton!="默认":
            expect1 = source + expect1_binrowseButton
            expect2 = source + expect2_binrowseButton
            actual1 = actual_editlist["选择铺层Excel文件浏览按钮对应文本框实际"]
            actual2 = actual_editlist["铺层数据保存路径浏览对应文本框实际"]
        return actual1,actual2,expect1,expect2








