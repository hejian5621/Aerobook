
from src.utils.commonality.ExcelFile import read_excel




site ={"详细地址": r"src\testCase\c_useCase_file\材料信息\自动化定义许用值.xlsx", "表单名称": "测试1", "初始行": 1,"初始列":1}

dicts1 = read_excel(site).readExcel_testCase()  # 读取测试用例

print("dicts1:",dicts1)