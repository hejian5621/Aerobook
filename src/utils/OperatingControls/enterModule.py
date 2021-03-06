# 进入被测弹窗或者工作栏
import time,sys,os
from pywinauto.application import Application
from pywinauto import findwindows
from config.configurationFile import ProfileDataProcessing
from tool import MyException
import win32gui



"""进入被测弹窗"""
class BeingMeasured_popupWin:
    """进入被测弹窗"""

    def __init__(self,window_title,cycleIndex=20,CircleInitial=1):
        self.window_title=window_title   # 弹窗标题或者名称
        self.cycleIndex = cycleIndex  # 循环最终次数
        self.CircleInitial = CircleInitial  # 循环初始次数
        self.popupWin = None  # 返回的弹窗实体



    def menu_LetsGoTopopover(self):
        """
        确定被测弹窗是否存在，如果存在返回弹窗实体
        :return:
        """

        while self.CircleInitial<=self.cycleIndex:
            try:
                hwnd = win32gui.FindWindow(None, self.window_title)
                if hwnd == 0:
                    raise MyException("窗口没有关闭")  # 实例化一个异常,实例化的时候需要传参数
            except Exception as obj:  # 如果没有找到弹窗继续循环找
                time.sleep(0.1)
            else:
                app = Application().connect(handle=hwnd)
                self.popupWin = app.window(handle=hwnd)
                break
            self.CircleInitial = self.CircleInitial + 1
            if self.CircleInitial == (self.cycleIndex + 1):
                raise MyException("没有找到”%r“弹窗" % self.window_title)
        return self.popupWin


    def Laminatedata_popUp(self,module_window):
        """
        铺层数据库制作工具弹窗
        切换到控件实例
        :return:
        """
        window_one=module_window.filepicker0
        window_two=module_window.filepicker2
        return window_one,window_two


"""切换到被测工作栏"""
class  ctrW_AeroAerochcek:
    """切换到被测工作栏"""

    def __init__(self,son_window):
        self.workField = son_window.scrolledpanelwxWindowNR2   # 切换到被测工作
        self.workField_son=None
        self.win_one = None
        self.win_two = None
        self.win_three = None
        self.win_four = None




    def workField_general(self):
        """
        切换到工作栏窗口
        :return:
        """
        # 切换到铺层库优化工作栏
        return self.workField



    def workField_sizeInfo(self):
        """
        尺寸信息--一维、二维单元尺寸定义（模板）
        :return:
        """
        dlg_spec = self.workField.child_window(class_name="_wx_SysTabCtl32")
        self.workField_son = dlg_spec.panelwxWindowNR2
        return self.workField_son



    def workField_composite_information(self):
        """
        材料信息--定义复合材料信息--编辑材料许用值、定义材料许用值
        :param Entities_winName:实体窗口
        :return:
        """
        # 切换实体窗口
        dlg_spec = self.workField.材料许用值曲线表_wx_SysTabCtl32
        self.workField_son = dlg_spec.panelwxWindowNR0
        return self.workField_son



    def workField_intensityCheck(self):
        """
        进入复合材料强度校核--一维单元工作栏(赶柱单元)、二维单元工作栏
        :return:
        """
        dlg_spec = self.workField.复合材料强度校核_wx_SysTabCtl32
        self.workField_son = dlg_spec.panelwxWindowNR2
        # dlg_spec2.print_control_identifiers()
        return self.workField_son,self.workField


    def workField_SizeDefinition_1D(self):
        """
        进入尺寸信息->一维单元尺寸定义
        :return:
        """
        # 获取窗口一
        dlg_spec = self.workField.截面形状_wx_SysTabCtl321
        self.win_one = dlg_spec.panelwxWindowNR0
        # 获取窗口二
        dlg2_spec = self.win_one.grid1
        self.win_two = dlg2_spec.GridWindowwxWindowNR0
        # 获取窗口三
        dlg3_spec = self.workField.复合材料_wx_SysTabCtl32
        dlg4_spec =dlg3_spec.panelwxWindowNR1
        dlg5_spec = dlg4_spec.gridwxWindowNR
        self.win_three = dlg5_spec.wxWindowNR6
        # 获取窗口四
        dlg6_spec = self.workField.复合材料_wx_SysTabCtl32
        dlg7_spec = dlg6_spec.panel5
        self.win_four = dlg7_spec.GridWindow2
        return self.win_one,self.win_two,self.win_three,self.win_four



    def workField_SizeDefinition_2D(self):
        """
        进入尺寸信息->二维单元尺寸定义
        :return:
        """
        # 获取窗口一
        dlg_spec = self.workField.截面形状_wx_SysTabCtl321
        self.win_one = dlg_spec.panelwxWindowNR0
        # 获取窗口二
        work4 = self.win_one.复合材料_wx_SysTabCtl32
        self.win_two = work4.wxWindowNR6
        return self.win_one,self.win_two


    def workField_Open_EditArgument(self):
        """
        紧固件强度校核--紧固件参数输入
        打开编辑参数弹框,并返回窗口实例
        :return:
        """
        from tool import Check_winControl
        workField=self.workField.Button2
        Check_winControl(None,workField).window_handle_WhetherOpen("#32770","Edit4")  # 编辑参数是否打开
        hwnd = win32gui.FindWindow("#32770", None)  # 获取窗体的句柄
        app = Application().connect(handle=hwnd, timeout=20)
        dlg_spec = app.window(handle=hwnd)  # 切换到选择文件弹窗窗口
        return dlg_spec


    def workField_fastener_parOptimization(self):
        """
        紧固件优化->紧固件参数优化
        :return:
        """
        self.win_one = self.workField.child_window(title="panel", class_name="wxWindowNR")
        return self.win_one


    def workField_fastenerSEO(self,operationWindow_son):
        """
        紧固件优化->紧固件参数优化
        :return:
        """
        from tool import Check_winControl
        from src.utils.OperatingControls.moduleControlOperation import OperatingControls
        dlg_spec = self.workField.材料许用值曲线表_wx_SysTabCtl32
        self.win_one = dlg_spec.panelwxWindowNR0
        if operationWindow_son =="编辑材料许用值曲线弹窗":
            dlg_spec = OperatingControls(self.win_one).ExpressionAssembly("Button1")  # 在编辑材料许用值工作栏点击“创建材料许用值曲线”按钮
            Check_winControl("编辑材料许用值曲线", dlg_spec).window_WhetherOpen()  # 判断预期窗口是否出现
            self.win_one = BeingMeasured_popupWin("编辑材料许用值曲线").menu_LetsGoTopopover()  # 切换到“编辑材料许用值曲线弹窗”中
            self.win_two =  self.win_one.child_window(title="GridWindow", class_name="wxWindowNR") #  切换到网格窗口
        return self.win_one,self.win_two





"""切换到被测工作栏"""
class  ctrW_AeroFiberbook:

    def __init__(self, son_window):
        self.workField = son_window.scrolledpanelwxWindowNR2  # 切换到被测工作
        self.workField_son = None
        self.win_one = None
        self.win_two = None
        self.win_three = None
        self.win_four = None



    def workField_general(self):
        """
        切换到工作栏窗口
        :return:
        """
        # 切换到铺层库优化工作栏
        return self.workField


    def workField_1DDESVAR_sectionSize(self):
        """
        一维单元设计参数（截面尺寸）
        :return:
        """
        # 窗口二
        self.win_two=self.workField.gridwxWindowNR1.GridWindowwxWindowNR1
        # 窗口三
        self.win_three=self.workField.panelwxWindowNR4.GridWindow2
        # 窗口四
        self.win_four=self.workField.panelwxWindowNR4
        return self.workField,self.win_two,self.win_three,self.win_four


    def workField_1DSection_popUps(self):
        """
        一维单元设计参数（截面尺寸）--》1D截面参数定义弹窗
        :return:
        """
        win = self.workField.gridwxWindowNR1.GridWindowwxWindowNR1
        # 打开“1D截面参数定义弹窗”
        win.double_click_input(coords=(60, 10), button="left")
        self.win_one = BeingMeasured_popupWin("1D截面参数定义").menu_LetsGoTopopover()
        return self.win_one,self.win_two,self.win_three,self.win_four

    def workField_2DDESVAR_popUps(self):
        """
        二维单元设计参数--》铺层厚度/铺层比定义
        :return:
        """
        win = self.workField.child_window(title="grid", class_name="wxWindowNR")
        # 打开“1D截面参数定义弹窗”
        win.double_click_input(coords=(100, 40), button="left")
        self.win_one = BeingMeasured_popupWin("铺层厚度/铺层比定义").menu_LetsGoTopopover()
        return self.win_one, self.win_two, self.win_three, self.win_four

    def workField_LayerThan_popUps(self):
        """
        一维单元设计参数（截面尺寸）--》铺层比定义弹窗
        :return:
        """
        win = self.workField.panelwxWindowNR4.GridWindow2
        # 打开“1D截面参数定义弹窗”
        win.double_click_input(coords=(60, 10), button="left")
        self.win_one = BeingMeasured_popupWin("铺层比定义").menu_LetsGoTopopover()
        return self.win_one,self.win_two,self.win_three,self.win_four


    def workField_2DDESVAR(self):
        """
        二维单元设计参数
        :return:
        """
        self.win_two = self.workField.child_window(title="grid", class_name="wxWindowNR")
        return self.workField, self.win_two, self.win_three, self.win_four


    def workField_Pole_stability(self):
        """
        稳定性设计响应--杆柱稳定性响应和约束
        :return:
        """
        self.win_two = self.workField.材料类型_wx_SysTabCtl32
        self.win_three = self.win_two.child_window(title="grid", class_name="wxWindowNR").child_window(title="GridWindow", class_name="wxWindowNR")
        return self.workField, self.win_two, self.win_three, self.win_four



"""特殊情况下的控件操作，一般是正常方法识别不了控件"""
class specialWay_OperatingControls:
    """特殊情况下的控件操作，一般是正常方法识别不了控件"""


    def __init__(self,cut_winName):
        self.cut_winName=cut_winName     # 被操作按钮名称
        self.aero_title = ProfileDataProcessing("commonality", "AerobookEdition").config_File()  # 从配置文件获取Aerobook窗口标题



    def uia_OperatingControls(self,searchDepth=7):
        """
        使用UIA的方法点击，工作栏中的切换模块按钮
        :param searchDepth:使用UIA查看控件的深度
        :return:
        """
        import uiautomation
        Use = uiautomation.WindowControl(searchDepth=1, Name=self.aero_title)  # 连接Aerobook窗口
        # 点击切换窗口按钮
        app1 = Use.Control(searchDepth=7, Name=self.cut_winName)
        app1.Click()




"""获取窗口实例"""
class GetWindowInstance:
    """获取窗口实例"""

    def __init__(self,property):
        self.property = property  # 字典类型测试用例
        self.initialLevel = property["初始化级别"]
        self.testWinTitle = property["操作窗口标题"]
        self.testWinTitle_son = property["操作子窗口标题"]
        self.ModuMarking = property["模块唯一标识"]
        self.module = property["测试主模块"]
        self.win_one = None  # 窗口一
        self.win_two = None  # 窗口二
        self.win_three = None  # 窗口三
        self.win_four = None  # 窗口四



    def get_window_instance(self):
        """
        获取操作控件的各个窗口
        :return:
        """
        print("\033[0;32;33m《开始获取“%r”模块窗口标识》\033[0m"%self.ModuMarking, __file__, sys._getframe().f_lineno)
        print("")
        from src.utils.otherMethods.initialize import pywin_openAProgram
        # 连接到被测程序，并且通过菜单栏打开被测模块
        aero_window, son_window = pywin_openAProgram(self.module).menuOpen(self.property)
        if self.module=="Aerobook-Aerocheck":
            # 切换到被测模块窗口
            if self.ModuMarking == "铺层信息--铺层库优化" or \
                    self.ModuMarking == "求解计算--求解计算" or \
                    self.ModuMarking == "紧固件强度校核--紧固件参数设置" or \
                    self.ModuMarking == "材料信息--定义金属材料参数" or \
                    self.ModuMarking == "金属结构强度校核--金属一维单元强度校核" or \
                    self.ModuMarking == "金属结构强度校核--金属二维单元强度校核" or \
                    self.ModuMarking == "金属结构强度校核--金属加筋板强度校核" or \
                    self.ModuMarking == "金属结构强度校核--金属曲板后驱曲强度校核":
                self.win_one = ctrW_AeroAerochcek(son_window).workField_general()
            elif self.ModuMarking == "尺寸信息--一维单元尺寸定义（模板）" or self.ModuMarking == "尺寸信息--二维单元尺寸定义（模板）":
                self.win_one = ctrW_AeroAerochcek(son_window).workField_sizeInfo()
            elif self.ModuMarking == "铺层信息--铺层数据库制作工具":
                # 切入铺层数据库工具弹窗中
                self.win_three = BeingMeasured_popupWin("铺层数据库制作工具").menu_LetsGoTopopover()
                # 切入铺层数据库工具弹窗中控件中
                self.win_one, self.win_two = BeingMeasured_popupWin(None).Laminatedata_popUp(self.win_three)
            elif self.ModuMarking == "载荷信息--载荷数据库制作工具":
                # 切入铺层数据库工具弹窗中
                self.win_three = BeingMeasured_popupWin("载荷数据库制作工具").menu_LetsGoTopopover()
                # 切入铺层数据库工具弹窗中控件中
                self.win_one, self.win_two = BeingMeasured_popupWin(None).Laminatedata_popUp(self.win_three)
            elif self.ModuMarking == "载荷信息--编辑工况":
                self.win_one = BeingMeasured_popupWin("编辑工况").menu_LetsGoTopopover()
            elif self.ModuMarking == "复材结构强度校核--复合材料强度校核1D" or \
                    self.ModuMarking == "复材结构强度校核--复合材料强度校核2D":
                specialWay_OperatingControls(self.testWinTitle_son).uia_OperatingControls()  # 使用uiautomation框架点击切换模块
                self.win_one, self.win_two = ctrW_AeroAerochcek(son_window).workField_intensityCheck()
            elif self.ModuMarking == "尺寸信息--一维单元尺寸定义":
                self.win_one, self.win_two, self.win_three, self.win_four = ctrW_AeroAerochcek(son_window).workField_SizeDefinition_1D()
            elif self.ModuMarking == "尺寸信息--二维单元尺寸定义":
                self.win_one, self.win_two = ctrW_AeroAerochcek(son_window).workField_SizeDefinition_2D()
            elif self.ModuMarking == "紧固件强度校核--紧固件信息输入":
                if self.testWinTitle_son == "紧固件参数输入":
                    self.win_one = ctrW_AeroAerochcek(son_window).workField_general()
                elif self.testWinTitle_son == "编辑参数弹框":
                    self.win_one = ctrW_AeroAerochcek(son_window).workField_Open_EditArgument()
            elif self.ModuMarking == "紧固件强度校核--紧固件强度校核":
                self.win_one = ctrW_AeroAerochcek(son_window).workField_general()
            elif self.ModuMarking == "紧固件优化--紧固件参数优化":
                self.win_one = ctrW_AeroAerochcek(son_window).workField_fastener_parOptimization()
            elif self.ModuMarking == "材料信息--定义复合材料参数":
                specialWay_OperatingControls(self.testWinTitle).uia_OperatingControls()  # 使用uiautomation框架点击切换模块
                self.win_one,self.win_two = ctrW_AeroAerochcek(son_window).workField_fastenerSEO(self.testWinTitle_son)
            else:
                raise MyException("没有找到需要切换的窗口：%r" % self.ModuMarking)
        elif self.module=="Aerobook-Fiberbook":
            if self.ModuMarking == "优化设置--全局设置":
                self.win_one =ctrW_AeroFiberbook(son_window).workField_general()
            elif self.ModuMarking == "设计变量--一维单元设计变量（截面尺寸）":
                if self.testWinTitle_son=="一维单元设计参数（截面尺寸）":
                    self.win_one,self.win_two,self.win_three,self.win_four = ctrW_AeroFiberbook(son_window).workField_1DDESVAR_sectionSize()
                elif self.testWinTitle_son=="1D截面参数定义":
                    self.win_one, self.win_two, self.win_three, self.win_four = ctrW_AeroFiberbook(son_window).workField_1DSection_popUps()
                elif self.testWinTitle_son=="铺层比定义":
                    self.win_one, self.win_two, self.win_three, self.win_four = ctrW_AeroFiberbook(son_window).workField_LayerThan_popUps()
                else:
                    raise MyException("没有找到需要切换的子窗口：%r" % self.testWinTitle_son)
            elif self.ModuMarking == "设计变量--一维单元设计变量（截面积）":
                self.win_one =ctrW_AeroFiberbook(son_window).workField_general()
            elif self.ModuMarking == "设计变量--二维单元设计参数":
                if self.testWinTitle_son == "二维单元设计参数":
                    self.win_one, self.win_two, self.win_three, self.win_four = ctrW_AeroFiberbook(son_window).workField_2DDESVAR()
                elif self.testWinTitle_son == "铺层厚度/铺层比定义":
                    self.win_one, self.win_two, self.win_three, self.win_four = ctrW_AeroFiberbook(son_window).workField_2DDESVAR_popUps()
            elif self.ModuMarking == "应变设计响应--一维单元应变设计响应":
                self.win_one = ctrW_AeroFiberbook(son_window).workField_general()
            elif self.ModuMarking == "应变设计响应--二维单元应变设计响应":
                self.win_one = ctrW_AeroFiberbook(son_window).workField_general()
            elif self.ModuMarking == "应变设计响应--二维单元应变耦合DRESP3":
                self.win_one = ctrW_AeroFiberbook(son_window).workField_general()
            elif self.ModuMarking == "应力设计响应->一维单元应力设计响应":
                self.win_one = ctrW_AeroFiberbook(son_window).workField_general()
            elif self.ModuMarking == "应力设计响应->二维单元应力设计响应":
                self.win_one = ctrW_AeroFiberbook(son_window).workField_general()
            elif self.ModuMarking == "丢成/厚度比设计响应--一维单元丢成/厚度比设计响应":
                self.win_one = ctrW_AeroFiberbook(son_window).workField_general()
            elif self.ModuMarking == "丢成/厚度比设计响应--二维单元丢成/厚度比设计响应":
                self.win_one = ctrW_AeroFiberbook(son_window).workField_general()
            elif self.ModuMarking == "优化设置--泊松比匹配响应":
                self.win_one = ctrW_AeroFiberbook(son_window).workField_general()
            elif self.ModuMarking == "刚度约束设计响应--位移设计响应":
                self.win_one = ctrW_AeroFiberbook(son_window).workField_general()
            elif self.ModuMarking == "刚度约束设计响应--扭转角约束设计响应":
                self.win_one = ctrW_AeroFiberbook(son_window).workField_general()
            elif self.ModuMarking == "刚度约束设计响应--刚度比设计响应":
                self.win_one = ctrW_AeroFiberbook(son_window).workField_general()
            elif self.ModuMarking == "机翼优化响应--梁腹板缘条厚度比设计响应":
                self.win_one = ctrW_AeroFiberbook(son_window).workField_general()
            elif self.ModuMarking == "机翼优化响应--梁腹板缘条铺层比之差设计响应":
                self.win_one = ctrW_AeroFiberbook(son_window).workField_general()
            elif self.ModuMarking == "机翼优化响应--肋站位EI GJ设计响应":
                self.win_one = ctrW_AeroFiberbook(son_window).workField_general()
            elif self.ModuMarking == "稳定性设计响应--杆柱稳定性响应和约束":
                self.win_one, self.win_two, self.win_three, self.win_four = ctrW_AeroFiberbook(son_window).workField_Pole_stability()
            elif self.ModuMarking == "稳定性设计响应--平板稳定性响应约束":
                self.win_one = ctrW_AeroFiberbook(son_window).workField_general()
            elif self.ModuMarking == "稳定性设计响应--曲板稳定性响应约束":
                self.win_one = ctrW_AeroFiberbook(son_window).workField_general()
            elif self.ModuMarking == "稳定性设计响应--加筋板稳定性响应约束":
                self.win_one, self.win_two, self.win_three, self.win_four = ctrW_AeroFiberbook(son_window).workField_Pole_stability()
            else:
                raise MyException("没有找到需要切换的窗口：%r" % self.ModuMarking)
        else:
            raise MyException("没有找到主模块名称：%r" % self.module)
        print("\033[0;34m窗口标识一：%r，窗口标识二：%r，窗口标识三：%r，窗口标识四：%r"%(self.win_one,self.win_two,self.win_three,self.win_four), __file__, sys._getframe().f_lineno)
        print("")
        print("\033[0;32;35m{{窗口标识获取完毕}}\033[0m", __file__, sys._getframe().f_lineno)
        print("")
        print(" ")
        return self.win_one,self.win_two,self.win_three,self.win_four