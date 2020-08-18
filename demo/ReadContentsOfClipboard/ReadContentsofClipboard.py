import win32clipboard as wc
import win32con

def getCopyText():
    wc.OpenClipboard()
    copy_text = wc.GetClipboardData(win32con.CF_TEXT)
    wc.CloseClipboard()
    return copy_text

# test
import chardet
print (chardet.detect(getCopyText()) )  # 找到包含中文内容的字符串编码
print (getCopyText().decode('GB2312') ) # 转码