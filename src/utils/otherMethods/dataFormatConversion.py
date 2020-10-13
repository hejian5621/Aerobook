#  数据处理

import os,sys
from config.relative_location import path



class FormatConversion:
    """数据处理"""

    def __init__(self):
        pass

    def RemoveSubscript(self,testdicts,dicti_argument):
        """
        过滤掉不执行的用例
        并且把所有模块名称放入用例中
        :return:
        """
        list1=[]
        for date in testdicts:
            if date["用例状态"] == "不执行":
                Angle = testdicts.index(date)
                del testdicts[Angle]
            date["测试主模块"]=dicti_argument
        return testdicts





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



    def UseCase_dataProcessing(self,str_spacing):
        """
        用例数据处理
        :param str_spacing:
        :return:
        """
        module_dict={}
        sonModuleName_list=[]
        sonModule_list=[]
        useCase_module_dict = {}
        if "测试主模块" in str_spacing:  # 取出主模块名称
            module_dict=str_spacing["测试主模块"]
        else:
           pass
        # 过滤掉不需要执行的主模块
        moduleName_list=FormatConversion().filtration_executingState(module_dict)
        # 根据主模块名取出对应的子模块名，放入列表
        for moduleName in moduleName_list:  # 循环取出主模块名称
            useCase_sonModule_dict = {}
            if moduleName in str_spacing:  # 取出子模块名称
                sonModule_dict = str_spacing[moduleName] # 取出子模块
                # 过滤掉不需要执行的子模块
                sonModule_list = FormatConversion().filtration_executingState(sonModule_dict)
                # 根据子模块名取表名
                for sonModule in sonModule_list:
                    if sonModule in str_spacing:  # 取出子模块名称
                        tableName_dict = str_spacing[sonModule]  # 取出子模块对应的表名称
                        # 过滤掉不需要执行的表名
                        tableName_list = FormatConversion().filtration_executingState(tableName_dict)
                        # 把表名放入子模块字典中
                        useCase_sonModule_dict[sonModule]=tableName_list
                # 最后生成字典嵌套字典嵌套列表数据类型的被测模块
                useCase_module_dict[moduleName]=useCase_sonModule_dict
        return useCase_module_dict


    # {"Aerobook-Aerocheck":{"铺层信息--铺层库优化":["表名一","表名二"],"铺层信息--铺层库优化":["表名一","表名二"]},"Aerobook-Fiberbook":{"铺层信息--铺层库优化":["表名一","表名二"]}}



    def filtration_executingState(self,dict_module):
        """
        过滤执行状态
        :return:
        """
        moduleName_list = []
        for run_state, moduleName in dict_module.items():  # 循环取出模块执行状态和模块名称
            if "不执行" not in run_state:  # 筛选出带“执行”的模块
                moduleName_list.append(moduleName)
        return  moduleName_list








# a1 =["a","b","c","d","e","f","g","h","j","k"]
# b1 =["a","b","c","d","e","f"]
# c1=FormatConversion().GetLatestData(a1,b1)
# print(c1)




