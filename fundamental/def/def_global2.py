def fun2():
    global c  #声明为全局变量
    c=20 #
    print(c)

fun2()  #调用函数后，全局变量可以使用，否则报错
print(c)