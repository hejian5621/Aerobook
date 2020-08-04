# 铺层库优化工作栏，对应Aerobook路径：铺层信息--》铺层库优化
from src.utils.otherMethods.control_except import combination_Control
import time



class laminate_WorkField():
    """进入铺层库优化工作栏"""

    def __init__(self,dlg_spec):
        """
        :param dlg_spec:
        """
        self.dlg_spec=dlg_spec


    def enterInto(self):
        """
        进入铺层库优化工作栏
        :return:工作栏对象
        """
        # 点击菜单栏的“铺层信息->铺层库优化”，显示出“铺层库优化”工作栏
        combination_Control(self.dlg_spec).enterInto_menuBar("Aerocheck 1.0.4", "wxWindowNR", r"铺层信息->铺层库优化")
        # 切换到“铺层库优化”工作栏
        workField=self.dlg_spec.scrolledpanel2
        return workField


    def ControlOperating(self,dicti):
        """
        铺层库控件操作
        :return:
        """

        Max=dicti["最大铺层数"];           minimum=dicti["最小铺层数"]
        LayerThan1 = dicti["铺层比一"];    LayerThan2 = dicti["铺层比二"]      ;      LayerThan3 = dicti["铺层比三"]
        ToleranceThan = dicti["容差比"];   thickness_monolayer = dicti["单层厚度"]
        elasticityModulusE11 = dicti["弹性模量E11"];          elasticityModulusE22 = dicti["弹性模量E22"]
        PoissonRatio = dicti["泊松比v12"];           shearElasticity = dicti["剪切模量G12"]
        LaminateLength=dicti["层合板长度"];           LaminateWidth=dicti["层合板宽度"]
        Mat8 = dicti["Mat8材料ID"];                  database = dicti["数据库名称"]
        save_database = dicti["保存为铺层数据库"] ;     save_file = dicti["保存为Excel文件"]
        path1 = dicti["路径"]
        solve = dicti["求解"]
        clo = dicti["关闭"]
        if Max!="默认":
            #最大铺层数文本框
            self.dlg_spec.Edit.set_text(Max)
        if minimum!="默认":
            #最小铺层数文本框
            self.dlg_spec.Edit2.set_text(minimum)
        if LayerThan1 != "默认":
            #铺层比第一个文本框
            self.dlg_spec.Edit3.set_text(LayerThan1)
        if LayerThan2 != "默认":
            #铺层比第二个文本框
            self.dlg_spec.Edit4.set_text(LayerThan2)
        if LayerThan3 != "默认":
            #铺层比第三个文本框
            self.dlg_spec.Edit5.set_text(LayerThan3)
        if ToleranceThan != "默认":
            #容差比
            self.dlg_spec.Edit6.set_text(ToleranceThan)
        if thickness_monolayer != "默认":
            #单层厚度
            self.dlg_spec.Edit7.set_text(thickness_monolayer)
        if elasticityModulusE11 != "默认":
            #弹性模量E11
            self.dlg_spec.Edit8.set_text(elasticityModulusE11)
        if elasticityModulusE22 != "默认":
            #弹性模量E22
            self.dlg_spec.Edit9.set_text(elasticityModulusE22)
        if PoissonRatio != "默认":
            #泊松比v12
            self.dlg_spec.Edit10.set_text(PoissonRatio)
        if shearElasticity != "默认":
            #剪切模量G12
            self.dlg_spec.Edit12.set_text(shearElasticity)
        if LaminateLength != "默认":
            #层合板长度a
            self.dlg_spec.Edit13.set_text(LaminateLength)
        if LaminateWidth != "默认":
            #层合板宽度b
            self.dlg_spec.Edit14.set_text(LaminateWidth)
        if Mat8 != "默认":
            #Mat8材料ID
            self.dlg_spec.Edit15.set_text(Mat8)
        if database != "默认":
            #数据库名称
            self.dlg_spec.Edit16.set_text(database)
        if path1 != "默认":
            #数据库名称
            self.dlg_spec.Edit16.set_text(path1)
        if save_database != "默认":
            #保存为铺层数据库勾选框
            self.dlg_spec.CheckBox0.check()
        if save_file != "默认":
            #保存为铺层数据库勾选框
            self.dlg_spec.CheckBox2.check()
        if solve != "默认":
            #保存为铺层数据库勾选框
            self.dlg_spec.Button2.check()
        # if clo != "默认":
        #     # 保存为铺层数据库勾选框
        #     self.dlg_spec.Button3.check()