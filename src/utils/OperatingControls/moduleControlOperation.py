# 铺层库优化工作栏，对应Aerobook路径：铺层信息--》铺层库优化
import time,sys, os
from src.utils.otherMethods.controlOperationSuite import ControlOperationSuite
from tool import KeyboardMouse,Check_winControl



class OperatingControls:
    """操作控件"""




    def __init__(self,window_one,window_two=None,window_three =None):
        self.window_one=window_one
        self.window_two = window_two
        self.window_three = window_three
        self.dlg_spec=None


    def controlConsole(self,Silverlight,argument ):
        """
        操作控件控制台
        :param Silverlight: 控件的存在方法
        :param argument: 控件的存在参数
        :return:
        """
        print("\033[0;34m 《进入操作控件函数开始操作控件》")
        location = argument["被测程序文件地址"]
        els = argument["其他"]
        for ControlsName, ControlProperties in Silverlight.items():  # 循环取出控件
            operational = argument[ControlsName]
            if operational != "默认":  # 当控件不等于默认（默认代表不用操作控件）
                ControlTypes = ControlProperties["控件类型"]
                ControlInstance = ControlProperties["所操作实例"]
                Controlmethod = ControlProperties["唯一标识方法"]
                discern = ControlProperties["唯一标识"]
                waitingTime = ControlProperties["操作控件后等待时间"]
                whetherpopup = ControlProperties["是否有弹窗出现"]
                WindowInstance = OperatingControls(self.window_one, self.window_two, self.window_three). \
                    OperationControlInstance(ControlInstance)  # 获取操作控件实例
                dlg_spec = OperatingControls(WindowInstance). \
                    IdentificationMethod(Controlmethod, discern)  # 获取操作控件实例
                if ControlTypes == "文本框":  # 当控件是文本框的时候
                    if els == "拼接路径":  # 如果是路径文本框，就判断需不需要拼接路径
                        operational = location + operational
                    Check_winControl(None, dlg_spec).Verify_inputBox(operational)
                    print("在控件”%r“文本框中输入：%r" % (ControlsName, operational))
                elif ControlTypes == "勾选框" or ControlTypes == "单选框":
                    Check_winControl(None, dlg_spec).Verify_CheckBox_Status()
                    print("控件”%r“成功勾选" % ControlsName)
                elif ControlTypes == "按钮" and whetherpopup == "否":
                    dlg_spec.click()
                    print("控件”%r“按钮点击成功" % ControlsName)
                elif ControlTypes == "按钮" and whetherpopup == "是":  # 操作套件
                    OperatingControls(dlg_spec).button_popUp(operational, location, operational)
                    PopupTitle = operational["弹窗标题"]
                    print("控件”%r“按钮点击后，成功弹出“%r”弹窗" % (ControlsName, PopupTitle))
                elif ControlTypes == "坐标--文本框":
                    OperatingControls(WindowInstance).Coordinate_Textbox(operational, discern)
                    print("控件”%r“坐标选择正确，并且在文本框中正确输入数据" % ControlsName)
                elif ControlTypes == "坐标--点击":
                    pass
                elif ControlTypes == "下拉框":
                    Check_winControl(None, dlg_spec).Verify_dropDownBox(operational)
                    print("控件”%r“下拉框选择成功选择数据" % ControlsName)
                else:
                    print("说明控件属性", __file__, sys._getframe().f_lineno)
                    os._exit(0)
                time.sleep(waitingTime)
            else:
                print("不操作控件“%r”：%r" % (ControlsName,operational))
        print("控件操作完成 \033[0m")
        print(" ")





    def OperationControlInstance(self,ControlInstance):
        """
        获取操作控件的窗口
        :return:
        """
        if ControlInstance=="窗口一":
            if self.window_one:
                return  self.window_one
            else:
                print("传过来的实例为空", __file__, sys._getframe().f_lineno)
                os._exit(0)
        elif ControlInstance=="窗口二":
            if self.window_two:
                return self.window_two
            else:
                print("传过来的实例为空", __file__, sys._getframe().f_lineno)
                os._exit(0)
        elif ControlInstance=="窗口三":
            if self.window_three:
                return self.window_three
            else:
                print("传过来的实例为空", __file__, sys._getframe().f_lineno)
                os._exit(0)
        else:
            if self.window_one:
                return self.window_one
            else:
                print("传过来的实例为空", __file__, sys._getframe().f_lineno)
                os._exit(0)



    def IdentificationMethod(self,Controlmethod,discern):
        """
        因为从电子表格获取的控件标识字符串，拼接在操作控件的时候会报错，暂时还没有找到原因，暂时使用该方法拼接操作方法
        :return:
        """
        if Controlmethod=="方式一":
           self.dlg_spec= OperatingControls(self.window_one).ExpressionAssembly(discern)
           Check_winControl("警告", "OK").popUp_Whether_close()
        elif Controlmethod=="方式二":
            list1=discern.split("；")
            self.dlg_spec = self.window_one.child_window(title=list1[0], class_name=list1[1])
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
        if str_Name=="Edit":
            self.dlg_spec=self.window_one.Edit
        elif str_Name=="Edit2":
            self.dlg_spec = self.window_one.Edit2
        elif str_Name=="Edit3":
            self.dlg_spec = self.window_one.Edit3
        elif str_Name=="Edit4":
            self.dlg_spec = self.window_one.Edit4
        elif str_Name=="Edit5":
            self.dlg_spec = self.window_one.Edit5
        elif str_Name=="Edit6":
            self.dlg_spec = self.window_one.Edit6
        elif str_Name=="Edit7":
            self.dlg_spec = self.window_one.Edit7
        elif str_Name=="Edit8":
            self.dlg_spec = self.window_one.Edit8
        elif str_Name=="Edit9":
            self.dlg_spec = self.window_one.Edit9
        elif str_Name=="Edit10":
            self.dlg_spec = self.window_one.Edit10
        elif str_Name=="Edit11":
            self.dlg_spec = self.window_one.Edit11
        elif str_Name=="Edit12":
            self.dlg_spec = self.window_one.Edit12
        elif str_Name=="Edit13":
            self.dlg_spec = self.window_one.Edit13
        elif str_Name == "Edit14":
            self.dlg_spec = self.window_one.Edit14
        elif str_Name == "Edit15":
            self.dlg_spec = self.window_one.Edit15
        elif str_Name == "Edit16":
            self.dlg_spec = self.window_one.Edit16
        elif str_Name == "CheckBox0":
            self.dlg_spec = self.window_one.CheckBox0
        elif str_Name == "CheckBox1":
            self.dlg_spec = self.window_one.CheckBox1
        elif str_Name == "CheckBox2":
            self.dlg_spec = self.window_one.CheckBox2
        elif str_Name == "CheckBox3":
            self.dlg_spec = self.window_one.CheckBox3
        elif str_Name == "CheckBox4":
            self.dlg_spec = self.window_one.CheckBox4
        elif str_Name == "CheckBox5":
            self.dlg_spec = self.window_one.CheckBox5
        elif str_Name == "CheckBox6":
            self.dlg_spec = self.window_one.CheckBox6
        elif str_Name == "CheckBox7":
            self.dlg_spec = self.window_one.CheckBox7
        elif str_Name == "CheckBox8":
            self.dlg_spec = self.window_one.CheckBox8
        elif str_Name == "CheckBox9":
            self.dlg_spec = self.window_one.CheckBox9
        elif str_Name == "CheckBox10":
            self.dlg_spec = self.window_one.CheckBox10
        elif str_Name == "CheckBox11":
            self.dlg_spec = self.window_one.CheckBox11
        elif str_Name == "CheckBox12":
            self.dlg_spec = self.window_one.CheckBox12
        elif str_Name == "CheckBox13":
            self.dlg_spec = self.window_one.CheckBox13
        elif str_Name == "CheckBox14":
            self.dlg_spec = self.window_one.CheckBox14
        elif str_Name == "CheckBox15":
            self.dlg_spec = self.window_one.CheckBox15
        elif str_Name == "CheckBox16":
            self.dlg_spec = self.window_one.CheckBox16
        elif str_Name == "Button":
            self.dlg_spec = self.window_one.Button
        elif str_Name == "Button0":
            self.dlg_spec = self.window_one.Button0
        elif str_Name == "Button1":
            self.dlg_spec = self.window_one.Button1
        elif str_Name == "Button2":
            self.dlg_spec = self.window_one.Button2
        elif str_Name == "Button3":
            self.dlg_spec = self.window_one.Button3
        elif str_Name == "Button4":
            self.dlg_spec = self.window_one.Button4
        elif str_Name == "Button5":
            self.dlg_spec = self.window_one.Button5
        elif str_Name == "Button6":
            self.dlg_spec = self.window_one.Button6
        elif str_Name == "Button7":
            self.dlg_spec = self.window_one.Button7
        elif str_Name == "Button8":
            self.dlg_spec = self.window_one.Button8
        elif str_Name == "Button9":
            self.dlg_spec = self.window_one.Button9
        elif str_Name == "Button10":
            self.dlg_spec = self.window_one.Button10
        elif str_Name == "Button11":
            self.dlg_spec = self.window_one.Button11
        elif str_Name == "RadioButton":
            self.dlg_spec = self.window_one.RadioButton
        elif str_Name == "RadioButton1":
            self.dlg_spec = self.window_one.RadioButton1
        elif str_Name == "RadioButton2":
            self.dlg_spec = self.window_one.RadioButton2
        elif str_Name == "RadioButton3":
            self.dlg_spec = self.window_one.RadioButton3
        elif str_Name == "RadioButton4":
            self.dlg_spec = self.window_one.RadioButton4
        elif str_Name == "RadioButton5":
            self.dlg_spec = self.window_one.RadioButton5
        elif str_Name == "RadioButton6":
            self.dlg_spec = self.window_one.RadioButton6
        elif str_Name == "RadioButton7":
            self.dlg_spec = self.window_one.RadioButton7
        elif str_Name == "RadioButton8":
            self.dlg_spec = self.window_one.RadioButton8
        elif str_Name == "RadioButton9":
            self.dlg_spec = self.window_one.RadioButton9
        elif str_Name == "RadioButton10":
            self.dlg_spec = self.window_one.RadioButton10
        elif str_Name == "RadioButton11":
            self.dlg_spec = self.window_one.RadioButton11
        elif str_Name == "ComboBox0":
            self.dlg_spec = self.window_one.ComboBox0
        elif str_Name == "ComboBox1":
            self.dlg_spec = self.window_one.ComboBox1
        elif str_Name == "ComboBox2":
            self.dlg_spec = self.window_one.ComboBox2
        elif str_Name == "ComboBox3":
            self.dlg_spec = self.window_one.ComboBox3
        elif str_Name == "ComboBox4":
            self.dlg_spec = self.window_one.ComboBox4
        elif str_Name == "ComboBox5":
            self.dlg_spec = self.window_one.ComboBox5
        elif str_Name == "路径Edit":
            self.dlg_spec = self.window_one.路径Edit
        elif str_Name == "两边各取蒙皮宽度一半":
            self.dlg_spec = self.window_one.两边各取蒙皮宽度一半
        elif str_Name == "极":
            self.dlg_spec = self.window_one.极
        elif str_Name == "均":
            self.dlg_spec = self.window_one.均
        elif str_Name == "机身半径Edit":
            self.dlg_spec = self.window_one.机身半径Edit
        else:
            print("str_Name:",str_Name)
            self.dlg_spec = self.window_one[str_Name]
        return self.dlg_spec



    def button_popUp(self, properties,location, valu):
        """
       套件操作
       :param  properties: 控件的属性
       :param  location: 项目存放路径
       :param  valu: 项目存放路径
       :return:
       """
        nestWin_Dicti ={}
        examine =None
        Popuptype = properties["弹窗类型"]
        if Popuptype=="路径弹窗":  # 操作弹窗套件
            PopupTitle = properties["弹窗标题"]
            nestPopup = properties["是否有嵌套弹窗"]
            Check_winControl(PopupTitle, self.window_one).window_WhetherOpen()  # 判断预期窗口是否出现
            closeName = properties["关闭弹窗按钮名称"]
            filename = properties["弹窗中输入文件名"]
            # 判断有没有嵌套弹窗
            if nestPopup=="是":
                examine= "检查"
                nest_PopupTitle = properties["嵌套弹窗标题"]
                nest_closeName = properties["嵌套弹窗关闭按钮名称"]
                nestWin_Dicti = {"嵌套窗口标题": nest_PopupTitle, "嵌套控件名称": nest_closeName }
            parWin1_Dicti = {"窗口标题": PopupTitle, "关闭窗口控件名称": closeName, "地址": location, "文件夹输入内容": filename}
            ControlOperationSuite(None).SelectFile_Popover(parWin1_Dicti, examine, nestWin_Dicti)
        elif Popuptype == "选择材料许用值曲线":  # 操作弹窗套件
            PopupTitle = properties["弹窗标题"]
            Check_winControl(PopupTitle, self.window_one).window_WhetherOpen()  # 判断预期窗口是否出现
            ControlOperationSuite(None).select_AllowableCurve(valu)
        elif Popuptype == "选择校核工况":  # 操作弹窗套件
            Check_winControl("选择校核工况", self.window_one).window_WhetherOpen()  # 判断选择校核工况是否出现
            ControlOperationSuite(None).select_workingCondition()
        elif Popuptype == "选择结构单元":  # 操作弹窗套件
            time.sleep(0.3)
            self.window_one.click()
            KeyboardMouse().selectionModel()  # 选择结构单元
        else:
            print("被操作的套件名称不存在,套件名称为：",Popuptype, __file__, sys._getframe().f_lineno)
            os._exit(0)


    def Coordinate_Textbox(self, list_argument,discern):
        """
        坐标--文本框
        通过点击坐标位置显示文本框，然后输入内容
        选择材料许用值曲线
        :return:
        """
        # 解析参数
        list_AfterParsing=list_argument.split("；")
        print("list_AfterParsing:",list_AfterParsing)
        coord_X=int(list_AfterParsing[0])
        print("coord_X:", coord_X)
        coord_Y = int(list_AfterParsing[1])
        print("coord_Y:",  coord_Y)
        valu=list_AfterParsing[2]
        dlg1_spec = OperatingControls(self.window_one).ExpressionAssembly(discern)
        self.window_one.double_click_input(coords=(coord_X, coord_Y), button="left")
        Check_winControl(None, dlg1_spec).Verify_inputBox(valu)











