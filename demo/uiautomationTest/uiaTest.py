

import subprocess
import uiautomation


wc=uiautomation.WindowControl(searchDepth=1,Name='警告')

# text=wc.EditControl(searchDepth=3,ClassName="Element")

text=wc.EditControl(searchDepth=3,ControlType="ControlType.Text")

# text1=wc.Control(searchDepth=2,AutomationId="ContentText")
# text2=wc.Control(searchDepth=3,AutomationId="ContentText")
# text3=wc.Control(searchDepth=4,AutomationId="ContentText")


print(text)

# textT1=text1.TextControl()

# textT2=text2.TextControl()

# textT3=text3.TextControl()

# print("text:",textT)

# print("text1:",textT1)

# print("text2:",textT2)

# print("text3:",textT3)