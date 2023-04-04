def calc(a,b):  #a,b 为形式参数，简称形参。
    c=a+b
    return c

result = calc(10,20)  #10，20为实际参数，简称实参
print(result) #参数传递的第一种方法：对应位置

res = calc(b=20,a=10) #参数传递的第二种方法。等号左边称为：关键字参数。
print(res)