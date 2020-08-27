import os
import time
sourceDir = r"F:\Aerobook\src\testCase\projectFile\自动化测试相关文件"
targetDir = r"F:\Aerobook\src\testCase\projectFile\automateFile"


def copyFiles(sourceDir, targetDir):
    copyFileCounts = 0
    for f in os.listdir(sourceDir):
        sourceF = os.path.join(sourceDir, f)
        targetF = os.path.join(targetDir, f)
        if os.path.isfile(sourceF):
            # 创建目录
            if not os.path.exists(targetDir):
                os.makedirs(targetDir)
            copyFileCounts += 1
            # 文件不存在，或者存在但是大小不同，覆盖
            if not os.path.exists(targetF) or (
                    os.path.exists(targetF) and (os.path.getsize(targetF) != os.path.getsize(sourceF))):
                # 2进制文件
                open(targetF, "wb").write(open(sourceF, "rb").read())
            if os.path.isdir(sourceF):
                copyFiles(sourceF, targetF)


copyFiles(sourceDir, targetDir)