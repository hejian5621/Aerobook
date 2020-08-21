
#
# from pywinauto.application import Application

from pywinauto.keyboard import send_keys
from pykeyboard import PyKeyboard



from pywinauto import mouse
import time


# 选择单元结构

# time.sleep(5)
# k = PyKeyboard()
# k.press_key(k.shift_key)
#
# # 鼠标长按
# mouse.press(coords=(345,167))
# # time.sleep(2)
# # # 释放鼠标位置
# mouse.release(coords=(1488,727))
#
# k.release_key(k.shift_key)

send_keys('{ENTER}')


# 使用Ctrl+A  ，Ctrl+C

# 鼠标点击操作，可以修改coords来指定点击位置
mouse.click(button='left', coords=(0, 0))
# 鼠标双击操作，可以修改coords来指定双击位置
mouse.double_click(button='left', coords=(0, 0))
# 移动鼠标，可以修改coords使鼠标移动到指定位置
mouse.move(coords=(0, 0))
# 鼠标右键点击，可以修改coords来指定右键点击位置
mouse.right_click(coords=(0, 0))
# 鼠标滚动操作，可以修改coords来指定滚动位置，修改wheel_dist来指定滚动距离
mouse.scroll(coords=(0, 0), wheel_dist=1)









