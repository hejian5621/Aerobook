# 铺层库优化

from src.utils.otherMethods.initialize import pywin_openAProgram
from OperatingControls.enterModule import BeingMeasured_popupWin


testdicts={"所在模块":"铺层信息->铺层库优化"}

aero_window, module_window = pywin_openAProgram().execute_useCase_enterInto(testdicts)