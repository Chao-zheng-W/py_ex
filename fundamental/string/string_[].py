#字符串切片操作

s='hello,Python'
s1=s[:5]
s2=s[6:]
s3='!'
s4=s1+s3+s2

print(s)
print(s1,id(s1))
print(s2,id(s2))
print(s3,id(s3))
print(s4,id(s4))  #字符串是不可变序列，切片会创造新对象

print("----------[开始:结束:步长]---------")
print(s[1:5:1])  #从索引1开始，到5结束（不包括5），步长为1
print(s[::-1])  #从后往前排
print(s[-6::1]) #索引从后往前为-1开始，注意引号的个数