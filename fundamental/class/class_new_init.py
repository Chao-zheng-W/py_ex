class Person():
    def __new__(cls, *args, **kwargs):  #创建实例对象时调用该函数
        print("__new__方法被调用了,cls的id是{0}".format(id(cls)))  #cls与Person类对象参数传递
        obj = super().__new__(cls)  #obj与self，p1进行参数传递，所以内存地址一致
        print("__new__方法被调用了,obj的id是{0}".format(id(obj)))
        return obj

    def __init__(self,name,age):  #obj与self，p1进行参数传递，所以内存地址一致
        print("__init__被调用了，self的id是{0}".format(id(self)))
        self.name = name
        self.age = age

print("Person类对象的id是{0}".format(id(Person)))  #程序先运行这条代码

p1 = Person("张三",20)
print("p1的id是{0}".format(id(p1)))

