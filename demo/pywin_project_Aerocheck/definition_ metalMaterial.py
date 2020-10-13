

from src.utils.otherMethods.initialize import pywin_openAProgram



testdicts={"所在模块":"材料信息->定义金属材料参数"}

module="Aerobook-Aerocheck"
aero_window, module_window = pywin_openAProgram(module).menuOpen(testdicts)


workField1 = module_window.scrolledpanelwxWindowNR2   # 切换到被测工作


workField1.print_control_identifiers()


#拉伸许用应力文本框
workField1.Edit1.set_text("222")


#压缩许用应力文本框
workField1.Edit2.set_text("222")


#剪切许用应力文本框
workField1.Edit3.set_text("222")

#环向许用应力文本框
workField1.Edit4.set_text("222")

#拉伸极限文本框
workField1.Edit5.set_text("222")

#屈服强度文本框
workField1.Edit6.set_text("222")

#剪切强度文本框
workField1.Edit7.set_text("222")

#选择结构单元按钮文本框
workField1.child_window(title="选择结构单元", class_name="Button").click_input()

#确认按钮文本框
workField1.Button2.click_input()