

from src.utils.commonality.ExcelFile import read_excel
import time

# 控件属性已经操作方法
site1 ={"详细地址": r"src\testCase\c_useCase_file\Aerocheck\initialize\自动化测试用例初始化.xlsx", "表单名称": "铺层数据库制作工具-控件属性已经操作方法", "初始行": 1,"初始列":1}
dicts1 = read_excel(site1).readExcel_ControlProperties()  # 读取测试用例


site2 ={"详细地址": r"src\testCase\c_useCase_file\Aerocheck\initialize\自动化测试用例初始化.xlsx", "表单名称": "铺层数据库制作工具", "初始行": 1,"初始列":1}
dicts2 = read_excel(site2).readExcel_testCase()  # 读取测试用例
print("dicts1：",dicts1)
print("dicts2：",dicts2)

