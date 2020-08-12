from pymouse import PyMouse
# from pykeyboard import PyKeyboard
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

url='https://www.baidu.com/'
dr=webdriver.Chrome()
m=PyMouse()
k=PyKeyboard()    #实例化dr.get(url)

dr.find_element(By.ID,'kw').click()
k.tap_key(k.shift_key)     #转换成英文输入
k.type_string('Python')    #输入内容sleep(2)
k.tap_key(k.enter_key)     #按键盘的回车
k.tap_key(k.function_keys[5])     #刷新页面，F5
k.press_keys([k.windows_l_key,'d'])    #win+d,切换至桌面
sleep(2)
print(dr.title)
print(dr.current_url)
dr.quit()