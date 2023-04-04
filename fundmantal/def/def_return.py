def fun1(num):
    odd =[]
    even =[]
    for i in num:
        if i%2:
            odd.append(i)
        else:
            even.append(i)
    return odd,even  #函数返回结果是元组

s = [1,2,3,4,5,6,7,8,9]
print(fun1(s))  #写一个函数，把奇数偶数分开。

def fun2():
    print("hello")
fun2() #函数本身功能是打印，无需返回

def fun3():
    return "hello",'world'

fun3() #有返回值，需要print参与打印出来
print(fun3())

#是否需要返回值，视情况而定