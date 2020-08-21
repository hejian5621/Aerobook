
from pywinauto.application import Application
import pywinauto
mywindows = pywinauto.findwindows.find_windows(title_re=".*MyProgramTitle")

# proof that two windows are found
print(len(mywindows))

for handle in mywindows:
    print('\nhandle {}'.format(handle))

    app = Application().connect(handle=handle)
    navwin = app.window(handle=handle)






    static = app.DialogName.child_window(title_re='*警告',
            class_name_re='Static')
    print("static:",static)
    if static.exists(timeout=20): # if it opens no later than 20 sec.
        app.DialogName.OK.click()











