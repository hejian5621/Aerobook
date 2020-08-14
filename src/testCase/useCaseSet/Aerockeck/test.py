# last_line=None
# n=-1
#
# while True:
#     with open('1.txt', 'r') as f:  # 打开文件
#         lines = f.readlines()  # 读取所有行
#         last_line = lines[n]  # 取最后一行
#         if last_line!="\n":
#             break
#     n =n + (-1)
#     print(n)
#
# print("last_line",last_line)
#
# # with open('1.txt', 'r') as f:  # 打开文件
# #     lines = f.readlines()  # 读取所有行
# #     last_line = lines[-2]  # 取最后一行
# # print(last_line)
last_line="[2020-08-13 17:56:14]: 请检查界面参数!"

actual=last_line[23:]
print("last_line:", actual)