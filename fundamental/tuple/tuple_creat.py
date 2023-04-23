t1 = (10,20,30)
t2 = tuple((10,[12,14,15],20))

#元组是不可变对象，元素为可变时，才可变，且引用不改变
print(t1[1],type(t1[1]))
#t2[1] = 100  #报错'tuple' object does not support item assignment，不可改动
print(t2[1],type(t2[1]),id(t2[1]))
t2[1].append(100)
print(t2[1],type(t2[1]),id(t2[1]))  # 列表本身可变，引用id不变化
