
# import uiautomation
# # Use = uiautomation.WindowControl(searchDepth=1, Name="警告")  # 连接Aerobook窗口
# # 点击切换窗口按钮
# # app=Use.TextControl(searchDepth=6, Name="请选择结构单元")
#
#
# window = uiautomation.WindowControl(Name="警告", searchDepth=1)
#
# window1=window.Control(searchDepth=2,AutomationId="-31624")
#
#
# window1.Click()

# alert_info =window1.ClassName

# app = window.Control(searchDepth=1,ClassName='DirectUIHWND')


# app = window.Control(searchDepth=2,ClassName='DirectUIHWND')


# app = window.Control(searchDepth=4,ClassName='DirectUIHWND')


# alert_info =app.Name

# app.TextControl(searchDepth=2,ClassName='Element')


# alert_info = text_element.Name
#
# print("alert_info:",window1)

# ContentText


import win32gui,win32api,win32con

# 获得父容器
pHwnd = win32gui.FindWindow(None, '警告')

# hwnd=win32gui.FindWindow(None,"wxWindowNR")

print("pHwnd",pHwnd)

# 获取子容器,识别结果输入框
edtextHwnd = win32gui.FindWindowEx(pHwnd, None, 'Edit', '')

# buf_size = win32gui.SendMessage(edtextHwnd, win32con.WM_GETTEXTLENGTH, 0, 0) + 1  # 要加上截尾的字节
# str_buffer = win32gui.PyMakeBuffer(buf_size)  # 生成buffer对象
# win32api.SendMessage(edtextHwnd, win32con.WM_GETTEXT, buf_size, str_buffer)  # 获取buffer
# print(str_buffer[:-1])
# str = str(str_buffer[:-1])  # 转为字符串
# result = str




# 获取识别结果中输入框文本
length = win32gui.SendMessage(edtextHwnd, win32con.WM_GETTEXTLENGTH)+1
buf = win32gui.PyMakeBuffer(length)
#发送获取文本请求
win32api.SendMessage(edtextHwnd, win32con.WM_GETTEXT, length, buf)
#下面应该是将内存读取文本
address, length = win32gui.PyGetBufferAddressAndLen(buf[:-1])
text = win32gui.PyGetString(address, length)

print("text:",text)
