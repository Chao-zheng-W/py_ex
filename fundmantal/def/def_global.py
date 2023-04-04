def fun():
    c=20 #c在函数体内，称为局部变量，无法在函数外调用
    print(c)

fun()
#print(c)
#报错：name 'c' is not defined
