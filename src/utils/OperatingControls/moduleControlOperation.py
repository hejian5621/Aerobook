# 铺层库优化工作栏，对应Aerobook路径：铺层信息--》铺层库优化
import time,sys, os
from src.utils.otherMethods.controlOperationSuite import ControlOperationSuite
from tool import KeyboardMouse,Check_winControl



class OperatingControls:
    """操作控件"""




    def __init__(self,window_one=None,window_two=None,window_three =None,window_four =None):
        self.win_one=window_one
        self.win_two = window_two
        self.win_three = window_three
        self.win_four = window_four
        self.dlg_spec=None
        self.list_AfterParsing=None


    def console(self,Silverlight,argument ):
        """
        操作控件控制台
        每次循环就是操作一次控件
        :param Silverlight: 控件的属性，例如：唯一标识、操作方法等
        :param argument: 控件输入参数和需不要操作
        :return:
        """
        print("\033[0;34m 《进入操作控件函数开始操作控件》\033[0m")
        print(" ")
        location = argument["被测程序文件地址"]
        els = argument["其他"]
        # 循环取出“控件属性已经操作方法”内的数据
        for ControlsName, ControlProperties in Silverlight.items():  # 循环取出控件
            if ControlsName in argument:
                operational = argument[ControlsName]
                print("开始操作控件：%r 值：%r" % (ControlsName, operational))
                if operational != "默认":  # 当控件不等于默认（默认代表不用操作控件）
                    ControlTypes = ControlProperties["控件类型"]
                    operateWin = ControlProperties["所操作实例"]
                    Controlmethod = ControlProperties["唯一标识方法"]
                    discern = ControlProperties["唯一标识"]
                    waitingTime = ControlProperties["操作控件后等待时间"]
                    Control_mode = ControlProperties["唯一标识方法"]
                    ControlWin = OperatingControls(self.win_one,self.win_two,self.win_three,self.win_four).acquire_controlWin(operateWin) # 获取操作控件实例
                    dlg_spec = OperatingControls(ControlWin).IdentificationMethod(Controlmethod, discern)  # 获取操作控件实例
                    if ControlTypes == "文本框":  # 当控件是文本框的时候
                        if "][" in operational:  # 当输入的参数中有“][”符号，代表此文本框为路径文本框，并且需要拼接路径
                            list_operational = operational.split("；")
                            operational  = list_operational[0]
                            operational = location + operational    # 拼接路径
                        Check_winControl(None, dlg_spec).Verify_inputBox(operational)   # 向文本框中输入数据
                        print("在控件”%r“文本框中输入：%r" % (ControlsName, operational))
                    elif ControlTypes == "勾选框" or ControlTypes == "单选框" or ControlTypes == "复选框":
                        Check_winControl(None, dlg_spec).Verify_CheckBox_Status()
                        print("控件%r成功勾选" % ControlsName)
                    elif ControlTypes == "按钮" :
                        dlg_spec.click_input()
                        print("控件”%r“按钮点击成功" % ControlsName)
                    elif ControlTypes == "按钮--弹窗套件":  # 操作套件
                        OperatingControls(dlg_spec).button_popUp(ControlProperties, location)
                        PopupTitle = ControlProperties["套件参数一"]
                        print("控件%r按钮点击后，成功弹出“%r”弹窗" % (ControlsName, PopupTitle))
                    elif ControlTypes == "坐标--单击--文本框":
                        OperatingControls(ControlWin).coord_click_textbox(ControlProperties,operational)
                        print("控件%r坐标选择正确，并且在文本框中正确输入数据" % ControlsName)
                    elif ControlTypes == "坐标--双击--弹窗套件":
                        OperatingControls(ControlWin).coord_dblclick_popUp(ControlProperties,operational)
                        print("控件%r操作成功" % ControlsName)
                    elif ControlTypes == "坐标--三击--文本框":
                        OperatingControls(ControlWin).coord_click_textbox(ControlProperties,operational)
                        print("控件%r操作成功" % ControlsName)
                    elif ControlTypes == "坐标--键盘--文本框":
                        OperatingControls(ControlWin).coord_click_textbox(ControlProperties,operational)
                        print("控件%r操作成功" % ControlsName)
                    elif ControlTypes == "下拉框":
                        if Control_mode=="方式二":
                            Check_winControl(None, dlg_spec).Verify_dropDownBox_change(operational)
                        else:
                            Check_winControl(None, dlg_spec).Verify_dropDownBox(operational)
                        print("控件%r下拉框选择数据成功" % ControlsName)
                    elif ControlTypes == "滚动鼠标":
                        OperatingControls(dlg_spec).scrollMouse()
                    else:
                        print("说明控件属性", __file__, sys._getframe().f_lineno)
                        os._exit(0)
                    time.sleep(waitingTime)
                else:
                    print("不操作控件“%r”：%r" % (ControlsName,operational))
                    print(" ")
            else:
                print("不操作控件“%r”" %ControlsName)
                print(" ")
            print("\033[0;34m控件操作完成 \033[0m")
            print(" ")
            print(" ")





    def acquire_controlWin(self,ControlInstance):
        """
        获取操作控件的窗口  acquire_controlWin
        :return:
        """
        if ControlInstance=="窗口一":
            if self.win_one:
                return  self.win_one
            else:
                print("传过来的实例为空", __file__, sys._getframe().f_lineno)
                os._exit(0)
        elif ControlInstance=="窗口二":
            if self.win_two:
                return self.win_two
            else:
                print("传过来的实例为空", __file__, sys._getframe().f_lineno)
                os._exit(0)
        elif ControlInstance=="窗口三":
            if self.win_three:
                return self.win_three
            else:
                print("传过来的实例为空", __file__, sys._getframe().f_lineno)
                os._exit(0)
        elif ControlInstance == "窗口四":
            if self.win_four:
                return self.win_four
            else:
                print("传过来的实例为空", __file__, sys._getframe().f_lineno)
                os._exit(0)
        else:
            if self.win_one:
                return self.win_one
            else:
                print("传过来的实例为空", __file__, sys._getframe().f_lineno)
                os._exit(0)



    def IdentificationMethod(self,Controlmethod,discern):
        """
        因为从电子表格获取的控件标识字符串，拼接在操作控件的时候会报错，暂时还没有找到原因，暂时使用该方法拼接操作方法
        :return:
        """
        # 解析参数
        if "；" in discern:
            self.list_AfterParsing = discern.split("；")
            discern=self.list_AfterParsing[-1]
        if Controlmethod=="方式一":
           self.dlg_spec= OperatingControls(self.win_one).ExpressionAssembly(discern)
           Check_winControl("警告", "OK").popUp_Whether_close()
        elif Controlmethod=="方式二":
            if "][" in discern:  # 解析参数
                self.list_AfterParsing = discern.split("][")
                discern = self.list_AfterParsing[-1]
                title_n=self.list_AfterParsing[0]
                className = self.list_AfterParsing[1]
                self.dlg_spec = self.win_one.child_window(title=title_n, class_name=className)
            else:
                print("传过来的控件唯一标识没有“][”，所有无法被转化成列表：",discern, __file__, sys._getframe().f_lineno)
                os._exit(0)
        else:
            print("没有唯一标识的操作方法", __file__, sys._getframe().f_lineno)
            os._exit(0)
        return  self.dlg_spec



    def ExpressionAssembly(self, str_Name):
        """
        组装表达式
        :param str_Name:
        :return:
        """
        print("控件的唯一标识:",str_Name)
        if str_Name=="Edit":
            self.dlg_spec=self.win_one.Edit
        elif str_Name=="Edit1":
            self.dlg_spec=self.win_one.Edit1
        elif str_Name=="Edit2":
            self.dlg_spec = self.win_one.Edit2
        elif str_Name=="Edit3":
            self.dlg_spec = self.win_one.Edit3
        elif str_Name=="Edit4":
            self.dlg_spec = self.win_one.Edit4
        elif str_Name=="Edit5":
            self.dlg_spec = self.win_one.Edit5
        elif str_Name=="Edit6":
            self.dlg_spec = self.win_one.Edit6
        elif str_Name=="Edit7":
            self.dlg_spec = self.win_one.Edit7
        elif str_Name=="Edit8":
            self.dlg_spec = self.win_one.Edit8
        elif str_Name=="Edit9":
            self.dlg_spec = self.win_one.Edit9
        elif str_Name=="Edit10":
            self.dlg_spec = self.win_one.Edit10
        elif str_Name=="Edit11":
            self.dlg_spec = self.win_one.Edit11
        elif str_Name=="Edit12":
            self.dlg_spec = self.win_one.Edit12
        elif str_Name=="Edit13":
            self.dlg_spec = self.win_one.Edit13
        elif str_Name == "Edit14":
            self.dlg_spec = self.win_one.Edit14
        elif str_Name == "Edit15":
            self.dlg_spec = self.win_one.Edit15
        elif str_Name == "Edit16":
            self.dlg_spec = self.win_one.Edit16
        elif str_Name == "CheckBox0":
            self.dlg_spec = self.win_one.CheckBox0
        elif str_Name == "CheckBox1":
            self.dlg_spec = self.win_one.CheckBox1
        elif str_Name == "CheckBox2":
            self.dlg_spec = self.win_one.CheckBox2
        elif str_Name == "CheckBox3":
            self.dlg_spec = self.win_one.CheckBox3
        elif str_Name == "CheckBox4":
            self.dlg_spec = self.win_one.CheckBox4
        elif str_Name == "CheckBox5":
            self.dlg_spec = self.win_one.CheckBox5
        elif str_Name == "CheckBox6":
            self.dlg_spec = self.win_one.CheckBox6
        elif str_Name == "CheckBox7":
            self.dlg_spec = self.win_one.CheckBox7
        elif str_Name == "CheckBox8":
            self.dlg_spec = self.win_one.CheckBox8
        elif str_Name == "CheckBox9":
            self.dlg_spec = self.win_one.CheckBox9
        elif str_Name == "CheckBox10":
            self.dlg_spec = self.win_one.CheckBox10
        elif str_Name == "CheckBox11":
            self.dlg_spec = self.win_one.CheckBox11
        elif str_Name == "CheckBox12":
            self.dlg_spec = self.win_one.CheckBox12
        elif str_Name == "CheckBox13":
            self.dlg_spec = self.win_one.CheckBox13
        elif str_Name == "CheckBox14":
            self.dlg_spec = self.win_one.CheckBox14
        elif str_Name == "CheckBox15":
            self.dlg_spec = self.win_one.CheckBox15
        elif str_Name == "CheckBox16":
            self.dlg_spec = self.win_one.CheckBox16
        elif str_Name == "Button":
            self.dlg_spec = self.win_one.Button
        elif str_Name == "Button0":
            self.dlg_spec = self.win_one.Button0
        elif str_Name == "Button1":
            self.dlg_spec = self.win_one.Button1
        elif str_Name == "Button2":
            self.dlg_spec = self.win_one.Button2
        elif str_Name == "Button3":
            self.dlg_spec = self.win_one.Button3
        elif str_Name == "Button4":
            self.dlg_spec = self.win_one.Button4
        elif str_Name == "Button5":
            self.dlg_spec = self.win_one.Button5
        elif str_Name == "Button6":
            self.dlg_spec = self.win_one.Button6
        elif str_Name == "Button7":
            self.dlg_spec = self.win_one.Button7
        elif str_Name == "Button8":
            self.dlg_spec = self.win_one.Button8
        elif str_Name == "Button9":
            self.dlg_spec = self.win_one.Button9
        elif str_Name == "Button10":
            self.dlg_spec = self.win_one.Button10
        elif str_Name == "Button11":
            self.dlg_spec = self.win_one.Button11
        elif str_Name == "RadioButton":
            self.dlg_spec = self.win_one.RadioButton
        elif str_Name == "RadioButton1":
            self.dlg_spec = self.win_one.RadioButton1
        elif str_Name == "RadioButton2":
            self.dlg_spec = self.win_one.RadioButton2
        elif str_Name == "RadioButton3":
            self.dlg_spec = self.win_one.RadioButton3
        elif str_Name == "RadioButton4":
            self.dlg_spec = self.win_one.RadioButton4
        elif str_Name == "RadioButton5":
            self.dlg_spec = self.win_one.RadioButton5
        elif str_Name == "RadioButton6":
            self.dlg_spec = self.win_one.RadioButton6
        elif str_Name == "RadioButton7":
            self.dlg_spec = self.win_one.RadioButton7
        elif str_Name == "RadioButton8":
            self.dlg_spec = self.win_one.RadioButton8
        elif str_Name == "RadioButton9":
            self.dlg_spec = self.win_one.RadioButton9
        elif str_Name == "RadioButton10":
            self.dlg_spec = self.win_one.RadioButton10
        elif str_Name == "RadioButton11":
            self.dlg_spec = self.win_one.RadioButton11
        elif str_Name == "RadioButton12":
            self.dlg_spec = self.win_one.RadioButton12
        elif str_Name == "RadioButton13":
            self.dlg_spec = self.win_one.RadioButton13
        elif str_Name == "RadioButton14":
            self.dlg_spec = self.win_one.RadioButton14
        elif str_Name == "ComboBox0":
            self.dlg_spec = self.win_one.ComboBox0
        elif str_Name == "ComboBox1":
            self.dlg_spec = self.win_one.ComboBox1
        elif str_Name == "ComboBox2":
            self.dlg_spec = self.win_one.ComboBox2
        elif str_Name == "ComboBox3":
            self.dlg_spec = self.win_one.ComboBox3
        elif str_Name == "ComboBox4":
            self.dlg_spec = self.win_one.ComboBox4
        elif str_Name == "ComboBox5":
            self.dlg_spec = self.win_one.ComboBox5
        elif str_Name == "GroupBox":
            self.dlg_spec = self.win_one.ComboBox
        elif str_Name == "GroupBox1":
            self.dlg_spec = self.win_one.ComboBox1
        elif str_Name == "GroupBox2":
            self.dlg_spec = self.win_one.ComboBox2
        elif str_Name == "GroupBox3":
            self.dlg_spec = self.win_one.GroupBox3
        elif str_Name == "Static3":
            self.dlg_spec = self.win_one.Static3
        elif str_Name == "Static6":
            self.dlg_spec = self.win_one.Static6
        elif str_Name == "Static15":
            self.dlg_spec = self.win_one.Static15
        elif str_Name == "路径Edit":
            self.dlg_spec = self.win_one.路径Edit
        elif str_Name == "两边各取蒙皮宽度一半":
            self.dlg_spec = self.win_one.两边各取蒙皮宽度一半
        elif str_Name == "极":
            self.dlg_spec = self.win_one.极
        elif str_Name == "均":
            self.dlg_spec = self.win_one.均
        elif str_Name == "机身半径Edit":
            self.dlg_spec = self.win_one.机身半径Edit
        else:
            print("没有找到唯一标识拼接方法:",str_Name)
            self.dlg_spec = self.win_one[str_Name]
        return self.dlg_spec



    def button_popUp(self, ControlProperties,location):
        """
       套件操作
       :param  ControlProperties: 控件的属性
       :param  location: 项目存放路径
       :return:
       """
        examine =None
        Popup_type = ControlProperties["套件类型一"]
        Popup_parameter = ControlProperties["套件参数一"]
        if "；" in Popup_parameter:
            self.list_AfterParsing = Popup_parameter.split("；")
        if Popup_type=="路径弹窗":  # 操作弹窗套件
            Popup_type2=ControlProperties["套件类型二"]
            Popup_parameter2 = ControlProperties["套件参数二"]
            ControlOperationSuite(None).SelectFile_Popover(self.list_AfterParsing,location,Popup_type2,Popup_parameter2,self.win_one)
        elif Popup_type == "选择材料许用值曲线":  # 操作弹窗套件
            str_coord = ControlProperties["唯一标识"]
            Check_winControl(Popup_parameter, self.win_one).window_WhetherOpen()  # 判断预期窗口是否出现
            ControlOperationSuite(None).select_AllowableCurve(str_coord)
        elif Popup_type == "选择校核工况" or Popup_type == "选择优化工况":  # 操作弹窗套件
            Check_winControl(Popup_type, self.win_one).window_WhetherOpen()  # 判断选择校核工况是否出现
            ControlOperationSuite(None).select_workingCondition(Popup_type)
        elif Popup_type == "选择结构单元":  # 操作弹窗套件
            time.sleep(0.3)
            self.win_one.click_input()
            KeyboardMouse().selectionModel()  # 选择结构单元
        else:
            print("被操作的套件名称不存在,套件名称为：",Popup_type, __file__, sys._getframe().f_lineno)
            os._exit(0)




    def coord_click_textbox(self,ControlProperties,argument):
        """
        坐标--文本框
        通过点击坐标位置显示文本框，然后输入内容
        选择材料许用值曲线
        :param argument: 在文本框输入的参数
        :param  ControlProperties: 控件属性
        :return:
        """
        discern = ControlProperties["唯一标识"]
        ControlTypes = ControlProperties["控件类型"]
        if ControlTypes=="坐标--单击--文本框":
            self.dlg_spec=OperatingControls(self.win_one).coord_dblclick(discern)
        elif ControlTypes=="坐标--三击--文本框":
            self.dlg_spec = OperatingControls(self.win_one).coord_Threeclick(discern)
        elif ControlTypes=="坐标--键盘--文本框":
            OperatingControls(self.win_one).coord_keyboardInput(discern,argument)
        else:
            print("没有找到操作方法：", ControlTypes, __file__, sys._getframe().f_lineno)
            os._exit(0)
        if ControlTypes !="坐标--键盘--文本框":
            Check_winControl(None, self.dlg_spec).Verify_inputBox(argument)



    def coord_dblclick_popUp(self,ControlProperties,argument):
        """
        根据坐标找到需要操作的控件，并且双击鼠标，操作套件
        :return:
        """
        discern = ControlProperties["唯一标识"]
        Popup_type =ControlProperties["套件类型一"]
        OperatingControls(self.win_one).coord_dblclick(discern)
        if Popup_type=="选择铺层库信息":
            ControlOperationSuite(None).select_Laminatedata(argument)
        else:
            print("没有弹窗类型：", Popup_type, __file__, sys._getframe().f_lineno)
            os._exit(0)




    def coord_dblclick(self,sole_logo):
        """
        根据坐标找到需要操作的控件，并且双击鼠标
        :return:
        """
        coord_X, coord_Y, sole = OperatingControls().analysis_coord(sole_logo)  # 解析参数
        dlg1_spec = OperatingControls(self.win_one).ExpressionAssembly(sole)
        self.win_one.double_click_input(coords=(coord_X, coord_Y), button="left")
        return dlg1_spec


    def coord_Threeclick(self,sole_logo):
        """
        根据坐标找到需要操作的控件，并且三击鼠标
        :return:
        """
        coord_X,coord_Y,sole = OperatingControls().analysis_coord(sole_logo)  # 解析参数
        dlg1_spec = OperatingControls(self.win_one).ExpressionAssembly(sole)
        self.win_one.click_input(coords=(coord_X, coord_Y), button="left")
        self.win_one.double_click_input(coords=(coord_X, coord_Y), button="left")
        return dlg1_spec



    def coord_keyboardInput(self, sole_logo,argument):
        """
        把鼠标移动到坐标位置，并点击，最后使用键盘输入
        :param sole_logo:
        :param argument:
        :return:
        """
        from pywinauto.keyboard import send_keys
        coord_X,coord_Y,sole = OperatingControls().analysis_coord(sole_logo)  # 解析参数
        dlg1_spec = OperatingControls(self.win_one).ExpressionAssembly(sole)
        dlg1_spec.click_input(coords=(coord_X, coord_Y), button="left")
        time.sleep(1)
        argument=str(argument)
        # 使用键盘向文本框中输入数据
        send_keys(argument)  # 使用键盘强制输入数据


    def analysis_coord(self,sole_logo):
        """
        移动坐标到指定的位置
        :return:
        """
        if "；" in sole_logo:
            self.list_AfterParsing = sole_logo.split("；")
        else:
            print("唯一标识不能解析出坐标：", sole_logo, __file__, sys._getframe().f_lineno)
            os._exit(0)
        coord_X = int(self.list_AfterParsing[0])
        coord_Y = int(self.list_AfterParsing[1])
        sole = self.list_AfterParsing[2]
        return coord_X,coord_Y,sole


    def scrollMouse(self):
        """
        滚动鼠标
        :return:
        """
        self.win_one.click_input()
        import win32api, win32con
        win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, -1000)  # 滚动鼠标