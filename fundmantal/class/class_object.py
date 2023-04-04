#object是所有对象的父对象，默认继承属性和方法
class Student:
    pass

stu1= Student()
print(dir(stu1))
print(stu1)  #直接打印，默认调用__str__，输出内存地址

class Student2:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return "我是%s，今年%d岁" % (self.name,self.age)

stu2= Student2('张三',20)
print(stu2)  #实际开发中，常改写__str__，达到直接输出自定义的效果