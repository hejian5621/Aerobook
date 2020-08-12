# 选中模型
from pykeyboard import PyKeyboard
from pywinauto import mouse
import time




class  operationalModel:
    """图形区操作"""



    def __init__(self):
         pass


    def selectionModel(self):
        """
        通过键盘和鼠标操作选择模型
        :return:
        """
        k = PyKeyboard()   # 键盘操作方法实例化
        k.press_key(k.shift_key)   # 按下键盘上的shift键
        mouse.press(coords=(345, 167))   # 鼠标长按
        mouse.release(coords=(1488, 727))  # 释放鼠标位置
        k.release_key(k.shift_key) # 释放键盘上的shift键



