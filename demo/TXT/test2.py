
from src.utils.otherMethods.actual import Warning_PopUp,GetActual_Value



testCase_dict = {"预期值信息类型":"警告弹窗","用例编号":"aa001"}


actual_Text = GetActual_Value(testCase_dict).ActualValue_controller()

print("actual_Text:",actual_Text)