# 获取实际值
import time,os,re, datetime
from tool import pictureProcessing
from pywinauto.application import Application
from tool import htmlFormat
from tool import Check_winControl




class GetActual_Value:
    """获取实际值"""

    def __init__(self,testCase_dict,instance=None):
        self.testCase_dict=testCase_dict
        self.instance = instance
        self.actual_Text=None



    def ActualValue_controller(self):
        """
        获取实际值
        :return:
        """
        Message_type = self.testCase_dict["预期值信息类型"]
        ProjectPath = self.testCase_dict["被测程序文件地址"]
        UseCase_Number = self.testCase_dict["用例编号"]  # 取出预期值
        if Message_type == "警告弹窗":  # 获取警告弹窗的文本信息（实际值）
            result= Warning_PopUp().Check_warning()
            if result:    # 如果警告弹窗存在
                self.actual_Text = Warning_PopUp().Warning_PopUp_TXT(UseCase_Number)
                # 关闭警告窗口
                Check_winControl("警告", "OK").popUp_Whether_close()
            else:
                self.actual_Text="没有警告弹窗"
        elif Message_type == "信息窗口":  # 获取信息窗口的文本信息（实际值）
            self.actual_Text = Information_Win().acquire_HTML_TXT(ProjectPath)
        else:
            import sys, os
            print("该“%r”测试用例没有说实际值的获取途径" % UseCase_Number, __file__, sys._getframe().f_lineno)
            os._exit(0)
        return self.actual_Text



class Warning_PopUp:
    """警告弹窗实际值"""


    def __init__(self):
        pass

    def Check_warning(self):
        """
        检查警告弹窗是否存在
        :return:
        """
        from pywinauto import findwindows
        try:
            app = Application().connect(title_re="警告")
            dlg_spec = app.window(title="警告")
        except findwindows.ElementNotFoundError:
            return False
        else:
            return True


    def Warning_PopUp_TXT(self,UseCase_Number):
        """
        获取警告窗口的文本信息
        :return:
        """
        from config.relative_location import path
        atLast_actuals =None
        relativeAddress = path.location()  # 获取项目相对位置
        app = Application().connect(title_re="警告")
        dlg_spec = app.window(title="警告")
        # 切换到文本信息窗口
        dlg_spec1=dlg_spec.警告DirectUIHWND
        # 获取预期值
        location=relativeAddress+r"src\testCase\d_useCase_screenshot\Aerocheck\\"+UseCase_Number+".png"
        time.sleep(0.5)
        dlg_spec1.capture_as_image().save(location)  # 获取警告弹窗的文本截图
        actuals=pictureProcessing(location).screenshot()    # 读取截图中的文本
        print("actuals",actuals)
        if "」OK" in actuals:
            atLast_actuals=re.sub("」OK", '', actuals)
        elif "OK" in actuals:
            atLast_actuals = re.sub("OK", '', actuals)
        else:
            atLast_actuals=actuals
        dlg_spec.child_window(title="OK", class_name="Button")  # 关闭弹窗
        return atLast_actuals


class  localControl:
    """获取本地控件的文本"""

    def __init__(self,module_window):
        self.module_window=module_window



    def LocalControl_TXT(self):
        """
        本地控件获取实际值
        :return:
        """
        txt = self.module_window.window_text()
        return txt




class Information_Win:
    """获取信息窗口的时间值"""


    def __init__(self):
        pass


    def copyAndPaste(self,dlg_spec,dataQuantity):
        """
        通过复制粘贴的方法获取实际值
        :param dataQuantity: 需要获取的数据数量（数据条数）
        :param dlg_spec: 需要获取的数据数量（数据条数）
        :return:
        """
        from tool import instrument
        n = 0;t=None;txtName="cache.txt";actuals = ""
        # 把信息窗口的文本信息粘贴到粘贴板
        instrument().infoWindow(dlg_spec)
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



    def acquire_HTML_TXT(self, source):
        """
        通过获取HTML文件里的文本，来获取信息窗口的实际值
        :return:
        """
        # 取出HTML文本，只留下有中文的行，在存入TXT文件中
        today = str(datetime.date.today())  # datetime.date类型当前日期
        Name = "Aerocheck_prjLog_" + today + ".html"
        ultimately_TXT = htmlFormat().compile_HTMl(source, Name)
        # 去掉缓存TXT文件里的空行
        with open(ultimately_TXT, 'r') as f:
            content = list(f)
        # 删除TXT文件
        return content