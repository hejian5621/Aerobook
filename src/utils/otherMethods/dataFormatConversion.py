#  数据处理

import os,sys
from config.relative_location import path



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



    def Actual_dataProcessing(self,dictSet,dicti_actual,location):
        """
        实际值格式规范
        :return:
        """
        # 如果有"控件截图"类型的检查，就直接在这个里面进行对比，获得的对比结果放到实际值字典中
        from tool import pictureProcessing
        if  "控件截图" in dicti_actual:  # 控件截图如果在“预期值信息类型”里
            path=dicti_actual["控件截图"]
            dicti_actual["控件截图"] = pictureProcessing(location,path).imageComparison() # 图片对比
        # 实际值数据处理
        for infowin,actual_result in dicti_actual.items():
            if type(actual_result) == list:  # 实际值如果是列表，就转化成字符串
                actual_result = ' '.join(actual_result)
            if actual_result:  # 如果实际值不为空
                actual_result = actual_result.strip()  # 去掉实际值，前后的空格
            dicti_actual[infowin]=actual_result
        return dicti_actual



    def expect_dataProcessing(self, dictSet, listt_dicti_actual):
        """
       预期值格式处理，用于实际值跟预期值对比的时候，保证对比的格式准确
       :return: 预期值字典；如果有“控件截图”类型的检查，就返回预期值图片的位置
        """
        dict_expect ={};path_value=None
        messageType=dictSet["预期值信息类型"]
        expect_result = dictSet["预期结果文本信息"]
        #   去掉预期结果前后的空格
        if expect_result:  # 如果预期值不为空
            expect_result = expect_result.strip()  # 去掉预期值，前后的空格
        # 字符串转化成列表
        if "；" in messageType:   # 如果预期值信息类型值中有“；”，就说明有多个检查类型
           messageType = messageType.split("；")
           if "；" in expect_result:  # 如果预期值信息类型值中有“；”，就说明有多个检查类型
               expect_result = expect_result.split("；")
        # 把两个列表和成字典
        if type(messageType)==list and type(expect_result)==list :   #  如果“预期值信息类型”和“预期结果文本信息”都是列表
            dict_expect = dict(zip(messageType, expect_result))      #  就把两个列表合成一个字典
        elif type(messageType) == str and type(expect_result) == str:
            dict_expect ={messageType:expect_result}
        else:
            from tool import MyException
            raise MyException("预期值信息类型和预期结果文本信息不匹配,预期值信息类型:%r;预期结果文本信息：%r"%(type(messageType),type(expect_result)))
        if   "控件截图" in dict_expect:  # 控件截图如果在“预期值信息类型”里
            # 获取“预期值信息类型”中“控件截图”详细的地址
            location=dict_expect["控件截图"]
            relativeAddress = path.location()  # 获取项目相对位置
            path_value=relativeAddress+location
            # 把预期结果放入，预期值字典中
            dict_expect["控件截图"]="图片一样"
        return dict_expect,path_value




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








# a1 =["a","b","c","d","e","f","g","h","j","k"]
# b1 =["a","b","c","d","e","f"]
# c1=FormatConversion().GetLatestData(a1,b1)
# print(c1)




