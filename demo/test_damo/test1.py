#!/usr/bin/python3

import _thread
import time

# 为线程定义一个函数
def print_time(threadName):
   print(threadName)

# 为线程定义一个函数
def print_time1(threadName):
   print(threadName)

# 创建两个线程
try:
   _thread.start_new_thread( print_time, ("Thread-1" ,) )
   print("1")
   _thread.start_new_thread( print_time1, ("Thread-2" ,) )
   print("2")
except:
   print ("Error: 无法启动线程")

while 1:
   pass

# 依次阻塞所有线程
for thread in threads:
    thread.join()