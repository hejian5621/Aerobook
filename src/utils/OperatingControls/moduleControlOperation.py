# 铺层库优化工作栏，对应Aerobook路径：铺层信息--》铺层库优化
import time
from src.utils.otherMethods.controlOperationSuite import ControlOperationSuite
from src.utils.commonality.tool import instrument,KeyboardMouse,Check_winControl


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



    def loaddatabase_popUp_operation(self,dicti):
        """
        铺层数据库制作工具弹窗控件操作
        :param dicti: 字典参数
        :return:如果是点击浏览按钮，就返回浏览按钮对应文本框地址数据
        """
        edit_box={"选择铺层Excel文件浏览按钮对应文本框实际":"","铺层数据保存路径浏览对应文本框实际":""}
        param1 = dicti["选择铺层Excel文件文本框"]
        param2 = dicti["载荷数据库保存路径文本框"]
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
            # 选择铺层Excel文件浏览按钮
            dlg_spec1 = self.dlg_spec.wxWindowNR.Button
            # 判断是否有选择铺层Excel文件弹窗，如果没有再次点击选择铺层Excel文件对应的浏览按钮
            Check_winControl("选择Excel铺层文件",dlg_spec1).window_WhetherOpen()
            # 在保存和选择文件路径弹窗中操作
            parWin2_Dicti = {"窗口标题": "选择Excel铺层文件", "关闭窗口控件名称": "打开", "关闭窗口控件操作方法": "click",
                            "地址": location,"文件夹输入状态": "文件名", "文件夹输入内容": "PlyLibDb_352_541.xlsx"}
            ControlOperationSuite(None).SelectFile_Popover(parWin2_Dicti)
        if param2 != "默认":
            time.sleep(0.1)
            #铺层数据保存路径浏览按钮
            dlg_spec2=self.dlg_spec.wxWindowNR2.Button2
            Check_winControl("选择铺层数据库保存路径", dlg_spec2).window_WhetherOpen()  # 判断预期窗口是否出现
            # 判断有没有确认另存为窗口，有就点击“确定”按钮，没有就不做操作
            # 在保存和选择文件路径弹窗中操作
            parWin1_Dicti = {"窗口标题": "选择铺层数据库保存路径", "关闭窗口控件名称": "保存", "关闭窗口控件操作方法": "click",
                            "地址": location, "文件夹输入内容": "plylib.db"}
            nestWin_Dicti= {"嵌套窗口标题":"确认另存为","嵌套控件名称":"是","嵌套控件操作方法":"click"}
            ControlOperationSuite(None).SelectFile_Popover(parWin1_Dicti,"检查",nestWin_Dicti)
            time.sleep(0.1)
        if param3!="默认" or param1 != "默认":
            #选择铺层Excel文件文本框
            if param1 != "默认":
                dlg_spec3 = self.dlg_spec.Dialog.Edit
                # 判断选择铺层Excel文件文本框控件是否存在，如果存在返回选择铺层Excel文件文本框中的文本
                # edit_box1=instrument().control_WhetherExist(dlg_spec3, "选择铺层Excel文件弹窗","window_text")
                # edit_box["选择铺层Excel文件浏览按钮对应文本框实际"]=edit_box1
            else:
                dlg_spec4=self.dlg_spec.wxWindowNR.Edit
                if else1 == "拼接路径":  # 拼接路径
                    param3=location+param3
                # # 判断选择铺层Excel文件文本框控件是否存在，如果存在向该文本框输入数据
                # edit_box1 = instrument().control_WhetherExist(dlg_spec4, "铺层Excel文件文本框", "set_text", param3)
        if param4!="默认" or param2 != "默认":
            #铺层数据保存路径文本框
            if param2 != "默认":
                dlg_spec5 = self.dlg_spec.Dialog.Edit2
                # 判断铺层数据保存路径对应的选择文件窗口是否存在，如果存在返回铺层数据保存路径文本框中的文本
                # edit_box2 = instrument().control_WhetherExist(dlg_spec5, "铺层数据保存路径文本框", "window_text")
                # edit_box["铺层数据保存路径浏览对应文本框实际"]=edit_box2
            else:
                dlg_spec6=self.dlg_spec.wxWindowNR.Edit2
                # 拼接路径
                if else1=="拼接路径":
                    param4 = location + param4
                # # 判断选择铺层Excel文件文本框控件是否存在，如果存在向该文本框输入数据
                # edit_box1 = instrument().control_WhetherExist(dlg_spec6, "铺层数据保存路径文本框", "set_text", param4)
        # if param5 != "默认":
        #     time.sleep(0.1)
        #     #模板文件按钮
        #     dlg_spec7=self.dlg_spec.模板文件.click()
        #     # 判断是否有选择铺层Excel文件弹窗，如果没有再次点击选择铺层Excel文件对应的浏览按钮
        #     instrument().window_WhetherExist(dlg_spec7, app, "ply_example_for_aerocheck.xls",3,5)
        #     time.sleep(param5_time)
        if param6 != "默认":
            time.sleep(1)
            if messageType=="警告弹窗":  # 预期点击开始制作按钮后会弹出警告弹窗
                #开始制作按钮
                dlg_spec6=self.dlg_spec.开始制作Button
                Check_winControl("警告", dlg_spec6).window_WhetherOpen()  # 判断预期窗口是否出现
            else:
                Check_winControl("铺层数据库制作工具", "开始制作Button").popUp_Whether_close()
            time.sleep(param6_time)
        if param7 != "默认":
            time.sleep(0.1)
            #关闭按钮
            self.dlg_spec.关闭.click()
            time.sleep(param7_time)
        return edit_box




    def sizeInfo_1DXls_operation(self,dicti):
        """
        尺寸定义--1D单元尺寸定义（模板）
        :return:
        """
        param1 = dicti["材料类型"]
        param2 = dicti["选择路径浏览按钮"]
        param3 = dicti["选择路径文本框"]
        param4 = dicti["创建按钮"]
        param5 = dicti["关闭按钮"]
        param1_time = int(dicti["创建按钮等待时间"])
        param2_time = int(dicti["关闭按钮等待时间"])
        location = dicti["被测程序文件地址"]
        else1 = dicti["其他"]
        messageType = dicti["提示信息类型"]
        if param1 != "默认":
            time.sleep(0.1)
            # 材料类型：选择“复合材料”或者“金属材料”
            if param1=="金属材料":
                self.dlg_spec.金属材料.click()
            elif param1=="金属材料":
                self.dlg_spec.复合材料.click()
            else:
                self.dlg_spec.复合材料.click()
        if param2 != "默认":
            time.sleep(0.1)
            # 检查选择文件弹窗是否打开
            dlg1_spec = self.dlg_spec.Button1
            Check_winControl("指定Excel模板文件路径", dlg1_spec).window_WhetherOpen()  # 判断预期窗口是否出现
            time.sleep(0.1)
            # 在“指定Excel模板文件路径”弹窗中操作
            parWin1_Dicti = {"窗口标题": "指定Excel模板文件路径", "关闭窗口控件名称": "打开", "关闭窗口控件操作方法": "click",
                             "地址": location,  "文件夹输入内容": "yz1d.xlsx"}
            ControlOperationSuite(None).SelectFile_Popover(parWin1_Dicti)
            time.sleep(0.1)
        if param3 != "默认" :
            #在类型材料文本框中输入路径
            dlg3_spec=self.dlg_spec.child_window(class_name="Edit")
            if else1 == "拼接路径":
                param3 = location + param3
            # 判断选择铺层Excel文件文本框控件是否存在，如果存在向该文本框输入数据
            if param3:
                Check_winControl(None, dlg3_spec).Verify_inputBox( param3)
        if param4 != "默认" :
            time.sleep(0.1)
            #点击“创建”按钮
            self.dlg_spec.创建.click()
            time.sleep(param1_time)
        if param5 != "默认":
            time.sleep(0.1)
            # 关闭按钮
            self.dlg_spec.关闭.click()
            time.sleep(param2_time)


    def solveCalculation_operation(self,dicti):
        """
        求解计算--求解计算
        :return:
        """
        param1 = dicti["属性更新选择路径文本框"]
        param2 = dicti["载荷提取选择路径文本框"]
        param3 = dicti["属性更新选择路径浏览按钮"]
        param4 = dicti["载荷提取选择路径浏览按钮"]
        param5 = dicti["属性更新按钮"]
        param6 = dicti["求解计算按钮"]
        param7 = dicti["载荷提取按钮"]
        param8 = dicti["关闭按钮"]
        param1_time = int(dicti["属性更新按钮等待时间"])
        param2_time = int(dicti["求解计算按钮等待时间"])
        param3_time = int(dicti["载荷提取按钮等待时间"])
        param4_time = int(dicti["关闭按钮等待时间"])
        location = dicti["被测程序文件地址"]
        else1 = dicti["其他"]
        if param1 != "默认":
           # 属性更新选择路径文本框
           dlg1_spec=self.dlg_spec.Edit
           if else1=="拼接路径":
               param1 = location + param1
           if param1:
               Check_winControl(None, dlg1_spec).Verify_inputBox(param1)
        if param2 != "默认":
            # 载荷提取选择路径文本框
            dlg2_spec = self.dlg_spec.Edit2
            if else1 == "拼接路径":
                param2 = location + param2
            if param2:
                Check_winControl(None, dlg2_spec).Verify_inputBox(param2)
        if param3 != "默认" :
            # 属性更新选择路径浏览按钮
            dlg3_spec = self.dlg_spec.Button2
            Check_winControl("指定bdf文件保存路径", dlg3_spec).window_WhetherOpen()  # 判断预期窗口是否出现
            # 在“指定bdf文件保存路径”弹窗中操作
            parWin3_Dicti = {"窗口标题": "指定bdf文件保存路径", "关闭窗口控件名称": "保存", "关闭窗口控件操作方法": "click",
                             "地址": location, "文件夹输入内容": "update_Htail.fem"}
            ControlOperationSuite(None).SelectFile_Popover(parWin3_Dicti)
        if param4 != "默认" :
            # 属性更新选择路径浏览按钮
            dlg4_spec = self.dlg_spec.Button3
            Check_winControl("指定载荷数据库保存路径", dlg4_spec).window_WhetherOpen()  # 判断预期窗口是否出现
            # 在“指定bdf文件保存路径”弹窗中操作
            parWin4_Dicti = {"窗口标题": "指定载荷数据库保存路径", "关闭窗口控件名称": "保存", "关闭窗口控件操作方法": "click",
                             "地址": location, "文件夹输入内容": "load.db"}
            ControlOperationSuite(None).SelectFile_Popover(parWin4_Dicti)
        if param5 != "默认":
            time.sleep(0.1)
            # 属性更新按钮
            self.dlg_spec.属性更新Button.click()
            time.sleep(param1_time)
        if param6 != "默认":
            time.sleep(0.1)
            # 求解计算按钮
            self.dlg_spec.求解计算.click()
            time.sleep(param2_time)
        if param7 != "默认":
            time.sleep(0.1)
            # 载荷提取按钮
            self.dlg_spec.载荷提取Button.click()
            time.sleep(param3_time)
        if param8 != "默认":
            time.sleep(0.1)
            # 关闭按钮
            self.dlg_spec.关闭.click()
            time.sleep(param4_time)


    def Laminatedata_operation(self, dicti):
        """
        铺层数据库制作工具弹窗控件操作
        :param dicti: 字典参数
        :return:如果是点击浏览按钮，就返回浏览按钮对应文本框地址数据
        """
        edit_box = {"选择铺层Excel文件浏览按钮对应文本框实际": "", "铺层数据保存路径浏览对应文本框实际": ""}
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
        print("location:", location)
        if param1 != "默认":
            # 选择铺层Excel文件浏览按钮
            dlg_spec1 = self.dlg_spec.wxWindowNR.Button
            # 判断是否有选择铺层Excel文件弹窗，如果没有再次点击选择铺层Excel文件对应的浏览按钮
            Check_winControl("选择Excel铺层文件", dlg_spec1).window_WhetherOpen()  # 判断预期窗口是否出现
            # 在保存和选择文件路径弹窗中操作
            parWin2_Dicti = {"窗口标题": "选择Excel铺层文件", "关闭窗口控件名称": "打开", "关闭窗口控件操作方法": "click",
                             "地址": location, "文件夹输入状态": "文件名", "文件夹输入内容": "PlyLibDb_352_541.xlsx"}
            ControlOperationSuite(None).SelectFile_Popover(parWin2_Dicti)
        if param2 != "默认":
            time.sleep(0.1)
            # 铺层数据保存路径浏览按钮
            dlg_spec2 = self.dlg_spec.wxWindowNR2.Button2
            # 判断是否有选择铺层数据保存路径弹窗，如果没有再次点击铺层数据保存路径对应的浏览按钮
            Check_winControl("选择铺层数据库保存路径", dlg_spec2).window_WhetherOpen()  # 判断预期窗口是否出现
            # 判断有没有确认另存为窗口，有就点击“确定”按钮，没有就不做操作
            # 在保存和选择文件路径弹窗中操作
            parWin1_Dicti = {"窗口标题": "选择铺层数据库保存路径", "关闭窗口控件名称": "保存", "关闭窗口控件操作方法": "click",
                             "地址": location, "文件夹输入内容": "plylib.db"}
            nestWin_Dicti = {"嵌套窗口标题": "确认另存为", "嵌套控件名称": "是", "嵌套控件操作方法": "click"}
            ControlOperationSuite(None).SelectFile_Popover(parWin1_Dicti, "检查", nestWin_Dicti)
            time.sleep(0.1)
        if param3 != "默认" or param1 != "默认":
            # 选择铺层Excel文件文本框
            if param1 != "默认":
                dlg_spec3 = self.dlg_spec.Dialog.Edit
                Check_winControl(None, dlg_spec3).Verify_inputBox(param1)
            else:
                dlg_spec4 = self.dlg_spec.wxWindowNR.Edit
                if else1 == "拼接路径":  # 拼接路径
                    param3 = location + param3
                Check_winControl(None, dlg_spec4).Verify_inputBox(param3)
        if param4 != "默认" or param2 != "默认":
            # 铺层数据保存路径文本框
            if param2 != "默认":
                dlg_spec5 = self.dlg_spec.Dialog.Edit2
                # # 判断铺层数据保存路径对应的选择文件窗口是否存在，如果存在返回铺层数据保存路径文本框中的文本
                # edit_box2 = instrument().control_WhetherExist(dlg_spec5, "铺层数据保存路径文本框", "window_text")
                # edit_box["铺层数据保存路径浏览对应文本框实际"] = edit_box2
            else:
                dlg_spec6 = self.dlg_spec.wxWindowNR.Edit2
                # 拼接路径
                if else1 == "拼接路径":
                    param4 = location + param4
                Check_winControl(None, dlg_spec6).Verify_inputBox(param4)
        # if param5 != "默认":
        #     time.sleep(0.1)
        #     #模板文件按钮
        #     dlg_spec7=self.dlg_spec.模板文件.click()
        #     # 判断是否有选择铺层Excel文件弹窗，如果没有再次点击选择铺层Excel文件对应的浏览按钮
        #     instrument().window_WhetherExist(dlg_spec7, app, "ply_example_for_aerocheck.xls",3,5)
        #     time.sleep(param5_time)
        if param6 != "默认":
            time.sleep(1)
            if messageType == "警告弹窗":  # 预期点击开始制作按钮后会弹出警告弹窗
                # 开始制作按钮
                dlg_spec6 = self.dlg_spec.开始制作Button
                Check_winControl("警告", dlg_spec6).window_WhetherOpen()  # 判断预期窗口是否出现
            else:
                # dlg_spec6 = dlg_spec.开始制作Button.check()
                # 关闭警告窗口
                Check_winControl("铺层数据库制作工具", "关闭").popUp_Whether_close()
            time.sleep(param6_time)
        if param7 != "默认":
            time.sleep(0.1)
            # 关闭按钮
            self.dlg_spec.关闭.click()
            time.sleep(param7_time)
        return edit_box


    def editWorkingCondition_operation(self,dicti):
        """
        载荷信息--编辑工况
        :return:
        """
        param1 = dicti["新建勾选框"]
        param2 = dicti["点击全选工况按钮"]
        param3 = dicti["点击不全选工况按钮"]
        param4 = dicti["新建文本框"]
        param5 = dicti["新建确认按钮"]
        param6 = dicti["重命名前工况组合下拉框选择"]
        param7 = dicti["重命名勾选框"]
        param8 = dicti["重命名文本框"]
        param9 = dicti["重命名确认按钮"]
        param10 = dicti["检查工况组合下拉框"]
        param11 = dicti["工况组合删除按钮"]
        param12 = dicti["关闭按钮"]
        # self.dlg_spec.print_control_identifiers()
        if param1 != "默认":
           time.sleep(0.5)
           # 新建勾选框
           self.dlg_spec.RadioButton2.click()
        if param2 != "默认":
            time.sleep(0.1)
            # 点击全选工况按钮
            self.dlg_spec.Button4.click()
        if param3 != "默认" :
            time.sleep(0.1)
            # 点击不全选工况按钮
            self.dlg_spec.Button5.click()
        if param4 != "默认" :
            time.sleep(0.1)
            # 新建文本框
            if param4:
                self.dlg_spec.Edit2.set_text(param4)
        if param5 != "默认":
            time.sleep(0.5)
            # 新建确认按钮
            self.dlg_spec.Button3.click()
        if param6 != "默认":
            time.sleep(0.1)
            # 重命名前工况组合下拉框选择
            self.dlg_spec.ComboBox.select(param6).click()
        if param7 != "默认":
            time.sleep(0.1)
            # 重命名勾选框
            self.dlg_spec.RadioButton0.click()
        if param8 != "默认":
            time.sleep(0.1)
            # 重命名文本框
            if param8:
                self.dlg_spec.Edit0.set_text(param8)
        if param9 != "默认":
            time.sleep(0.1)
            # 重命名确认按钮
            self.dlg_spec.编辑工况Button2.click()
        if param10 != "默认":
            time.sleep(0.1)
            # 检查工况组合下拉框
            self.dlg_spec.ComboBox.select(param10).click()
        if param11 != "默认":
            time.sleep(0.1)
            # 工况组合删除按钮
            self.dlg_spec.编辑工况Button.click()
        if param12 != "默认":
            time.sleep(0.1)
            # 关闭按钮
            self.dlg_spec.关闭.click()



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




    def DefineAllowable_operation(self, dicti):
        """
        载荷信息--编辑工况
        :return:
        """
        from src.utils.otherMethods.controlOperationSuite import ControlOperationSuite
        param1 = dicti["拉伸对应增加按钮"]
        param2 = dicti["压缩对应增加按钮"]
        param3 = dicti["剪切对应增加按钮"]
        param4 = dicti["在选择材料许用值曲线弹窗中"]
        param5 = dicti["定义材料许用值选择结构单元按钮"]
        param6 = dicti["定义材料许用值确认按钮"]
        param7 = dicti["定义材料许用值关闭按钮"]
        # self.dlg_spec.print_control_identifiers()
        if param1 != "默认":
            time.sleep(0.1)
            # 拉伸对应增加按钮
            dlg1_spec =self.dlg_spec.Button0
            # 检查点击按钮后，应该打开的窗口是否打开
            Check_winControl("选择材料许用值曲线", dlg1_spec).window_WhetherOpen()  # 判断预期窗口是否出现
            testdicts = {"弹窗标题": "选择材料许用值曲线", "选择的值": param4}
            ControlOperationSuite(None).select_AllowableCurve(testdicts)
        if param2 != "默认":
            time.sleep(0.1)
            # 压缩对应增加按钮
            dlg2_spec = self.dlg_spec.Button2
            # 检查点击按钮后，应该打开的窗口是否打开
            Check_winControl("选择材料许用值曲线", dlg2_spec).window_WhetherOpen()  # 判断预期窗口是否出现
            testdicts = {"弹窗标题": "选择材料许用值曲线", "选择的值": param4}
            ControlOperationSuite(None).select_AllowableCurve(testdicts)
        if param3 != "默认":
            time.sleep(0.1)
            # 剪切对应增加按钮
            dlg3_spec = self.dlg_spec.Button3
            # 检查点击按钮后，应该打开的窗口是否打开
            Check_winControl("选择材料许用值曲线", dlg3_spec).window_WhetherOpen()  # 判断预期窗口是否出现
            testdicts = {"弹窗标题": "选择材料许用值曲线", "选择的值": param4}
            ControlOperationSuite(None).select_AllowableCurve(testdicts)
        if param5 != "默认":
            time.sleep(0.5)
            # 定义材料许用值选择结构单元按钮
            self.dlg_spec.child_window(title="选择结构单元", class_name="Button").click()  # 点击“选择结构单元按钮”按钮
            KeyboardMouse().selectionModel()  # 选择结构单元
        if param6 != "默认":
            time.sleep(0.1)
            # 曲线坐标文本框，第三横行X竖行
            self.dlg_spec.确认.click()
            Check_winControl("编辑材料许用值曲线", "确认").popUp_Whether_close()
            time.sleep(1)



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
