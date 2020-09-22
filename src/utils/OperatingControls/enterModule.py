# 进入被测弹窗或者工作栏
import time,sys,os
from pywinauto.application import Application
from pywinauto import findwindows
from config.configurationFile import ProfileDataProcessing



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
                app = Application().connect(title_re=self.window_title)
                self.popupWin = app.window(title=self.window_title)
            except findwindows.ElementNotFoundError as err:   # 如果没有找到弹窗继续循环找
                time.sleep(0.1)
            except Exception :
                print("没有找到”%r“弹窗"%self.window_title, __file__, sys._getframe().f_lineno)
                os._exit(0)
            else:
                break
            self.CircleInitial = self.CircleInitial + 1
            if self.CircleInitial == (self.cycleIndex + 1):
                print("没有找到”%r“弹窗"%self.window_title, __file__, sys._getframe().f_lineno)
                os._exit(0)
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



class  BeingMeasured_work:
    """切换到被测工作栏"""

    def __init__(self,son_window):
        self.workField = son_window.scrolledpanelwxWindowNR2   # 切换到被测工作
        self.workField_son=None
        self.window_one = None
        self.window_two = None
        self.window_three = None
        self.window_four = None




    def workField_general(self):
        """
        切换到工作栏实体
        :return:铺层库优化工作栏对象
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
        # self.workField_son.print_control_identifiers()
        return self.workField_son



    def workField_composite_information(self):
        """
        材料信息--定义复合材料信息--编辑材料许用值、定义材料许用值
        :param Entities_winName:实体窗口
        :return:
        """
        # 切换实体窗口
        dlg_spec = self.workField.选择材料许用值曲线_wx_SysTabCtl32
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
        self.window_one = dlg_spec.panelwxWindowNR0
        # 获取窗口二
        dlg2_spec = self.window_one.grid1
        self.window_two = dlg2_spec.GridWindowwxWindowNR0
        # 获取窗口三
        dlg3_spec = self.workField.复合材料_wx_SysTabCtl32
        dlg4_spec =dlg3_spec.panelwxWindowNR1
        dlg5_spec = dlg4_spec.gridwxWindowNR
        self.window_three = dlg5_spec.wxWindowNR6
        # 获取窗口四
        dlg6_spec = self.workField.复合材料_wx_SysTabCtl32
        dlg7_spec = dlg6_spec.panel5
        self.window_four = dlg7_spec.GridWindow2
        return self.window_one,self.window_two,self.window_three,self.window_four



    def workField_SizeDefinition_2D(self):
        """
        进入尺寸信息->二维单元尺寸定义
        :return:
        """
        # 获取窗口一
        dlg_spec = self.workField.截面形状_wx_SysTabCtl321
        self.window_one = dlg_spec.panelwxWindowNR0
        # 获取窗口二
        work4 = self.window_one.复合材料_wx_SysTabCtl32
        self.window_two = work4.wxWindowNR6
        return self.window_one,self.window_two


    def workField_Open_EditArgument(self):
        """
        紧固件强度校核--紧固件参数输入
        打开编辑参数弹框,并返回窗口实例
        :return:
        """
        from tool import Check_winControl
        workField=self.workField.Button2
        Check_winControl(None,workField).window_handle_WhetherOpen("#32770","Edit4")  # 编辑参数是否打开
        import win32gui
        hwnd = win32gui.FindWindow("#32770", None)  # 获取窗体的句柄
        app = Application().connect(handle=hwnd, timeout=20)
        dlg_spec = app.window(handle=hwnd)  # 切换到选择文件弹窗窗口
        return dlg_spec


    def workField_fastener_parOptimization(self):
        """
        紧固件优化->紧固件参数优化
        :return:
        """
        self.window_one = self.workField.child_window(title="panel", class_name="wxWindowNR")
        return self.window_one





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


