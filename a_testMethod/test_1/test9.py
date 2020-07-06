

from pywinauto.application import Application
from src.utils.privately_owned.ClientInitialization import *

location = r"C:\Program Files (x86)\Aerobook\bin\Aerobook.exe"

dlg_spec=ClientInitialization().open_Aerobook(location)
dlg_spec_Aerolab=ClientInitialization().open_Aerolab(dlg_spec)