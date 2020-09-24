
#知识点：如何自定义类
class MyException(Exception):                   #让MyException类继承Exception
    def __init__(self,name,age):
        self.name = name
        self.age = age


a=1
b=2
try:
    # 知识点：主动抛出异常，就是实例化一个异常类
    if a !=b:
        raise MyException("zhansgan","zhansgan" )  # 实例化一个异常,实例化的时候需要传参数

except MyException as obj:  # 这里体现一个封装，
    print(obj.age, obj.name)  # 捕获的就是MyException类携带过来的信息

except Exception as obj:  # 万能捕获，之前的可能捕获不到，这里添加Exception作为保底
    print(obj)
else:

    print("a不等于b")