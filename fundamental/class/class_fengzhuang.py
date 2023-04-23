class Student:
    def __init__(self,name,age):
        Student.name = name
        Student.__age = age  #不希望在类对象外被使用，加两个_

stu = Student('张三',20)
print(stu.name)
#print(stu.age) 报错，无法使用
#print(stu.__age)  报错，无法使用

#这是一个君子协定，要使用也可以，如下
print(dir(stu)) #先获取属性准确的名称
print(stu._Student__age)  #接着就可以使用