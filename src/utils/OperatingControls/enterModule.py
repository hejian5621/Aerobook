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





class  BeingMeasured_work:
    """切换到被测工作栏"""

    def __init__(self,son_window):
        self.workField = son_window.scrolledpanelwxWindowNR2   # 切换到被测工作
        self.workField_son=None




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


