# 获取测试用例

from tool import MyException
import  os,sys
from utils.commonality.tool import UseCase_parameterization


class getTestCase:
    """获取测试用例"""

    def __init__(self,moduleName):
        self.moduleName=moduleName
        self.list_dict_site=None
        self.list_testPoint=None

    def  console(self):
        """
        控制读取Aerocheck、Aerocheck等模块用例
        :return:
        """
        if self.moduleName=="Aerobook-Aerocheck":
            self.list_dict_site, self.list_testPoint=getTestCase(self.moduleName).Aerocheck_testCase()
        elif self.moduleName=="aerobook-Fiberbook":
            pass
        elif self.moduleName=="Fembook":
            pass
        else:
            raise MyException("没有找到执行模块的用例：%r"%self.moduleName)
        return self.list_dict_site, self.list_testPoint


    def Aerocheck_testCase(self):
        """
        获取Aerocheck测试用例
        :return:
        """
        # # 用于控制被测模块的测试，字典的键为模块名称，嵌套的列表为表名称
        # list_dicti_argument=[
        #     {"铺层信息--铺层库优化":["最大铺层数","最小铺层数","铺层比","容差比","单层厚度","弹性模量E11(MPa)","弹性模量E22（MPa）","泊松比v12","剪切模量G12（MPa）",
        #                        "层合板长度a(mm)","层合板宽度b(mm)","Mat8材料ID","数据库名称","路径文本框","Mat8材料ID","保存为铺层数据库和保存为Excel勾选框"]},
        #     {"铺层信息--铺层数据库制作工具":["铺层库制作弹窗", "选择铺层Excel文件", "铺层数据保存路径文本框"]},
        #     {"尺寸信息--一维单元尺寸定义": ["一维单元尺寸定义截面形状T型"]},
        #     {"尺寸信息--二维单元尺寸定义": ["二维单元尺寸定义"]},
        #     {"尺寸信息--一维单元尺寸定义（模板）":["铺层库制作弹窗", "选择铺层Excel文件", "铺层数据保存路径文本框"]},
        #     {"尺寸信息--二维单元尺寸定义（模板）":["一维单元尺寸定义复合材料（模板）", "一维单元尺寸定义金属材料（模板）", "二维单元尺寸定义金属材料（模板）","二维单元尺寸定义金属材料（模板）"]},
        #     {"求解计算--求解计算":["属性更新选择路径",  "载荷提取选择路径"]},
        #     {"载荷信息--载荷数据库制作工具": ["载荷数据库制作弹窗", "选择载荷文件","载荷数据库保存路径"]},
        #     {"载荷信息--编辑工况": ["新建", "重命名"]},
        #     {"材料信息--定义复合材料参数": ["其他"]},
        #     {"复材结构强度校核--复合材料强度校核1D": ["其他"]},
        #     {"复材结构强度校核--复合材料强度校核2D": ["其他"]},
        #     {"紧固件强度校核--紧固件信息输入": ["测试"]},
        #     {"紧固件强度校核--紧固件参数设置": ["其他"]},
        #     {"紧固件强度校核--紧固件强度校核": ["其他"]},
        #     {"紧固件优化--紧固件参数优化": ["其他"]},
        #     {"材料信息--定义金属材料参数": ["其他"]},
        #     {"金属结构强度校核--金属一维单元强度校核": ["其他"]},
        #     {"金属结构强度校核--金属二维单元强度校核": ["其他"]},
        #     {"金属结构强度校核--金属加筋板强度校核": ["其他"]}
        # ]

        # list_dicti_argument=[
        #     {"铺层信息--铺层库优化": ["测试一"]},          {"铺层信息--铺层数据库制作工具": ["测试一"]},              {"尺寸信息--一维单元尺寸定义": ["测试一"]},
        #     {"尺寸信息--二维单元尺寸定义": ["测试一"]},     {"尺寸信息--一维单元尺寸定义（模板）": ["测试一"]},         {"尺寸信息--二维单元尺寸定义（模板）": ["测试一"]},
        #     {"求解计算--求解计算": ["测试一"]},            {"载荷信息--载荷数据库制作工具": ["测试一"]},              {"载荷信息--编辑工况": ["测试一"]},
        #     {"材料信息--定义复合材料参数": ["其他"]},       {"复材结构强度校核--复合材料强度校核1D": ["测试一"]},      {"复材结构强度校核--复合材料强度校核2D": ["测试一"]},
        #     {"紧固件强度校核--紧固件信息输入": ["测试一"]},  {"紧固件强度校核--紧固件参数设置": ["测试一"]},           {"紧固件强度校核--紧固件强度校核": ["测试一"]},
        #     {"紧固件优化--紧固件参数优化": ["测试一"]},     {"材料信息--定义金属材料参数": ["测试一"]},               {"金属结构强度校核--金属一维单元强度校核":["测试一"]},
        #     {"金属结构强度校核--金属二维单元强度校核": ["测试一"]},    {"金属结构强度校核--金属加筋板强度校核": ["测试一"]}  ]

        list_dicti_argument = [
            {"铺层信息--铺层数据库制作工具": ["测试一"]},
            {"尺寸信息--一维单元尺寸定义": ["测试一"]}
        ]
        # 读取测试用例
        self.list_dict_site, self.list_testPoint = UseCase_parameterization().parameterization_data(self.moduleName,list_dicti_argument)
        return self.list_dict_site, self.list_testPoint