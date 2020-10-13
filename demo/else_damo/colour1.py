
import os,sys

# 控制台输出内容样式

tested_Module="铺层信息--铺层库优化"
UseCase_Number="jjj0001"
print("")
print("\033[0;33m$$$《“%r”模块开始测试，执行用例：%r》\033[0m" % (tested_Module, UseCase_Number), __file__, sys._getframe().f_lineno)
print("")
print("")
print("\033[0;32;35m《开始进行执行用例前的准备工作》\033[0m", __file__, sys._getframe().f_lineno)
print("")
real_arg=0
global_UseCase_Name="铺层信息--铺层库优化"
print("初始化全局变量，全局变量参数：%r，全局变量模块名称：%r"%(real_arg, global_UseCase_Name), __file__, sys._getframe().f_lineno)
print("")

sole_ModuleIdentifier="金属结构强度校核--金属曲板后驱曲强度校核"
list_CloseWindows=["警告", "选择校核工况"]

print("\033[0;32;34m检查”%r“模块，弹窗是否关闭,需要检查的弹窗标题：%r\033[0m" % (sole_ModuleIdentifier,list_CloseWindows), __file__, sys._getframe().f_lineno)
print("")
print("\033[0;40;36m{{准备工作准备完毕}}", __file__, sys._getframe().f_lineno)
print("")

print("\033[0;32;34m实际值跟预期值对比\033[0m", __file__, sys._getframe().f_lineno)

print("\033[0;31m$$$《执行用例“%r”执行结束》$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\033[0m" % UseCase_Number)

print("\033[0;32;34m检查”%r“模块，弹窗是否关闭,需要检查的弹窗标题：%r\033[0m" % (sole_ModuleIdentifier, list_CloseWindows), __file__, sys._getframe().f_lineno)