
#知识点：如何自定义类
class MyException(Exception):                   #让MyException类继承Exception
    def __init__(self,name):
        self.name = name



import win32gui
try:
    # 知识点：主动抛出异常，就是实例化一个异常类
    hwnd = win32gui.FindWindow(None, "警告")  # 通过弹窗的标题获取弹窗的句柄
    print(hwnd)
    if hwnd == 0:
        raise MyException("没有找到弹窗" )  # 实例化一个异常,实例化的时候需要传参数
except Exception as obj:  # 万能捕获，之前的可能捕获不到，这里添加Exception作为保底
    print("没有弹窗")
else:
    print("有弹窗")