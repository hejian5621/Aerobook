import os
import time
import shutil




class kk:



    def CopyFiles(self,sourceDir, targetDir):
        # 完全连子目录也会复制好，美观

        copyFileCounts = 0
        for f in os.listdir(sourceDir):
            sourceF = os.path.join(sourceDir, f)
            targetF = os.path.join(targetDir, f)
            if os.path.isfile(sourceF):
                if not os.path.exists(targetDir):
                    os.makedirs(targetDir)
                copyFileCounts += 1
                if not os.path.exists(targetF) or (
                        os.path.exists(targetF) and (os.path.getsize(targetF) != os.path.getsize(sourceF))):
                    open(targetF, "wb").write(open(sourceF, "rb").read())
            if os.path.isdir(sourceF):
                kk().CopyFiles(sourceF, targetF)


#
# sourceDir = r"F:\Aerobook\src\testCase\projectFile\自动化测试相关文件"
# targetDir = r"F:\Aerobook\src\testCase\projectFile\automateFile"
# # print("总共有",i,"图层文件被复制！")
# kk().CopyFiles1(sourceDir, targetDir)