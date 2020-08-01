
from src.utils.otherMethods.control_except import combination_Control
from src.utils.otherMethods.ClientInitialization import ConnectApp
from src.utils.operation.Placement_majorization import laminate_WorkField

dicti = {"最大铺层数": "50", "最小铺层数": "30", "铺层比一": "3", "铺层比二": "5", "铺层比三": "2",
         "容差比": "6", "单层厚度": "0.25", "弹性模量E11": "165000", "弹性模量E22": "8000", "泊松比v12": "0.50",
         "剪切模量G12": "4500", "层合板长度": "800", "层合板宽度": "300", "Mat8材料ID": "3", "数据库名称": "330",
         "保存为铺层数据库": "1", "保存为Excel文件": "1", "路径": "C:\\Users\Administrator\Desktop\aro\aro2", "求解": "1", "关闭": "1"}


dlg_spec=ConnectApp('Aerobook v1.0.4').pyw_Connect()
workField=laminate_WorkField(dlg_spec).enterInto()
laminate_WorkField(workField).ControlOperating(dicti)