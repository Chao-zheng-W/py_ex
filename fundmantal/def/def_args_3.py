'''需求：c,d只能用关键字实参传递'''
def fun(a,b,*,c,d):
    print("a=",a)
    print("b=",b)
    print("c=",c)
    print("d=",d)

#fun(10,20,30,40)   #报错：fun() takes 2 positional arguments but 4 were given
fun(10,20,c=30,d=40)  #实现需求

def fun2(a,b,*e,c,d):
    print("a=",a)
    print("b=",b)
    print("c=",c)
    print("d=",d)
    print(e)

#fun2(1,2,3,4,5,6) #报错：fun2() missing 2 required keyword-only arguments: 'c' and 'd'
fun2(1,2,3,4,c=5,d=6)

# def fun2(**e,a,b,c,d,):
'''个数可变的关键字形参位置，只能放在最后，否则报错
但是个数可变的位置形参，不会报错，如第11行'''