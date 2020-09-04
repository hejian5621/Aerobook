from src.utils.commonality.tool import pictureProcessing,KeyboardMouse


"""在Aerobook--Aerocheck的图形区通过键盘和鼠标的操作方式选中全部的结构单元"""

# KeyboardMouse().selectionModel()  # 选择结构单元



"""API获取图片信息"""

location=r"F:\Aerobook\src\testCase\d_useCase_screenshot\1.png"

actuals=pictureProcessing(location).screenshot()

print("actuals:",actuals)




