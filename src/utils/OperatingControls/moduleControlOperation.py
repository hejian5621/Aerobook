# 铺层库优化工作栏，对应Aerobook路径：铺层信息--》铺层库优化
import time
from src.utils.otherMethods.controlOperationSuite import ControlOperationSuite
from src.utils.commonality.tool import instrument


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



    def Laminatedata(self,dicti,dlg_spec):
        """
        铺层数据库制作工具弹窗控件操作
        :param dicti: 字典参数
        :param dlg_spec: 字典参数
        :return:如果是点击浏览按钮，就返回浏览按钮对应文本框地址数据
        """
        edit_box={"选择铺层Excel文件浏览按钮对应文本框实际":"","铺层数据保存路径浏览对应文本框实际":""}
        param1 = dicti["选择铺层Excel文件浏览按钮"]
        param2 = dicti["铺层数据保存路径浏览按钮"]
        param3 = dicti["选择铺层Excel文件文本框"]
        param4 = dicti["铺层数据保存路径文本框"]
        # param5 = dicti["模板文件按钮"]
        param6 = dicti["开始制作按钮"]
        param7 = dicti["关闭按钮"]
        param5_time = int(dicti["模板文件按钮等待时间"])
        param6_time = int(dicti["开始制作按钮等待时间"])
        param7_time = int(dicti["关闭按钮等待时间"])
        location = dicti["被测程序文件地址"]
        else1 = dicti["其他"]
        messageType = dicti["提示信息类型"]
        print("location:",location)
        if param1 != "默认":
            app1=self.dlg_spec.window(title="选择Excel铺层文件")
            # 选择铺层Excel文件浏览按钮
            dlg_spec1 = dlg_spec.wxWindowNR.Button
            # 判断是否有选择铺层Excel文件弹窗，如果没有再次点击选择铺层Excel文件对应的浏览按钮
            instrument().window_WhetherExist(dlg_spec1,app1,"没有选择铺层Excel文件弹窗")
            # 在保存和选择文件路径弹窗中操作
            parWin_Dicti = {"窗口标题": "选择Excel铺层文件", "关闭窗口控件名称": "打开", "关闭窗口控件操作方法": "click",
                            "地址": location,"文件夹输入状态": "文件名", "文件夹输入内容": "PlyLibDb_352_541.xlsx"}
            ControlOperationSuite(None).SelectFile_Popover(parWin_Dicti)
        if param2 != "默认":
            time.sleep(0.1)
            #铺层数据保存路径浏览按钮
            dlg_spec2=dlg_spec.wxWindowNR2.Button2
            app2 = self.dlg_spec.window(title="选择铺层数据库保存路径")
            # 判断是否有选择铺层数据保存路径弹窗，如果没有再次点击铺层数据保存路径对应的浏览按钮
            instrument().window_WhetherExist(dlg_spec2, app2, "没有选择铺层数据保存路径弹窗")
            # 判断有没有确认另存为窗口，有就点击“确定”按钮，没有就不做操作
            # 在保存和选择文件路径弹窗中操作
            parWin_Dicti = {"窗口标题": "选择铺层数据库保存路径", "关闭窗口控件名称": "保存", "关闭窗口控件操作方法": "click",
                            "地址": location,"文件夹输入状态": "文件名", "文件夹输入内容": "plylib.db"}
            nestWin_Dicti= {"嵌套窗口标题":"确认另存为","嵌套控件名称":"是","嵌套控件操作方法":"click"}
            ControlOperationSuite(None).SelectFile_Popover(parWin_Dicti,"检查",nestWin_Dicti)
            time.sleep(0.1)
        if param3!="默认" or param1 != "默认":
            #选择铺层Excel文件文本框
            if param1 != "默认":
                dlg_spec3 = self.dlg_spec.Dialog.Edit
                # 判断选择铺层Excel文件文本框控件是否存在，如果存在返回选择铺层Excel文件文本框中的文本
                edit_box1=instrument().control_WhetherExist(dlg_spec3, "选择铺层Excel文件弹窗","window_text")
                edit_box["选择铺层Excel文件浏览按钮对应文本框实际"]=edit_box1
            else:
                dlg_spec4=dlg_spec.wxWindowNR.Edit
                # 拼接路径
                if else1 == "拼接路径":
                    param3=location+param3
                # 判断选择铺层Excel文件文本框控件是否存在，如果存在向该文本框输入数据
                edit_box1 = instrument().control_WhetherExist(dlg_spec4, "铺层Excel文件文本框", "set_text", param3)
        if param4!="默认" or param2 != "默认":
            #铺层数据保存路径文本框
            if param2 != "默认":
                dlg_spec5 = self.dlg_spec.Dialog.Edit2
                # 判断铺层数据保存路径对应的选择文件窗口是否存在，如果存在返回铺层数据保存路径文本框中的文本
                edit_box2 = instrument().control_WhetherExist(dlg_spec5, "铺层数据保存路径文本框", "window_text")
                edit_box["铺层数据保存路径浏览对应文本框实际"]=edit_box2
            else:
                dlg_spec6=dlg_spec.wxWindowNR.Edit2
                # 拼接路径
                if else1=="拼接路径":
                    param4 = location + param4
                # 判断选择铺层Excel文件文本框控件是否存在，如果存在向该文本框输入数据
                edit_box1 = instrument().control_WhetherExist(dlg_spec6, "铺层数据保存路径文本框", "set_text", param4)
        # if param5 != "默认":
        #     time.sleep(0.1)
        #     #模板文件按钮
        #     dlg_spec7=self.dlg_spec.模板文件.click()
        #     # 判断是否有选择铺层Excel文件弹窗，如果没有再次点击选择铺层Excel文件对应的浏览按钮
        #     instrument().window_WhetherExist(dlg_spec7, app, "ply_example_for_aerocheck.xls",3,5)
        #     time.sleep(param5_time)
        if param6 != "默认":
            time.sleep(1)
            if messageType=="警告弹窗":
                #开始制作按钮
                app3 = self.dlg_spec.window(title="警告")
                dlg_spec6=dlg_spec.开始制作Button
                instrument().window_WhetherExist(dlg_spec6, app3, "没有选择铺层Excel文件弹窗")
            else:
                dlg_spec6 = dlg_spec.开始制作Button.check()
            time.sleep(param6_time)
        if param7 != "默认":
            time.sleep(0.1)
            #关闭按钮
            dlg_spec.关闭.click()
            time.sleep(param7_time)
        return edit_box





