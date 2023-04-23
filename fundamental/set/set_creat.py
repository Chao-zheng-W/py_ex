#集合是没有键的字典
#创建集合

s = {121,32,23,432,32}
print(s)    #重复的元素会去掉，且与顺序无关

s1 = set((12,23,"hello",32,"hello"))
print(s1)

#通过函数set可以把元组，列表，字符串转变为集合
print(set([1,2,3,4,5]))
print(set(range(6)))
print(set("python"))

#创建空集合
s2 = {}
print(s2,type(s2))  # 直接花括号产生空字典
s3 = set()
print(s3,type(s3))  # 用函数产生空集合

#复习：列表生成式
print([ i*i for i in range(9)])
#集合生成式
print({ i*i for i in range(9)})

