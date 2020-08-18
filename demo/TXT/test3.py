
n = -1;t=1

dataQuantity=320
txtName="cache.txt"
actuals=""


# 去掉缓存TXT文件里的空行
with open(txtName, "r") as f:  # 打开文件
    lines = f.readlines()  # 读取所有行
    while True:
        if "\n"  in lines:
            lines.remove("\n")
        else:
            break
number=len(lines)  # 获取列表元素的个数

n=0
actuals=""
# 取出TXT文件中需要的数据
while n<dataQuantity :
    line =dataQuantity-n
    t=number-line
    if t >= 0:
        actual= lines[t]
        actual = actual[23:]
        actuals=str(actuals)+str(actual)
    n=n+1





print("actuals:",actuals)


# while t>= -dataQuantity+2:
#     actual = None
#     n = -t + n
#     print("n:", n)
#     while True:
#
#             last_line = lines[n]  # 取最后一行
#             if last_line != "\n":
#                 break
#         n = n + (-1)
#     t = t + (-1)
#     # 去掉时间
#     actual = last_line[23:]
#     actuals = str(actuals) + str(actual)
# print("actuals:", actuals)
# 删除TXT文件
# if os.path.exists(txtName): os.remove(txtName)






