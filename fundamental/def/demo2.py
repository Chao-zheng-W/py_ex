def fun(arg1,arg2):
    print(arg1,id(arg1))
    print(arg2,id(arg2))
    arg1 = 100
    arg2.append(10)
    print(arg1,id(arg1))
    print(arg2,id(arg2))
    return arg1,arg2

n1 = 11
n2 = [22,33,44]
print(n1,id(n1))
print(n2,id(n2))
fun(n1,n2)
print(n1,id(n1)) #可以发现n1的值没有变化，原因是n1是不可变对象，函数无法改变实参n1的值。从id也可看到不在同一内存空间
print(n2,id(n2))  #n2列表是可变对象，函数体可以改变

'''无法在函数体外再调用形式参数，会报错'''
#print(arg1, id(arg1))  #name 'arg1' is not defined
#print(arg2, id(arg2))
