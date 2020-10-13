# 铺层库优化工作栏

from src.utils.otherMethods.initialize import pywin_openAProgram
from OperatingControls.enterModule import BeingMeasured_popupWin


testdicts={"所在模块":"铺层信息->铺层库优化"}

module="Aerobook-Aerocheck"

aero_window, module_window = pywin_openAProgram(module).menuOpen(testdicts)