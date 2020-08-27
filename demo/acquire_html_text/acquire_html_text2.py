# 把html格式的文件转化成文本，只留下中文存入TXT格式文件中

import re
import string


with open("Aerocheck_prjLog_2020-08-26.html","r",encoding="utf-8") as strf:
 str = strf.read()




res = r'(?<=<strong>).*?(?=</strong><br /><hr />)'
res1 = r'(?<=<span style="color:#bb3d00;">).*?(?=</span>)'
res12=r'<span style='
li = re.findall(res,str)

li3=[]

for li1 in li:
    if res12 in li1:
        li2 = re.findall(res1,li1)
        if li2 :
            print("li2:",li2)
            li2=li2[0]
            li3.append(li2)
    else:
        li3.append(li1)

    with open("new.txt","w") as wstr:

     for s in li3:
      wstr.write(s)
      wstr.write("")
      wstr.write("\n")

  # print(s,"")
content=None

list2=[]

with open('new.txt', 'r') as f:
 content = list(f)
 print(content)

list2=[]

for con in content:
    zhmodel = re.compile(u'[\u4e00-\u9fa5]')  # 检查中文
    # zhmodel = re.compile(u'[^\u4e00-\u9fa5]')  #检查非中文

    match = zhmodel.search(con)
    if match:
        con.lstrip('<span style="color:#bb3d00;">')
        con.lstrip('</span>')
        list2.append(con)





filename = 'test_text.txt'
with open(filename, 'w') as file_object:
    for li in list2:
     file_object.write(li)



