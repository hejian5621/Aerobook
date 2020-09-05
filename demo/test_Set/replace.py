

from tool import folderFile_dispose


sourceDir = r"F:\Aerobook\src\testCase\projectFile\自动化测试相关文件"
targetDir = r"F:\Aerobook\src\testCase\projectFile\automateFile"
folderFile_dispose(sourceDir ).delfolder()    # 删除已有的项目文件夹
folderFile_dispose(sourceDir).copyFile(targetDir)   # 生成新的项目文件夹，并返回文件夹路径

