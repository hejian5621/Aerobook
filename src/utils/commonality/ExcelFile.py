# 读取自动化测试用例
#coding:utf-8
import sys,os,xlrd
from config.relative_location import  path
from time import *




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
            sys.exit(0)




    def readExcel_testCase (self):
        """
        读取电子表格里的内容生成列表嵌套字典数据类型的值
        :return:
        """

        data = xlrd.open_workbook(self.CompleteAddress)  # 打开需要读取的电子表格
        table = data.sheet_by_name(self.menu_table_name)  # 根据表单名称获取对应表单的数据
        rowns = table.nrows  # 获取总行数
        list_row_title = table.row_values(self.onset - 1)  # 取出标题行一行的数据
        begin_time = time()
        while rowns > self.onset:
            list_row_value = table.row_values(self.onset)  # 获取整行的值
            dicti_Excel = dict(zip(list_row_title, list_row_value))  # 标题列表跟值列表合并成字典
            self.onset = self.onset + 1
            self.list_dicti_Excel.append(dicti_Excel)
        end_time = time()
        run_time = end_time - begin_time
        print('该循环程序运行时间：', run_time)
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


    def readExcel_common(self):
        """
        读取Excel表格内容，读取控件属性
        :return:数据类型，字典嵌套字典
        """
        data = xlrd.open_workbook(self.CompleteAddress)  # 打开需要读取的电子表格
        table = data.sheet_by_name(self.menu_table_name)  # 根据表单名称获取对应表单的数据
        colns = table.ncols  # 获取总列数
        list_row_one = table.row_values(self.onset - 1)  # 取出初始行的数据
        del list_row_one[0]  # 删除第一列的数据
        list_row_two = table.row_values(self.onset)  # 取出初始行开始第二行的数据
        del list_row_two[0]  # 删除第一列的数据
        dicti_Excel = dict(zip(list_row_one,list_row_two))  # 标题列表跟值列表合并成字典
        return dicti_Excel



    def readExcel_modularControl(self):
        """
        读取Excel表格内容，测试模块
        :return:数据类型，字典嵌套字典
        """
        data = xlrd.open_workbook(self.CompleteAddress)  # 打开需要读取的电子表格
        table = data.sheet_by_name(self.menu_table_name)  # 根据表单名称获取对应表单的数据
        colns = table.nrows  # 获取总行数数
        while self.onset<=colns:
            list_row_one = table.row_values(self.onset - 1)  # 取出初始行的数据
            row_one = list_row_one[0]  # 取出初始行第一列的数据
            del list_row_one[0]  # 删除第一列的数据
            list_row_two = table.row_values(self.onset)  # 取出初始行开始第二行的数据
            del list_row_two[0]  # 删除第一列的数据
            dicti_Excel = dict(zip(list_row_one,list_row_two))  # 标题列表跟值列表合并成字典
            # 删除键值为空的键值
            for k in list(dicti_Excel.keys()):
                if not dicti_Excel[k]:
                    del dicti_Excel[k]
            # 把第一行和第二行的放入字典
            self.list_dicti_dicti_Excel[row_one]=dicti_Excel
            self.onset +=2
        return  self.list_dicti_dicti_Excel




    def readExcel_testCase_blank(self):
        """
        读取测试用例，控件与其他方法区分开
        :return:
        """
        dicti_dicti_Excel={}
        dicti_Excel={}
        arg=None
        row_one=None
        row_two=None
        row_three=None
        lis55=[]
        data = xlrd.open_workbook(self.CompleteAddress)  # 打开需要读取的电子表格
        table = data.sheet_by_name(self.menu_table_name)  # 根据表单名称获取对应表单的数据
        list_row_one = table.row_values(self.onset-1)  # 取出初始行的数据
        list_row_two = table.row_values(self.onset)  # 取出初始行的数据
        begin_time = time()
        # print('该循环程序运行时间1：', run_time1)
        colns = table.nrows  # 获取总行数数
        onse = self.onset + 1
        print("colns:",colns)
        while onse <colns:
            dicti_dicti_Excel = {}
            list_row_three = table.row_values(onse)  # 取出初始行的数据
            # 获取第一行数据列表的元素总数
            sun=len(list_row_one)
            n =0
            while n <=sun:
                if n <sun:
                    row_one=list_row_one[n]  # 取出第一列的标题
                    row_two=list_row_two[n]  # 取出第二列的标题
                    row_three=list_row_three[n]  # 取出值
                else:
                    row_one = arg
                if row_one!="":
                    if n != 0:
                        dicti_dicti_Excel[arg] = dicti_Excel
                    arg = row_one      # 把第一行的标题复制个定值
                    dicti_Excel = {}   # 情况字典
                dicti_Excel[row_two] = row_three  # 把每一列的数据跟标题生成字典
                n+=1
            onse+=1
            lis55.append(dicti_dicti_Excel)
        print("lis.append:", lis55)
        end_time = time()
        run_time = end_time - begin_time
        print ('该循环程序运行时间：',run_time)







#
# dict1 = {"详细地址": r"src\testCase\c_useCase_file\Fiberbook\设置变量\一维单元设计参数（截面尺寸）.xlsx", "表单名称": "测试一",
#          "初始行": 1,"初始列":1}
# read_excel(dict1).readExcel_testCase_blank()
#
# read_excel(dict1).readExcel_testCase()

# read_excel(None).closure_Excel_course()




