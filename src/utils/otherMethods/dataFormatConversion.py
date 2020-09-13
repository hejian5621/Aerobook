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



    def GetLatestData(self,list_new,list_old):
        """
        两个列表对吧，去掉前面重复的数据
        :return:
        """
        while True:
            if list_new and list_old:
                new = list_new[0]
                old = list_old[0]
                if new == old:
                    del list_new[0]
                    del list_old[0]
                else:
                    break
            else:
                break
        return list_new




    def takeOut_space(self,str_spacing):
        """
        去掉空格
        :return:
        """
        list_NoSpace = []
        str_spacing = str_spacing.strip()  # 去掉字符串的前后空格
        str_spacing = str_spacing.split("\n") # 根据\n把字符串转化成列表
        for str in str_spacing: # 去掉列表中每一个元素的前后空格
            str = str.strip()
            list_NoSpace.append(str)
        return list_NoSpace



    def str_dicti(self):
        """
        拼接数据类型，用于读取读取Excel表格用例
        :return:
        """




# a1 =["a","b","c","d","e","f","g","h","j","k"]
# b1 =["a","b","c","d","e","f"]
# c1=FormatConversion().GetLatestData(a1,b1)
# print(c1)




