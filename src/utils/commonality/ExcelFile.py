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
        self.dataPackage = dataPackage



    def readExcel_testCase (self):
        """
        读取电子表格里的内容生成列表嵌套字典数据类型的值
        :return:
        """
        detailedAddress = self.dataPackage["详细地址"];  menu_table_name = self.dataPackage["表单名称"];onset = int(self.dataPackage["初始行"])
        list_dicti_Excel = []  # 空的列表
        relativeAddress = path.location()  # 获取项目相对位置
        if detailedAddress and menu_table_name and onset:  # 判断详细地址、表单名称和初始行都不为空的情况下
            CompleteAddress = relativeAddress + detailedAddress  # 获取完整的地址
            data = xlrd.open_workbook(CompleteAddress)  # 打开需要读取的电子表格
            table = data.sheet_by_name(menu_table_name)  # 根据表单名称获取对应表单的数据
            rowns = table.nrows  # 获取总行数
            list_row_title = table.row_values(onset - 1)  # 取出标题行一行的数据
            while rowns > onset:
                list_row_value = table.row_values(onset)  # 获取整行的值
                dicti_Excel = dict(zip(list_row_title, list_row_value))  # 标题列表跟值列表合并成字典
                onset = onset + 1
                list_dicti_Excel.append(dicti_Excel)
        else:
            print("传入的电子表格地址、表单名称和初始行数不能为空，表格地址：%r；表单名称：%r；初始行数：%r" % (detailedAddress, menu_table_name, onset),
                  __file__, sys._getframe().f_lineno)
            os._exit(0)
        return list_dicti_Excel

#
#
# dict1={"详细地址":"src\\testCase\\useCase_file\\Aerocheck\\铺层库优化工具.xlsx","表单名称":"模块说明","初始行":1}
# dict2=read_excel(dict1).readExcel_testCase()
# print("dict2:",dict2)
#

