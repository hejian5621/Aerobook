import win32con
from win32gui import PyMakeBuffer, SendMessage, PyGetBufferAddressAndLen, PyGetString

length = 10000

hWnd=68214
hWnd=68302

buf = PyMakeBuffer(length)
length2 = SendMessage(hWnd, win32con.WM_GETTEXT, length, buf)+1
print(length2)
buf = PyMakeBuffer(length2)
print('get: ', SendMessage(hWnd, win32con.WM_GETTEXT, length2, buf))

address, length = PyGetBufferAddressAndLen(buf)
text = PyGetString(address, length)

print('text: ', text)