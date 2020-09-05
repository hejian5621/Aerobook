

from src.utils.otherMethods.controlOperationSuite import ControlOperationSuite
from src.utils.otherMethods.initialize import execute_useCase_initialize
from OperatingControls.enterModule import BeingMeasured_work


from tool import WindowTop
WindowTop.EnumWindows("Aerobook v1.0.4")

location=r"F:\Aerobook\src\testCase\projectFile\automateFile"

parWin1_Dicti = {"窗口标题": "选择铺层数据库保存路径", "关闭窗口控件名称": "保存","地址": location, "文件夹输入内容": "plylib.db"}
nestWin_Dicti = {"嵌套窗口标题": "确认另存为", "嵌套控件名称": "是"}
ControlOperationSuite(None).SelectFile_Popover(parWin1_Dicti, "检查", nestWin_Dicti)