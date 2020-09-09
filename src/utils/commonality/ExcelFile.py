# 读取自动化测试用例
#coding:utf-8
import sys,os,xlrd
from config.relative_location import  path




class read_excel():
    """读取excel文件"""

    def __init__(self, dataPackage):
        """
        :param dataPackage: {"详细地址":"detailedAddress","表单名称":"menu_table_name","初始行":"onset",} 需要读取电子表格的地址
        """
        detailedAddress = dataPackage["详细地址"]
        self.menu_table_name = dataPackage["表单名称"]
        self.onset = int(dataPackage["初始行"])
        self.oncol = int(dataPackage["初始列"])
        self.list_dicti_Excel = []  # 空的列表
        self.list_dicti_dicti_Excel = {}  # 空的字典
        relativeAddress = path.location()  # 获取项目相对位置
        # 首先判断参数是否为空
        if detailedAddress and self.menu_table_name and self.onset and  self.oncol :  # 判断详细地址、表单名称和初始行都不为空的情况下
            self.CompleteAddress = relativeAddress + detailedAddress  # 获取完整的地址
        else:
            print("传入的电子表格地址、表单名称、初始行数和初始列数不能为空，表格地址：%r；表单名称：%r；初始行数：%r；初始列数：%r" % (
                detailedAddress, self.menu_table_name, self.onset,self.oncol),__file__, sys._getframe().f_lineno)
            os._exit(0)




    def readExcel_testCase (self):
        """
        读取电子表格里的内容生成列表嵌套字典数据类型的值
        :return:
        """
        data = xlrd.open_workbook(self.CompleteAddress)  # 打开需要读取的电子表格
        table = data.sheet_by_name(self.menu_table_name)  # 根据表单名称获取对应表单的数据
        rowns = table.nrows  # 获取总行数
        list_row_title = table.row_values(self.onset - 1)  # 取出标题行一行的数据
        while rowns > self.onset:
            list_row_value = table.row_values(self.onset)  # 获取整行的值
            dicti_Excel = dict(zip(list_row_title, list_row_value))  # 标题列表跟值列表合并成字典
            self.onset = self.onset + 1
            self.list_dicti_Excel.append(dicti_Excel)
        return  self.list_dicti_Excel


    def readExcel_ControlProperties(self):
        """
        读取Excel表格内容，读取控件属性
        :return:数据类型，字典嵌套字典
        """
        data = xlrd.open_workbook(self.CompleteAddress)  # 打开需要读取的电子表格
        table = data.sheet_by_name(self.menu_table_name)  # 根据表单名称获取对应表单的数据
        colns = table.ncols  # 获取总列数
        list_row = table.row_values(self.onset - 1)  # 取出第一行的数据
        del list_row[0]    #  删除第一行，第一个值
        list_col = table.col_values(self.oncol - 1)  # 取出第一列的数据
        del list_col[0]     #  删除第一列，第一个值
        oncol_n=self.oncol-1
        for rowone in list_row:   #取出第一行第一个数据
            list_col_value=None
            list_col_value = table.col_values(self.oncol)  # 获取整列的值
            del list_col_value[0]
            dicti_Excel = dict(zip(list_col, list_col_value))  # 标题列表跟值列表合并成字典
            self.list_dicti_dicti_Excel[rowone]= dicti_Excel
            self.oncol= self.oncol+1
        return self.list_dicti_dicti_Excel






# #
# dict1 = {"详细地址": r"src\testCase\c_useCase_file\Aerocheck\铺层信息\自动化铺层库优化.xlsx", "表单名称": "控件属性已经操作方法",
#          "初始行": 1,"初始列":1}
# dict2=read_excel(dict1).readExcel_ControlProperties()
# print("dict2:",dict2)
#
#

