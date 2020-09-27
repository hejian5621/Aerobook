
from tool import folderFile_dispose
import os,datetime

ProjectPath=r"F:\Aerobook\src\testCase\projectFile\automateFile"

list_fileNames=folderFile_dispose(ProjectPath).FetchFileName("2020-09-27 17:30:40")





print(list_fileNames)

print(type(list_fileNames))


str1=str(list_fileNames)


print(type(str1))
print(str1)