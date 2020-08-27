
from pywinauto  import findbestmatch,findwindows
from pywinauto.application import Application
from src.utils.otherMethods.initialize import programInitialization
from config.configurationFile import ProfileDataProcessing







try:
    Aero_window = Application().connect(title_re="指定Excel模板文件路径")
    Aero_window.window(title="指定Excel模板文件路径")
except findwindows.ElementAmbiguousError:
    print(" 捕获到异常")
except findwindows.ElementNotFoundError:
    print(" 找不到元素")
else:
    print("没有异常执行该代码")