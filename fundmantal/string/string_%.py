#格式化字符串
#（1）% 占位符
name ='张三'
age = 20
print('我叫%s，今年%d岁' % (name,age))  # %s占位字符串，%d占位整数，%f占位浮点

#（2）{} 占位符
print('我叫{0}，今年{1}岁'.format(name,age)) #{0}和{1}代表索引顺序

#（3）f-string
print(f'我叫{name}，今年{age}岁')

'''规定宽度和精度'''
print('%d' % 99)
print('%10d' % 99) #规定宽度为10
print('%.3f' % 3.1415926) #规定精度为小数点后3
print('%10.3f' % 3.1415926) #同时规定宽度和精度
print('hellohello')

print("{0:.3}".format(3.1415926))  #表示截取3位
print("{0:.3f}".format(3.1415926))  #表示3位小数
print("{0:10.3f}".format(3.1415926))  #表示3位小数，10位宽度