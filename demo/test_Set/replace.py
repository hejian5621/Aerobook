

from src.utils.commonality.tool import instrument


sourceDir = r"F:\Aerobook\src\testCase\projectFile\自动化测试相关文件"
targetDir = r"F:\Aerobook\src\testCase\projectFile\automateFile"
instrument().delfolder()    # 删除已有的项目文件夹
instrument().copyFile(sourceDir, targetDir)   # 生成新的项目文件夹，并返回文件夹路径

source1=str(source )


print("转化前：",source)
print("转化后：",source1)