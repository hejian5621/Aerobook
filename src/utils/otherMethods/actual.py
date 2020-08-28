# 获取实际值
import win32clipboard as wc
import os
import time,os
from utils.commonality.tool import instrument
from pywinauto.application import Application
import re, datetime
from src.utils.commonality.tool import htmlFormat


class  reality:
    """实际值获取"""


    def __init__(self):
        pass


    def infoWindow(self,aero_window):
        """
        通过全选/复制信息窗口里的数据，获取实际值
        :return:
        """
        wc.OpenClipboard()
        wc.EmptyClipboard()
        wc.CloseClipboard()
        dlg_spec = aero_window.richText2   # 切换到信息窗口
        dlg_spec.send_keystrokes("^a")     # 全选信息窗口的文本信息
        dlg_spec.send_keystrokes("^c")     # 复制信息窗口的文本信息到粘贴板



class ActualProcessing:
    """实际值处理"""


    def __init__(self,dlg_spec):
        self.dlg_spec=dlg_spec


    def laminateOptimize(self,dataQuantity):
        """
        获取铺层库优化工作栏的实际值
        通过复制粘贴方法获取信息窗口里的数据
        :param dataQuantity: 需要获取的数据数量（数据条数）
        :return:
        """
        n = 0;t=None;txtName="cache.txt";actuals = ""
        # 把信息窗口的文本信息粘贴到粘贴板
        reality().infoWindow(self.dlg_spec)
        # 取出粘贴板的文本信息
        Text=instrument().getCopyText()
        # 把文本信息存入TXT文件中
        file_handle = open(txtName, mode='w')
        file_handle.write(Text)
        file_handle.close()
        time.sleep(1)
        # 去掉缓存TXT文件里的空行
        with open(txtName, "r") as f:  # 打开文件
            lines = f.readlines()  # 读取所有行
            while True:
                if "\n" in lines:
                    lines.remove("\n")
                else:
                    break
        number = len(lines)  # 获取列表元素的个数
        # 取出TXT文件中需要的数据
        while n < dataQuantity:
            actual=None
            line = dataQuantity - n
            t = number - line
            if t >= 0:
                actual = lines[t]   # 取出列表中的对应的元素
                actual = actual[23:]
                actuals = str(actuals) + str(actual)
            n = n + 1
        # 删除TXT文件
        if os.path.exists(txtName): os.remove(txtName)
        return actuals



    def Laminatedata_warning_warning(self,UseCase_Number):
        """
        获取警告窗口的文本信息
        :return:
        """
        from config.relative_location import path
        relativeAddress = path.location()  # 获取项目相对位置
        app = Application().connect(title_re="警告")
        dlg_spec = app.window(title="警告")
        # 切换到文本信息窗口
        dlg_spec1=dlg_spec.警告DirectUIHWND
        # 获取预期值
        location=relativeAddress+r"src\testCase\d_useCase_screenshot\Aerocheck\\"+UseCase_Number+".png"
        dlg_spec1.capture_as_image().save(location)  # 获取警告弹窗的文本截图
        actuals=instrument().screenshot(location)    # 读取截图中的文本
        print("actuals",actuals)
        if "」OK" in actuals:
            atLast_actuals=re.sub("」OK", '', actuals)
        if "OK" in actuals:
            atLast_actuals = re.sub("OK", '', actuals)
        else:
            atLast_actuals=actuals
        dlg_spec2 = dlg_spec.child_window(title="OK", class_name="Button")  # 关闭弹窗
        return atLast_actuals



    def acquire_HTML_TXT(self,source):
        """
        通过获取HTML文件里的文本，来获取信息窗口的实际值
        :return:
        """
        # 取出HTML文本，只留下有中文的行，在存入TXT文件中
        today = str(datetime.date.today())  # datetime.date类型当前日期
        Name = "Aerocheck_prjLog_" + today + ".html"
        ultimately_TXT=htmlFormat().compile_HTMl(source, Name)
        # 去掉缓存TXT文件里的空行
        with open(ultimately_TXT, 'r') as f:
            content = list(f)
        # 删除TXT文件
        return content



    def editWorkingCondition_TXT(self, module_window):
        """
        获取编辑工况弹窗中，获取工况组合下拉框里的文本信息
        :return:
        """
        txt=module_window.ComboBox.window_text()
        return txt




# source=r"F:\Aerobook\src\testCase\projectFile\automateFile"
# content=ActualProcessing(None).acquire_HTML_TXT(source)
# print("content:",content)
