# 铺层库优化工作栏，对应Aerobook路径：铺层信息--》铺层库优化
import time
from src.utils.otherMethods.controlOperationSuite import ControlOperationSuite
from tool import instrument,KeyboardMouse,Check_winControl
import sys, os


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
        print("进入操作控件函数")
        location = argument["被测程序文件地址"]
        els = argument["其他"]
        for k1,v1 in Silverlight.items():   # 取出被操作控件的名称
            for k2,v2 in argument.items():  # 取出被操作控件的名称
                if k1 == k2:
                    # 当两个名称相等的时候
                    if v2 !="默认" :   # 当控件不等于默认（默认代表不用操作控件）
                        ControlTypes =v1["控件类型"]
                        ControlInstance = v1["所操作实例"]
                        Controlmethod = v1["唯一标识方法"]
                        discern = v1["唯一标识"]
                        waitingTime = v1["操作控件后等待时间"]
                        whetherpopup = v1["是否有弹窗出现"]
                        WindowInstance=OperatingControls(self.window_one,self.window_two,self.window_three).\
                            OperationControlInstance(ControlInstance)  # 获取操作控件实例
                        dlg_spec = OperatingControls(WindowInstance).IdentificationMethod(Controlmethod,discern)  # 获取操作控件实例
                        if ControlTypes=="文本框":   # 当控件是文本框的时候
                            if els == "拼接路径":   # 如果是路径文本框，就判断需不需要拼接路径
                                v2=location+v2
                            Check_winControl(None, dlg_spec).Verify_inputBox(v2)
                        elif ControlTypes=="勾选框" or ControlTypes=="单选框":
                            Check_winControl(None, dlg_spec).Verify_CheckBox_Status()
                        elif ControlTypes == "按钮" and whetherpopup=="否":
                            print("开始点击”%r“按钮"%k1)
                            dlg_spec.check()
                            dlg_spec.click()
                        elif ControlTypes == "按钮" and whetherpopup=="是"  :  # 操作套件
                            OperatingControls(dlg_spec).button_popUp(v1,location,v2)
                        elif  ControlTypes == "坐标--文本框":
                            OperatingControls(dlg_spec).Coordinate_Textbox(v2,discern)
                        elif ControlTypes == "坐标--点击":
                            pass
                        elif ControlTypes == "下拉框":
                            Check_winControl(None, dlg_spec).Verify_dropDownBox(v2)
                        else:
                            print("说明控件属性", __file__, sys._getframe().f_lineno)
                            os._exit(0)
                        time.sleep(waitingTime)



    def OperationControlInstance(self,ControlInstance):
        """
        获取操作控件的实例
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
        唯一标识的操作方法
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
        print("str_Name:",str_Name)
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
        coord_Y = int(list_AfterParsing[1])
        valu=list_AfterParsing[2]
        dlg1_spec = OperatingControls(self.window_one).ExpressionAssembly(discern)
        self.window_one.double_click_input(coords=(coord_X, coord_Y), button="left")
        Check_winControl(None, dlg1_spec).Verify_inputBox(valu)



class ModuleControlOperation():
    """工作栏控件操作"""

    def __init__(self,dlg_spec):
        """
        :param dlg_spec:
        """
        self.dlg_spec=dlg_spec


    def editAllowable_operation(self,dicti):
        """
        材料信息--定义复合材料参数
        :return:
        """
        param1 = dicti["编辑材料许用值-创建材料许用值按钮"]
        param2 = dicti["编辑材料许用值关闭按钮"]
        # self.dlg_spec.print_control_identifiers()
        if param1 != "默认":
           time.sleep(0.1)
           # 在编辑材料许用值窗口中点击“创建材料许用值按”钮
           dlg1_spec=self.dlg_spec.child_window(title="创建材料许用值曲线", class_name="Button")
           # 检查点击按钮后，弹窗是否出现
           Check_winControl("编辑材料许用值曲线", dlg1_spec).window_WhetherOpen()  # 判断预期窗口是否出现
        if param2 != "默认":
            time.sleep(0.1)
            # 在编辑材料许用值窗口中点击“创建材料许用值按”钮
            self.dlg_spec.关闭.click()



    def editAllowable_CurvePopupWin_operation(self,dicti):
        """
        载荷信息--编辑工况
        :return:
        """
        param1 = dicti["曲线名称文本框"]
        param2 = dicti["曲线坐标文本框，第一横行X竖行"]
        param3 = dicti["曲线坐标文本框，第一横行Y竖行"]
        param4 = dicti["曲线坐标文本框，第二横行X竖行"]
        param5 = dicti["曲线坐标文本框，第二横行Y竖行"]
        param6 = dicti["曲线坐标文本框，第三横行X竖行"]
        param7 = dicti["曲线坐标文本框，第三横行Y竖行"]
        param8 = dicti["曲线坐标文本框，第四横行X竖行"]
        param9 = dicti["曲线坐标文本框，第四横行Y竖行"]
        param10 = dicti["编辑材料许用值曲线确认按钮"]
        param11 = dicti["编辑材料许用值曲线关闭按钮"]
        # 切换到网格窗口中
        dlg_spec = self.dlg_spec.child_window(title="GridWindow", class_name="wxWindowNR")
        # self.dlg_spec.print_control_identifiers()
        if param1 != "默认":
           time.sleep(0.1)
           # 向曲线名称文本框中输入数据
           self.dlg_spec.Edit2.set_text(param1)
        if param2 != "默认":
            time.sleep(0.1)
            # 曲线坐标文本框，第一横行X竖行
            dlg_spec.double_click_input(coords = (40, 20),button ="left")
            dlg_spec.Edit.set_text(param2)
        if param3 != "默认" :
            time.sleep(0.1)
            # 曲线坐标文本框，第一横行Y竖行
            dlg_spec.double_click_input(coords=(180, 20), button="left")
            dlg_spec.Edit.set_text(param3)
        if param4 != "默认" :
            time.sleep(0.1)
            # 曲线坐标文本框，第二横行X竖行
            dlg_spec.double_click_input(coords = (40, 40),button ="left")
            dlg_spec.Edit.set_text(param4)
        if param5 != "默认":
            time.sleep(0.5)
            # 曲线坐标文本框，第二横行Y竖行
            dlg_spec.double_click_input(coords = (180, 40),button ="left")
            dlg_spec.Edit.set_text(param5)
        if param6 != "默认":
            time.sleep(0.1)
            # 曲线坐标文本框，第三横行X竖行
            dlg_spec.click_input(coords = (40, 60),double = True)
            dlg_spec.Edit.set_text(param6)
        if param7 != "默认":
            time.sleep(0.1)
            # 曲线坐标文本框，第三横行Y竖行
            dlg_spec.double_click_input(coords = (180, 60),button ="left")
            dlg_spec.Edit.set_text(param7)
        if param8 != "默认":
            time.sleep(0.1)
            # 曲线坐标文本框，第四横行X竖行
            dlg_spec.double_click_input(coords=(40, 80), button="left")
            dlg_spec.Edit.set_text(param8)
        if param9 != "默认":
            time.sleep(0.1)
            # 曲线坐标文本框，第四横行Y竖行
            dlg_spec.double_click_input(coords=(180, 80), button="left")
            dlg_spec.Edit.set_text(param9)
        if param10 != "默认":
            time.sleep(0.5)
            # 编辑材料许用值曲线确认按钮
            Check_winControl("编辑材料许用值曲线", "确认").popUp_Whether_close()
        if param11 != "默认":
            time.sleep(0.1)
            # 编辑材料许用值曲线关闭按钮
            self.dlg_spec.关闭.click()






    def CompoundStrengthCheck_2D_operation(self,testdicts,work_window):
        """
        操作复合强度校核--》二维单元工作栏内的控件
        :return:
        """
        param1  = testdicts["2D静强度勾选框"]
        param2  = testdicts["VonMises勾选框"]
        param3  = testdicts["P1“major”勾选框"]
        param4  = testdicts["P3“minor”勾选框"]
        param5  = testdicts["X向勾选框"]
        param6  = testdicts["Y向勾选框"]
        param7  = testdicts["XY向勾选框"]
        param8  = testdicts["耦合应变勾选框"]
        param9  = testdicts["简支压缩勾选框"]
        param10 = testdicts["简支剪切勾选框"]
        param11 = testdicts["弯剪复合失稳勾选框"]
        param12 = testdicts["压剪复合失稳“单轴压”勾选框"]
        param13 = testdicts["简支压缩“双轴压”勾选框"]
        param14 = testdicts["压剪复合失稳“双轴压”勾选框"]
        param15 = testdicts["曲板勾选框"]
        param16 = testdicts["机身半径文本框"]
        param17 = testdicts["机身蒙皮单选框"]
        param18 = testdicts["翼盒蒙皮单选框"]
        param19 = testdicts["梁腹板单选框"]
        param20 = testdicts["其他单选框"]
        param21 = testdicts["B值减缩系数文本框"]
        param22 = testdicts["坐标系下拉框"]
        param23 = testdicts["参考方向下拉框"]
        param24 = testdicts["宽度修正系数下拉框"]
        param25 = testdicts["宽度修正系数对应的文本框"]
        param26 = testdicts["蒙皮计算宽度方法一单选框"]
        param27 = testdicts["蒙皮计算宽度方法二单选框"]
        param28 = testdicts["蒙皮计算宽度方法三单选框"]
        param29 = testdicts["载荷类型单选框均值"]
        param30 = testdicts["载荷类型单选框极值"]
        param31 = testdicts["选择校核工况按钮"]
        param32 = testdicts["选择结构单元"]
        param33 = testdicts["校核按钮"]
        param34 = testdicts["关闭按钮"]
        if param1 != "默认":
            time.sleep(0.1)
            # 2D静强度勾选框
            dlg1_spec=self.dlg_spec.CheckBox0
            Check_winControl(None,dlg1_spec).Verify_CheckBox_Status()
        if param2 != "默认" and param1 != "默认":
            time.sleep(0.1)
            # VonMises勾选框
            dlg2_spec = self.dlg_spec.CheckBox2
            Check_winControl(None,dlg2_spec).Verify_CheckBox_Status()
        if param3 != "默认" and param1 != "默认":
            time.sleep(0.1)
            # P1(major)勾选框
            dlg3_spec = self.dlg_spec.CheckBox3
            Check_winControl(None, dlg3_spec).Verify_CheckBox_Status()
        if param4 != "默认" and param1 != "默认":
            time.sleep(0.1)
            # P3(minor)勾选框
            dlg4_spec = self.dlg_spec.CheckBox4
            Check_winControl(None, dlg4_spec).Verify_CheckBox_Status()
        if param5 != "默认" and param1 != "默认":
            time.sleep(0.1)
            # X向勾选框
            dlg5_spec = self.dlg_spec.CheckBox5
            Check_winControl(None, dlg5_spec).Verify_CheckBox_Status()
        if param6 != "默认"and param1 != "默认":
            time.sleep(0.1)
            # Y向勾选框
            dlg6_spec = self.dlg_spec.CheckBox6
            Check_winControl(None, dlg6_spec).Verify_CheckBox_Status()
        if param7 != "默认"  and param1 != "默认":
            time.sleep(0.1)
            # XY向勾选框
            dlg7_spec = self.dlg_spec.CheckBox7
            Check_winControl(None, dlg7_spec).Verify_CheckBox_Status()
        if param8 != "默认"  and param1 != "默认":
            time.sleep(0.1)
            # 耦合应变勾选框
            dlg8_spec = self.dlg_spec.CheckBox8
            Check_winControl(None, dlg8_spec).Verify_CheckBox_Status()
        if param9 != "默认" and param1 != "默认":
            time.sleep(0.1)
            # 简支压缩勾选框
            dlg8_spec = self.dlg_spec.CheckBox9
            Check_winControl(None, dlg8_spec).Verify_CheckBox_Status()
        if param10 != "默认":
            time.sleep(0.1)
            # 简支剪切勾选框
            dlg8_spec = self.dlg_spec.CheckBox10
            Check_winControl(None, dlg8_spec).Verify_CheckBox_Status()
        if param11 != "默认":
            time.sleep(0.1)
            # 弯剪复合失稳勾选框
            dlg8_spec = self.dlg_spec.CheckBox11
            Check_winControl(None, dlg8_spec).Verify_CheckBox_Status()
        if param12 != "默认":
            time.sleep(0.1)
            # 压剪复合失稳（单轴压）勾选框
            dlg8_spec = self.dlg_spec.CheckBox12
            Check_winControl(None, dlg8_spec).Verify_CheckBox_Status()
        if param13 != "默认":
            time.sleep(0.1)
            # 简支压缩（双轴压）勾选框
            dlg8_spec = self.dlg_spec.CheckBox13
            Check_winControl(None, dlg8_spec).Verify_CheckBox_Status()
        if param14 != "默认":
            time.sleep(0.1)
            # 压剪复合失稳（双轴压）勾选框
            dlg8_spec = self.dlg_spec.CheckBox14
            Check_winControl(None, dlg8_spec).Verify_CheckBox_Status()
        if param15 != "默认":
            time.sleep(0.1)
            # 曲板勾选框
            dlg8_spec = self.dlg_spec.CheckBox15
            Check_winControl(None, dlg8_spec).Verify_CheckBox_Status()
        if param16 != "默认":
            time.sleep(0.1)
            # 机身半径文本框
            dlg8_spec = self.dlg_spec.机身半径Edit
            Check_winControl(None, dlg8_spec).Verify_inputBox(param16)
        if param17 != "默认":
            time.sleep(0.1)
            # 机身蒙皮单选框
            dlg8_spec = self.dlg_spec.RadioButton1
            Check_winControl(None, dlg8_spec).Verify_CheckBox_Status()
        if param18 != "默认":
            time.sleep(0.1)
            # 翼盒蒙皮单选框
            dlg8_spec = self.dlg_spec.RadioButton2
            Check_winControl(None, dlg8_spec).Verify_CheckBox_Status()
        if param19 != "默认":
            time.sleep(0.1)
            # 梁腹板单选框
            dlg8_spec = self.dlg_spec.RadioButton3
            Check_winControl(None, dlg8_spec).Verify_CheckBox_Status()
        if param20 != "默认":
            time.sleep(0.1)
            # 其他单选框
            dlg8_spec = self.dlg_spec.RadioButton4
            Check_winControl(None, dlg8_spec).Verify_CheckBox_Status()
        if param21 != "默认":
            time.sleep(0.1)
            # B值减缩系数文本框
            dlg8_spec = self.dlg_spec.B值减缩系数Edit
            Check_winControl(None, dlg8_spec).Verify_inputBox( param21)
        if param22 != "默认":
            time.sleep(0.1)
            # 坐标系下拉框
            dlg8_spec = self.dlg_spec.ComboBox0
            Check_winControl(None, dlg8_spec).Verify_dropDownBox(param22)
        if param23 != "默认":
            time.sleep(0.1)
            # 参考方向下拉框
            dlg8_spec = self.dlg_spec.ComboBox2
            Check_winControl(None, dlg8_spec).Verify_dropDownBox(param23)
        if param24 != "默认":
            time.sleep(0.1)
            # 宽度修正系数下拉框
            dlg8_spec = self.dlg_spec.ComboBox3
            Check_winControl(None, dlg8_spec).Verify_dropDownBox(param24)
        if param25 != "默认":
            time.sleep(0.1)
            # 宽度修正系数对应的文本框
            dlg8_spec = self.dlg_spec.Edit3
            Check_winControl(None, dlg8_spec).Verify_inputBox(param25)
        if param26 != "默认":
            time.sleep(0.1)
            # 蒙皮计算宽度方法一单选框
            dlg8_spec = self.dlg_spec.RadioButton6
            Check_winControl(None, dlg8_spec).Verify_CheckBox_Status()
        if param27 != "默认":
            time.sleep(0.1)
            # 蒙皮计算宽度方法二单选框
            dlg8_spec = self.dlg_spec.RadioButton7
            Check_winControl(None, dlg8_spec).Verify_CheckBox_Status()
        if param28 != "默认":
            time.sleep(0.1)
            # 蒙皮计算宽度方法三单选框
            dlg8_spec = self.dlg_spec.RadioButton8
            Check_winControl(None, dlg8_spec).Verify_CheckBox_Status()
        if param29 != "默认":
            time.sleep(0.1)
            # 载荷类型单选框均值
            dlg8_spec = self.dlg_spec.RadioButton9
            Check_winControl(None, dlg8_spec).Verify_CheckBox_Status()
        if param30 != "默认":
            time.sleep(0.1)
            # 载荷类型单选框极值
            dlg8_spec = self.dlg_spec.child_window(title="极  值", class_name="Button")
            Check_winControl(None, dlg8_spec).Verify_CheckBox_Status()
        if param31 != "默认":
            time.sleep(0.1)
            # 选择校核工况按钮
            dlg8_spec = work_window.child_window(title="...", class_name="Button")
            Check_winControl("选择校核工况", dlg8_spec).window_WhetherOpen()  # 判断预期窗口是否出现
            ControlOperationSuite(None).select_workingCondition()  # 选择组合工况
        if param32 != "默认":
            # 选择结构单元
            work_window.child_window(title="选择结构单元", class_name="Button").click()  # 点击“选择结构单元按钮”按钮
            time.sleep(0.3)
            KeyboardMouse().selectionModel()  # 选择结构单元
        if param33 != "默认":
            time.sleep(0.1)
            # 校核按钮
            work_window.校核Button.click()
            time.sleep(5)
        if param34 != "默认":
            time.sleep(0.1)
            # 关闭按钮
            work_window.关闭.click()



    def CompoundStrengthCheck_1D_operation(self,testdicts,work_window):
        """
        操作复合强度校核--》二维单元工作栏内的控件
        :return:
        """
        param1  = testdicts["1D静强度勾选框"]
        param2  = testdicts["局部失稳勾选框"]
        param3  = testdicts["压损勾选框"]
        param4  = testdicts["加筋板柱屈曲勾选框"]
        param5  = testdicts["两边各取蒙皮宽度一半单选框"]
        param6  = testdicts["两边各取15倍蒙皮厚度单选框"]
        param7  = testdicts["端部支持系数文本框"]
        param8  = testdicts["刚度比勾选框"]
        param9  = testdicts["上限文本框"]
        param10 = testdicts["下限文本框"]
        param11 = testdicts["B值减缩系数文本框"]
        param12 = testdicts["载荷类型单选框均值"]
        param13 = testdicts["载荷类型单选框极值"]
        param14 = testdicts["选择校核工况按钮"]
        param15 = testdicts["选择结构单元"]
        param16 = testdicts["校核按钮"]
        param17 = testdicts["关闭按钮"]
        if param1 != "默认":
            time.sleep(0.1)
            # 1D静强度勾选框
            dlg1_spec=self.dlg_spec.CheckBox0
            Check_winControl(None, dlg1_spec).Verify_CheckBox_Status()
        if param2 != "默认":
            time.sleep(0.1)
            # 局部失稳勾选框
            dlg2_spec = self.dlg_spec.CheckBox2
            Check_winControl(None, dlg2_spec).Verify_CheckBox_Status()
        if param3 != "默认":
            time.sleep(0.1)
            # 压损勾选框
            dlg3_spec = self.dlg_spec.CheckBox3
            Check_winControl(None, dlg3_spec).Verify_CheckBox_Status()
        if param4 != "默认" :
            time.sleep(0.1)
            # 加筋板柱屈曲勾选框
            dlg4_spec = self.dlg_spec.CheckBox4
            Check_winControl(None, dlg4_spec).Verify_CheckBox_Status()
        if param5 != "默认" and param4 != "默认":
            time.sleep(0.1)
            # 两边各取蒙皮宽度一半单选框
            dlg5_spec = self.dlg_spec.child_window(title="两边各取蒙皮宽度一半    ", class_name="Button")
            Check_winControl(None, dlg5_spec).Verify_CheckBox_Status()
        if param6 != "默认"and param4 != "默认":
            time.sleep(0.1)
            # 两边各取15倍蒙皮厚度单选框
            dlg6_spec = self.dlg_spec.RadioButton5
            Check_winControl(None, dlg6_spec).Verify_CheckBox_Status()
        if param7 != "默认"  and param4 != "默认":
            time.sleep(0.1)
            # 端部支持系数文本框
            dlg8_spec = self.dlg_spec.Edit0
            Check_winControl(None, dlg8_spec).Verify_inputBox(param7)
        if param8 != "默认":
            time.sleep(0.1)
            # 刚度比勾选框
            dlg8_spec = self.dlg_spec.CheckBox5
            Check_winControl(None, dlg8_spec).Verify_CheckBox_Status()
        if param9 != "默认" and param1 != "默认":
            time.sleep(0.1)
            # 上限文本框
            dlg8_spec = self.dlg_spec.Edit2
            Check_winControl(None, dlg8_spec).Verify_inputBox(param9)
        if param10 != "默认":
            time.sleep(0.1)
            # 下限文本框
            dlg8_spec = self.dlg_spec.Edit3
            Check_winControl(None, dlg8_spec).Verify_inputBox(param10)
        if param11 != "默认":
            time.sleep(0.1)
            # B值减缩系数文本框
            dlg8_spec = self.dlg_spec.Edit4
            Check_winControl(None, dlg8_spec).Verify_inputBox(param11)
        if param12 != "默认":
            time.sleep(0.1)
            # 载荷类型单选框均值
            dlg8_spec = self.dlg_spec.child_window(title="均  值", class_name="Button")
            Check_winControl(None, dlg8_spec).Verify_CheckBox_Status()
        if param13 != "默认":
            time.sleep(0.1)
            # 载荷类型单选框极值
            dlg8_spec = self.dlg_spec.child_window(title="极  值", class_name="Button")
            Check_winControl(None, dlg8_spec).Verify_CheckBox_Status()
        if param14 != "默认":
            time.sleep(0.1)
            # 选择校核工况按钮
            dlg8_spec = work_window.child_window(title="...", class_name="Button")
            Check_winControl("选择校核工况", dlg8_spec).window_WhetherOpen()  # 判断预期窗口是否出现
            ControlOperationSuite(None).select_workingCondition()  # 选择组合工况
        if param15 != "默认":
            # 选择结构单元
            work_window.child_window(title="选择结构单元", class_name="Button").click()  # 点击“选择结构单元按钮”按钮
            time.sleep(0.3)
            KeyboardMouse().selectionModel()  # 选择结构单元
        if param16 != "默认":
            time.sleep(0.1)
            # 校核按钮
            work_window.校核Button.click()
            time.sleep(5)
        if param17 != "默认":
            time.sleep(0.1)
            # 关闭按钮
            work_window.关闭.click()
