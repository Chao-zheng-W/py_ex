#父对象，和子类的概念
class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print("我是{0},今年{1}岁".format(self.name,self.age))

class Student(Person):  #定义Student类对象，为Person类对象的子对象
    def __init__(self,name,age,score):
        super().__init__(name,age)
        self.score = score
    def spm(self):
        print("我是{0},今年{1}岁,得分{2}".format(self.name, self.age,self.score))

stu1 = Student('张三',20,100)
stu1.info()    #继承父对象的实例方法
stu1.spm()   #使用自己的实例方法
