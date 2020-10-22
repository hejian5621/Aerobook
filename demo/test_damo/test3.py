from src.utils.otherMethods.dataFormatConversion import FormatConversion
from utils.otherMethods.unittest_start_finish import handlingMethod


# allTime=['2020-10-22 09:35:02', '2020-10-22 09:35:03','2020-10-22 09:35:04','2020-10-22 09:35:05','2020-10-22 09:35:06','2020-10-22 09:35:07','2020-10-22 09:35:08',
#          '2020-10-22 09:35:09','2020-10-22 09:35:10','2020-10-22 09:35:11','2020-10-22 09:35:12','2020-10-22 09:35:13']
#
# oldTime="2020-10-22 09:35:11"
#
# timeAmount = FormatConversion().greater_oldTime(allTime, oldTime)
#
# print("timeAmount:",timeAmount)
ProjectPath=r"F:\Aerobook\src\testCase\projectFile\automateFile"

newTime,allTime = handlingMethod().infoWin_new_dateAndTime(ProjectPath)  # 取出信息窗口最新的时间

print("newTime:",newTime)
print("allTime:",allTime)