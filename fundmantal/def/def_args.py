def fun(*args): #使用*号，不限定形参的个数
    print(args)

fun(1)
fun(1,2)
fun(1,2,3,4) #输出为元组

def fun2(*a): #使用*号，不限定形参的个数
    print(a)

fun2(1)
fun2(1,2)
fun2(1,2,3,4)  #输出为元组

def fun3(**args): #使用**号，不限定关键字参数的个数
    print(args)

fun3(a=1)
fun3(a=1,b=2,c=3) #输出为字典

