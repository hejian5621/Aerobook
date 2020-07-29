
import wx
class Frame1(wx.Frame):
   def __init__(self,parent,title):
        wx.Frame.__init__(self, parent, title = title, pos = (100,200), size = (200,100))
        #容纳其他组件的容器
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        text1 = wx.Button( self, wx.ID_ANY, u"开始", wx.DefaultPosition, wx.DefaultSize, 1)
        bSizer1.Add( text1, 3, wx.ALIGN_CENTER_HORIZONTAL, 4 )

        self.Show(True)
if __name__ == '__main__':
    #创建一个应用程序对象，用于消息循环
    app = wx.App()
    #创建一个窗体
    frame = Frame1(None, "Example")
    app.MainLoop()
