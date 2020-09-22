from tool import WindowTop
from config.configurationFile import ProfileDataProcessing
from src.utils.otherMethods.actual import Information_Win
from src.utils.commonality.ExcelFile import read_excel
from tool import folderFile_dispose,Check_winControl
from src.utils.otherMethods.initialize import execute_useCase_initialize
from utils.commonality.tool import UseCase_parameterization
import time





class Initializing:
    """用例执行前需要做的操作"""

    def __init__(self):
        self.testCase_attribute=None


    def controller(self,dictSet ):
        """
          在执行用例前需要要准备的操作
        dict={"全局参数":"","全局用例集名称":"","当前用例集名称":"","删除文件名列表":[],"详细地址":"","关闭弹窗":[],"控件属性已经操作方法":testCase_attribute}
        :param dictSet:
        :return:
        """
        WindowTop.EnumWindows("Aerobook v1.0.4")     # 把被测系统页面置顶
        number=dictSet["全局参数"]
        global_UseCase_Name = dictSet["全局用例集名称"]
        real_UseCase_Name = dictSet["当前用例集名称"]
        self.testCase_attribute = dictSet["控件属性已经操作方法"]
        # 在运行每一个用例集之前初始化全局变量参数
        number,global_Name = Initializing().initialize_globalVariable(number, global_UseCase_Name, real_UseCase_Name)
        # 获取项目所在路径
        ProjectPath = ProfileDataProcessing("commonality", "ProjectSave_path").config_File()
        # 用例在执行前，首先获取信息窗口的文本信息，用于获取最新的信息窗口文本信息
        old_content = Information_Win().acquire_HTML_TXT(ProjectPath)
        if "删除文件名列表" in dictSet : # 用例执行前，删除相关文件
            list_filePath = dictSet["删除文件名列表"]
            folderFile_dispose(ProjectPath).delfile(list_filePath)
        if number == 1:  # 在执行该模块第一条用例前执行下面操作
            tableName=["控件属性已经操作方法"]
            site = UseCase_parameterization().parameterization_location(real_UseCase_Name, tableName)
            site=site[0]
            self.testCase_attribute = read_excel(site).readExcel_ControlProperties()  # 读取该测试用例中控件的操作属性
            if real_UseCase_Name=="载荷信息--编辑工况":
                execute_useCase_initialize().clear_editWorkingCondition()    # 清除所有的包络工况
        if "关闭弹窗" in dictSet: # 关闭没有关闭的弹窗
            list_CloseWindows = dictSet["关闭弹窗"]
            for CloseWindows in list_CloseWindows:
                title=CloseWindows[0]
                button_name=CloseWindows[1]
                Check_winControl(title, button_name).popUp_Whether_close()
        return number,global_Name,ProjectPath,old_content,self.testCase_attribute



    def initialize_globalVariable(self,reset_arg,global_UseCase_Name,real_UseCase_Name):
        """
        在每一次运行用例集之前都初始化一次全局变量
        :param reset_arg: 需要初始化得参数
        :param global_UseCase_Name: 全局变量的用例集名称
        :param real_UseCase_Name:  正在执行用例集的用例集名称
        :return:
        """
        if global_UseCase_Name==real_UseCase_Name:
            real_arg=reset_arg+1
        else:
            global_UseCase_Name = real_UseCase_Name
            real_arg =1
        return real_arg,global_UseCase_Name


class finish_clear:
    """结束清理"""

    def controller(self, dictSet):
        """
        用例执行结束后，所作的清理工作
        :param dictSet:{"预期值信息类型":"","信息窗口之前的文本":"","实际值":"","预期值":[],"详细地址":"","关闭弹窗":[]}
        :return:
        """
        from src.utils.otherMethods.dataFormatConversion import FormatConversion
        messageType=dictSet["预期值信息类型"]
        actual_result = dictSet["实际值"]
        expect_result = dictSet["预期值"]
        """ 收尾，如果有警告弹框就关掉"""
        list_CloseWindows = [["铺层数据库制作工具", "关闭"],["警告", "OK"],["错误", "确定"],["编辑工况", "关闭"]]
        for CloseWindows in list_CloseWindows:
            title = CloseWindows[0]
            button_name = CloseWindows[1]
            Check_winControl(title, button_name).popUp_Whether_close()
        """取出Excel里面的值"""
        """处理预期结果或实际结果，用以实际结果和预期结果文本对比"""
        if messageType == "信息窗口":  # 如果预期值在信息窗口，就通过以下方法获取最新的信息窗口文本信息
            old_content=dictSet["信息窗口之前的文本"]
            actual_result = FormatConversion().GetLatestData(actual_result, old_content)
        # 格式化实际值跟预期值
        if type(actual_result) == list:  # 实际值如果是列表，就转化成字符串
            actual_result = ' '.join(actual_result)
        if actual_result:  # 如果实际值不为空
            expect_result = expect_result.strip()  # 去掉预期值，前后的空格
            actual_result = actual_result.strip()  # 去掉实际值，前后的空格
        return  expect_result,actual_result


