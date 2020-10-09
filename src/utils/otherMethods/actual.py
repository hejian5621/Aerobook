# 获取实际值
import time,os,re, datetime,sys
from tool import pictureProcessing
from pywinauto.application import Application
from tool import htmlFormat
from tool import Check_winControl
from src.utils.otherMethods.dataFormatConversion import FormatConversion
from src.utils.OperatingControls.moduleControlOperation import OperatingControls
from OperatingControls.enterModule import GetWindowInstance
from tool import folderFile_dispose
from tool import MyException



class GetActual_Value:
    """获取实际值"""

    def __init__(self,testCase_dict,instance=None):
        self.property=testCase_dict
        self.instance = instance
        self.list_Message_type = []
        self.dicti_actual = None
        self.list_dicti_actual=[]
        self.actual_dicti_type ={}


    def ActualValue_controller(self,result):
        """
        获取实际值
        :param result: 因为在程序启动或执行用例前需要做的初始化前不需要实例值
        :return:
        """
        if result==1:
            pass
        else:

            Message_type = self.property["预期值信息类型"]
            UseCase_Number = self.property["用例编号"]
            print("\033[0;32;35m《开始获取实际值，获取的途径：%r》\033[0m" % Message_type, __file__, sys._getframe().f_lineno)
            print("")
            # 判断是不是有多个检查类型
            if "；" in Message_type:   # 如果预期值信息类型值中有“；”，就说明有多个检查类型
               self.list_Message_type = Message_type.split("；")
            else:                      # 如果预期值信息类型值中没有“；”，就说明有只有一个检查类型
                self.list_Message_type.append(Message_type)
            for Message_type in self.list_Message_type:   # 循环取出检查类型
                if Message_type == "警告弹窗":  # 获取警告弹窗的文本信息（实际值）
                    result= Warning_PopUp().Check_warning()
                    if result:    # 如果警告弹窗存在
                        self.dicti_actual = Warning_PopUp().Warning_PopUp_TXT(UseCase_Number)
                        # 关闭警告窗口
                        Check_winControl("警告", "OK").popUp_Whether_close()
                    else:
                        self.dicti_actual="没有警告弹窗"
                elif Message_type == "信息窗口":  # 获取信息窗口的文本信息（实际值）
                    old_content = self.property["信息窗口之前的文本"]  # 取出之前的信息窗口数据
                    ProjectPath = self.property["被测程序文件地址"]
                    new_content = Information_Win().acquire_HTML_TXT(ProjectPath)  # 取出信息窗口实时数据
                    self.dicti_actual = FormatConversion().GetLatestData(new_content, old_content)
                elif Message_type == "控件文本":  # 获取信息窗口的文本信息（实际值）
                    self.dicti_actual = localControl(self.instance).LocalControl_TXT(self.property)
                elif Message_type == "控件截图":  # 获取控件的实际值截图
                    # 获取工况组合下拉框里的文本信息
                    self.dicti_actual =screenshot(self.instance).interceptPicture(self.property,Message_type)
                elif Message_type == "文件检查":  #
                    ProjectPath = self.property["被测程序文件地址"]
                    BeforeTime = self.property["用例步骤执行前时间"]
                    # 取出文件夹里文件所有的名称, 并且根据实际筛选出符合时间条件的文件名称
                    self.dicti_actual=folderFile_dispose(ProjectPath).FetchFileName(BeforeTime)
                    # 列表转化成字符串,强行转化
                    self.dicti_actual=str(self.dicti_actual)
                else:
                    raise MyException("该%r测试用例没有说实际值的获取途径" % UseCase_Number)
                # 把获取的单个检查类型放在列表嵌套字典中
                self.actual_dicti_type[Message_type]=self.dicti_actual
            print("\033[0;34m获取到的实际值：\033[0m",self.actual_dicti_type)
            print("")
            print("\033[0;32;35m{{获取实际值完毕}}\033[0;32;35m", __file__, sys._getframe().f_lineno)
            print("")
            print(" ")
        return self.actual_dicti_type









class Warning_PopUp:
    """警告弹窗实际值"""


    def __init__(self):
        pass

    def Check_warning(self):
        """
        检查警告弹窗是否存在
        :return:
        """
        from pywinauto import findwindows,timings
        try:
            app = Application().connect(title_re="警告",timeout=0.5)
            dlg_spec = app.window(title="警告")
        except (findwindows.ElementNotFoundError,timings.TimeoutError):
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




    def Get_window_identity(self,property):
        """
        获取窗口或者唯一标识
        :return:
        """
        expect_control = property["预期值控件标识属性"]
        list_Message_type = None
        # 取出窗口
        win_one = self.module_window[0]
        win_two = self.module_window[1]
        win_three = self.module_window[2]
        win_four = self.module_window[3]
        if expect_control:
            if "；" in expect_control:
                list_Message_type = expect_control.split("；")
                if len(list_Message_type) == 5:
                    pass
                else:
                    raise MyException("当获取实际值，使用“控件文本”获取文本时，“预期值控件标识属性”字段虽然没有为空,也转化成了列表，但是属性不足值：%r"% list_Message_type)
            else:
                raise MyException("当获取实际值，使用“控件文本”获取文本时，“预期值控件标识属性”字段虽然没有为空但是，由于没有“；”特殊字符“，所有无法转化成列表,值：%r"% list_Message_type)
        else:
            raise MyException("当获取实际值，使用“控件文本”获取文本时，“预期值控件标识属性”字段不能为空")
        # 如果需要获取实际值的控件所在窗口等于步骤操作的窗口，就用之前的窗口
        if property["操作窗口标题"] == list_Message_type[0] and property["操作子窗口标题"] == list_Message_type[1]:
            pass
        else:
            # 切换到被测模块窗口
            property["操作窗口标题"] = list_Message_type[0]
            property["操作子窗口标题"] = list_Message_type[1]
            win_one, win_two, win_three, win_four = GetWindowInstance(property).get_window_instance()
        logo = list_Message_type[2]
        method = list_Message_type[3]
        win = list_Message_type[4]
        # 获取操作控件的实际窗口
        WindowInstance = OperatingControls(win_one, win_two, win_three, win_four).acquire_controlWin(win)
        # 获取操作控件的唯一标识
        dlg_spec = OperatingControls(WindowInstance).IdentificationMethod(method, logo)
        return dlg_spec



    def LocalControl_TXT(self,property):
        """
        本地控件获取实际值
        :return:
        """
        # 获取控件的唯一标识
        dlg_spec=localControl(self.module_window).Get_window_identity(property)
        # 获取控件的文本
        txt = dlg_spec.window_text()
        return txt





class screenshot:
    """截取图片"""

    def __init__(self,module_window):
        self.module_window = module_window


    def interceptPicture(self,property,Message_type=None):
        """
       截取图片返回图片地址
       :return:
       """
        UseCase_Number=property["用例编号"]
        # 获取控件的唯一标识
        self.module_window = localControl(self.module_window).Get_window_identity(property)
        location=r"F:\Aerobook\src\testCase\d_useCase_screenshot\expectScreenshots"+"\\"+UseCase_Number+".png"
        # 截取图片
        self.module_window.capture_as_image().save(location)  # 获取警告弹窗的文本截图
        return location



    def UseCaseFailureScreenshot(self,UseCase_Number,Message_type):
        """
        把截的图片移动到生成测试
        :return:
        """
        import shutil
        old_path = r"F:\Aerobook\src\testCase\d_useCase_screenshot\expectScreenshots\test_1.png"
        new_path = r"F:\Aerobook\src\testCase\a_useCaseSet\Aerockeck\img\test_1.png"
        shutil.copyfile(old_path, new_path)









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
        print("\033[0;32;34m获取信息窗口数据\033[0m", __file__, sys._getframe().f_lineno)
        print("")
        # 取出HTML文本，只留下有中文的行，在存入TXT文件中
        today = str(datetime.date.today())  # datetime.date类型当前日期
        Name = "Aerocheck_prjLog_" + today + ".html"
        ultimately_TXT = htmlFormat().compile_HTMl(source, Name)
        # 去掉缓存TXT文件里的空行
        with open(ultimately_TXT, 'r') as f:
            content = list(f)
        content = [x.strip() for x in content]
        # 删除TXT文件
        return content