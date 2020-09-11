
from src.utils.OperatingControls.moduleControlOperation import OperatingControls
from src.utils.commonality.ExcelFile import read_excel
import time

# 控件属性已经操作方法
site1 ={"详细地址": r"src\testCase\c_useCase_file\Aerocheck\铺层信息\自动化铺层库优化.xlsx", "表单名称": "控件属性已经操作方法", "初始行": 1,"初始列":1}
dicts1 = read_excel(site1).readExcel_ControlProperties()  # 读取测试用例


site2 ={"详细地址": r"src\testCase\c_useCase_file\Aerocheck\铺层信息\自动化铺层库优化.xlsx", "表单名称": "测试", "初始行": 1,"初始列":1}
dicts2 = read_excel(site2).readExcel_testCase()  # 读取测试用例
print("dicts1：",dicts1)
print("dicts2：",dicts2)







from OperatingControls.enterModule import BeingMeasured_work
from src.utils.otherMethods.initialize import pywin_openAProgram
from tool import WindowTop
# 被系统置顶
WindowTop.EnumWindows("Aerobook v1.0.4")
for dict in dicts2 :

    testdicts={"所在模块":"铺层信息->铺层库优化"}


    dict["被测程序文件地址"]= r"F:\Aerobook\src\testCase\projectFile\automateFile"


    aero_window, module_window = pywin_openAProgram().menuOpen(testdicts)

    # 通过操作菜单栏，打开被测模块，然后切换到被测模块
    module_window1=BeingMeasured_work( module_window).workField_general()




    OperatingControls(module_window).controlConsole(dicts1,dict)
#
    # living="Edit2"
    #
    # time.sleep(1)
#     module_window1.print_control_identifiers()
    module_window1.Button2.check()
    module1_window=module_window1.Button2
    module1_window.click()
    print("使用方法",dir(module1_window.wrapper_object()))


