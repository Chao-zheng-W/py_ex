try:
    a = int(input('输入一个整数'))
    b = int(input('输入一个整数'))
    result = a / b
except ZeroDivisionError:
    print('除数不能为0')
else:
    print('a/b的结果是：' + result)
finally:
    print('谢谢参与')
