

from src.utils.commonality.tool import instrument



instrument().delFile()
# 复制模板文件，并返回复制的地址
source = instrument().copyFile()

source1=str(source )


print("转化前：",source)
print("转化后：",source1)