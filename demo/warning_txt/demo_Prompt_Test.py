# 获取警告弹窗文本

from pywinauto.application import Application
import time
from utils.otherMethods.actual import Warning_PopUp
from config.relative_location import path
#
# atLast_actuals = None
# relativeAddress = path.location()  # 获取项目相对位置
# app = Application().connect(title_re="提示")
# app1 = app.window(title_re="提示")
#
# app12=app1.DirectUIHWND
#
# app12.print_control_identifiers()
time.sleep(2)


UseCase_Number='1111'

Popup_type="警告"

dicti_actual = Warning_PopUp().Warning_PopUp_TXT(UseCase_Number,Popup_type)

print(dicti_actual)
