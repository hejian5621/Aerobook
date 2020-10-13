from src.utils.otherMethods.initialize import pywin_openAProgram


# 窗口链接并切换到Aerobook

#
# testdicts={"所在模块":"优化->优化设置->设计变量->二维单元设计变量"}
# module="Aerobook-Fiberbook"

testdicts={"所在模块":"铺层信息->铺层库优化"}
module="Aerobook-Aerocheck"

# testdicts={"所在模块":"File->open"}
# module="Aerobook-Fembook"

aero_window, module_window = pywin_openAProgram(module).menuOpen(testdicts)


