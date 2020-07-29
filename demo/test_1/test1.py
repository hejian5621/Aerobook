import uiautomation

import os
import subprocess
import uiautomation
import time

a = r"C:\Program Files (x86)\Aerobook\bin\Aerobook.exe"

subprocess.Popen(a)


time.sleep(2)

app=uiautomation.WindowControl(searchDepth=1,Name='Aerobook平台启动器')


app.ButtonControl(Name='请求授权').Click()