from src.utils.commonality.ExcelFile import read_excel


moduleName="Aerobook-Aerocheck"


sole_ModuleIdentifier="金属结构强度校核--金属曲板后驱曲强度校核"

site = {"详细地址": r"src\testCase\c_useCase_file\initialize\自动化测试公共属性.xlsx", "表单名称": moduleName,
        "初始行": 3, "初始列": 1}
dicts_title = read_excel(site).readExcel_common()  # 从Excel表格中取出要关闭窗口的标题


location=dicts_title[sole_ModuleIdentifier]

print("dicts_title：",dicts_title )

print("location：",location )