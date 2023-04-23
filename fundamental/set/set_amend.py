#集合相关操作

s = {12,14,15,17}
print(12 in s)
print(12 not in s)
print(13 in s)
print(13 not in s)

#增加元素
s.add(18)
#s.add(18,19)  # add() takes exactly one argument (2 given) 报错 add只能增加1个元素
print(s)
s.update([12,13,14])  #可以添加至少一个元素
print(s)

#删除元素
s.discard(15)  #一次删除一个元素，若没有不报错
print(s)
#s.remove(15)  #一次删除一个元素，若没有会报错
s.remove(12)
print(s)
s.pop()  # 随机删除一个元素，函数里无参数
print(s)

#清空集合
s.clear()
print(s)