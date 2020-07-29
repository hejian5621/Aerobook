

from pywinauto.application import Application


app = Application(backend="uia").connect(process=15000)

Aerobook_main = app.window(title=r'Aerobook v1.0.4')



Aerobook_main1=Aerobook_main.child_window(title_re="splitter", class_name="WindowsForms10.Window.8.app.0.141b42a_r9_ad1")




print(Aerobook_main1.print_control_identifiers())
