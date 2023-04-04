def fun(a,b,c):
    print("a=",a)
    print("b=",b)
    print("c=",c)

lst= [1,2,3]
#fun(lst) #报错，缺参数
fun(*lst)

dict={'d':1,"e":2,'f':3}
#fun(dict) #报错，缺参数
fun(*dict) #传了字典的键

dict2={'a':1,"b":2,'c':3}
fun(**dict2) #根据键传了字典的值

#fun(10,a=10,b=20) #报错，fun() got multiple values for argument 'a'
