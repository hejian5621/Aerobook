
from pywinauto.application import Application
#打印出所有的菜单项，由于菜单可能是多级，所以得采用递归
def ShowMenus(MenuItem, Spaces = ""):
    if None == MenuItem:
        return
    Spaces = Spaces + "  "
    for Item in MenuItem.Items():
        if (2048 != Item.Type()):
            print(Spaces + Item.Text())
        SubMenu = Item.SubMenu()
        if None != SubMenu:
            ShowMenus(SubMenu, Spaces)

if __name__ == "__main__":
    # 应用程序的地址
    a = r"C:\Program Files (x86)\Aerobook\bin\Aerobook.exe"
    # 打开应用程序
    app = Application().start(a)
    # 选择应用程序
    dlg_spec = app.window(title=r'Aerobook平台启动器').window(title=r'本地授权')
    # 点击请求授权
    dlg_spec.child_window(title="请求授权").click()
    # 切换到授权成功窗口
    dlg_spec1 = app.window(title=r'成功')
    # 点击确定按钮Aerobook平台启动器
    dlg_spec1.child_window(title="确定").click()
    # 切回到Aerobook平台启动器窗口并点击运行按钮
    app.window(title=r'Aerobook平台启动器').window(title=r'运行').click()
    # 切换到Aerobook主窗口
    Aerobook_main = app.window(title=r'Aerobook v1.0.4').window(title=r'正在启动应用程序，需要一定的时间，请耐心等待...')
    # 取得当前程序对话框窗口
