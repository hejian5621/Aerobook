# 进入被测模块


class Entrance_module:
    """进入被测模块"""


    def __init__(self,dlg_spec):
        self.dlg_spec=dlg_spec


    def combination_Control(self, title, class_name, MenuOptions):
        """
        切换到菜单栏，并点击对应的菜单选项
        通过pywinauto框架执行
        :param title:子应用标题
        :param class_name: 子应用类名
        :param MenuOptions: 菜单选项,使用格式：r"尺寸信息->一维单元尺寸定义"
        :return:
        """
        # 从Aerobook切换到子应用
        dlg_spec1 = self.dlg_spec.child_window(auto_id="panel_Graph", control_type="System.Windows.Forms.Panel")
        dlg_spec2 = dlg_spec1.child_window(title=title, class_name=class_name)
        print(title)
        # 点击菜单选项
        dlg_spec2.menu_select(MenuOptions)
        return dlg_spec2
