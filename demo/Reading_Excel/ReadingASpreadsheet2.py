
from src.utils.commonality.ExcelFile import read_excel
from src.utils.otherMethods.dataFormatConversion import FormatConversion

from utils.commonality.tool import UseCase_parameterization
#
# dict1 = {"详细地址": r"src\testCase\c_useCase_file\initialize\自动化测试公共属性.xlsx", "表单名称": "测试模块控制",
#          "初始行": 1,"初始列":1}
# dict2=read_excel(dict1).readExcel_modularControl()
# print("dict2:",dict2)
#
# # 处理数据的数据类型
# list_dicti_argument = FormatConversion().UseCase_dataProcessing(dict2)
#
# print(list_dicti_argument)


list_dict_site = UseCase_parameterization().parameterization_data()  # 读取测试用例

print(list_dict_site)




