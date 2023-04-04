a = 'hello python'
b = a.upper()
print(a,id(a))
print(b,id(b)) #全部改成大写，新的内存地址

c = 'hello,Python'
d = c.lower()
print(c,id(c))
print(d,id(d)) # 全部改成小写，新的内存地址

e = 'hello,Python'
f = e.swapcase()
g = e.title()
print(e,id(e))
print(f,id(f)) # 大写变小写，小写变大写
print(g,id(g)) # 把每个单词的首字母变成大写
