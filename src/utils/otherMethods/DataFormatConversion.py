# 数据格式类型转化

from src.utils.commonality.ExcelFile import read_excel
import numpy as np


class FormatConversion:
    """数据格式转化"""

    def __init__(self):
        pass

    def ParameterizedFormat(self,detailedAddress,frmName):
        """
        测试用例参数化格式处理。
        从测试用例Excel中取出测试用例后，转化成参数化所需的数组
        :return:
        """
        testdata = []
        site = {"详细地址":detailedAddress , "表单名称": frmName, "初始行": 1}
        testdicts = read_excel(site).readExcel_testCase()
        # print("dict2:", testdicts)
        # for testdict in testdicts:
        #     list1 = []
        #     list1.append(testdict)
        #     testdata.append(list1)
        # ar_testdicts = np.array(testdata)
        print("testdicts:",testdicts)
        return testdicts






