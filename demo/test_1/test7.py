
import os
import subprocess
import uiautomation
import uiautomation as auto
import time

a = r"E:\Program Files (x86)\Aerobook\bin\Aerobook.exe"
# 打开Aerobook
subprocess.Popen(a)


window1 = uiautomation.WindowControl(searchDepth=1, Name='Aerobook平台启动器') # 找到Aerobook平台主窗口

sub1 = window1.Control(searchDepth=1, Name='本地授权')    # 找到本地授权控件
sub1.ButtonControl(searchDepth=1, Name='请求授权').Click()  # 找到请求授权按钮

time.sleep(1)

sub2 = window1.Control(searchDepth=1, Name='成功')    # 找到成功按钮
print(sub2.Name)
sub2.ButtonControl(searchDepth=1, Name='确定').Click()  # 找到确认按钮并点击

window1.ButtonControl(searchDepth=1, Name='运行').Click()   # 点击运行按钮

time.sleep(5)
window2 = uiautomation.WindowControl(searchDepth=1, Name='Aerobook v1.0.4') # 找到Aerobook平台主窗口
window2.ButtonControl(searchDepth=2, Name='最大化').Click()
sub3 = window2.Control(searchDepth=1, Name='正在启动应用程序，需要一定的时间，请耐心等待...', className="WindowsForms10.Window.8.app.0.141b42a_r9_ad1")  # 找到成功按钮
print(sub3.Name)
sub4 = sub3.Control(searchDepth=1, Name='The Ribbon')    # 找到成功按钮
print(sub4.Name)
sub5 = sub4.Control(searchDepth=1, Name='Ribbon Tabs')    # 找到成功按钮
print(sub5.Name)
sub5.TabItemControl(searchDepth=1, Name='Fembook').Click()
handle 