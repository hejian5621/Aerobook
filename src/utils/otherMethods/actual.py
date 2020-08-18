# 获取实际值

import time,os
from utils.commonality.tool import instrument
from pywinauto.application import Application
import re


class  reality:
    """实际值获取"""


    def __init__(self):
        pass


    def infoWindow(self,aero_window):
        """
        通过全选/复制信息窗口里的数据，获取实际值
        :return:
        """

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



    def Laminatedata_warning_warning(self,expect_result):
        """
        获取警告窗口的文本信息
        :return:
        """
        atLast_actuals=None
        app = Application().connect(title_re="警告")
        dlg_spec = app.window(title="警告")
        # 切换到文本信息窗口
        dlg_spec1=dlg_spec.警告DirectUIHWND
        # 获取预期值
        site=r"F:\Aerobook\src\testCase\useCase_screenshot\Aerocheck1\\"
        location=site+expect_result+".png"
        dlg_spec1.capture_as_image().save(location)  # 获取警告弹窗的文本截图
        actuals=instrument().screenshot(location)
        if "」OK" in actuals:
            atLast_actuals=re.sub("」OK", '', actuals)
        else:
            atLast_actuals=actuals
        return atLast_actuals
