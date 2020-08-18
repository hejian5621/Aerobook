# 铺层库优化工作栏，对应Aerobook路径：铺层信息--》铺层库优化
import time



class ModuleControlOperation():
    """工作栏控件操作"""

    def __init__(self,dlg_spec):
        """
        :param dlg_spec:
        """
        self.dlg_spec=dlg_spec



    def laminate_optimize(self,dicti):
        """
        铺层库优化工作栏控件操作
        :param dicti: 输入的实际数据
        :return:
        """
        Max=dicti["最大铺层数"]
        minimum=dicti["最小铺层数"]
        LayerThan1 = dicti["铺层比一"]
        LayerThan2 = dicti["铺层比二"]
        LayerThan3 = dicti["铺层比三"]
        ToleranceThan = dicti["容差比"]
        thickness_monolayer = dicti["单层厚度"]
        elasticityModulusE11 = dicti["弹性模量E11"]
        elasticityModulusE22 = dicti["弹性模量E22"]
        PoissonRatio = dicti["泊松比v12"]
        shearElasticity = dicti["剪切模量G12"]
        LaminateLength=dicti["层合板长度"]
        LaminateWidth=dicti["层合板宽度"]
        Mat8 = dicti["Mat8材料ID"]
        database = dicti["数据库名称"]
        save_database = dicti["保存为铺层数据库"]
        save_file = dicti["保存为Excel文件"]
        path1 = dicti["路径"]
        solve = dicti["求解"]
        solve_time = int(dicti["求解按钮等待时间"])
        clo = dicti["关闭"]
        clo_time = int(dicti["关闭按钮等待时间"])
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
            self.dlg_spec.CheckBox0.click()
        if save_file != "默认":
            #保存为铺层数据库勾选框
            self.dlg_spec.CheckBox2.click()
        if solve != "默认":
            time.sleep(0.5)
            #点击求解按钮
            self.dlg_spec.Button2.click()
            time.sleep(solve_time)
        if clo != "默认":
            time.sleep(0.5)
            # 点击关闭按钮
            self.dlg_spec.Button3.click()
            time.sleep(clo_time)



    def Laminatedata(self,dicti):
        """
        铺层数据库制作工具弹窗控件操作
        :param dicti: 字典参数
        :return:
        """
        param1=dicti["选择铺层Excel文件文本框"]
        param2=dicti["铺层数据保存路径文本框"]
        param3 = dicti["选择铺层Excel文件浏览按钮"]
        param4 = dicti["铺层数据保存路径浏览按钮"]
        param5 = dicti["模板文件按钮"]
        param6 = dicti["开始制作按钮"]
        param7 = dicti["关闭按钮"]
        param3_time = int(dicti["选择铺层Excel文件浏览按钮等到时"])
        param4_time = int(dicti["选择铺层Excel文件浏览按钮等到时"])
        param5_time = int(dicti["模板文件按钮等待时间"])
        param6_time = int(dicti["开始制作按钮等待时间"])
        param7_time = int(dicti["关闭按钮等待时间"])
        if param1!="默认":
            #选择铺层Excel文件文本框
            self.dlg_spec.wxWindowNR.Edit.set_text(param1)
        if param2!="默认":
            #铺层数据保存路径文本框
            self.dlg_spec.wxWindowNR2.Edit2.set_text(param2)
        if param3 != "默认":
            time.sleep(0.1)
            #选择铺层Excel文件浏览按钮
            self.dlg_spec.wxWindowNR.Button.click()
            time.sleep(param3_time)
        if param4 != "默认":
            time.sleep(0.1)
            #铺层数据保存路径浏览按钮
            self.dlg_spec.wxWindowNR2.Button2.click()
            time.sleep(param4_time)
        if param5 != "默认":
            time.sleep(0.1)
            #模板文件按钮
            self.dlg_spec.模板文件.click()
            time.sleep(param5_time)
        if param6 != "默认":
            time.sleep(1)
            #开始制作按钮
            self.dlg_spec.开始制作Button.click()
            time.sleep(param6_time)
        if param7 != "默认":
            time.sleep(0.1)
            #关闭按钮
            self.dlg_spec.关闭.click()
            time.sleep(param7_time)





