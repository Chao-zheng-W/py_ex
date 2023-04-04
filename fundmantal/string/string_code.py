#编码
s = '天涯共此时'
print(s.encode(encoding="GBK"))  #一个中文占两个字符
print(s.encode(encoding="UTF-8"))  #一个中文占3个字符

#解码
bytes = s.encode(encoding="GBK")
print(bytes.decode(encoding="GBK"))
#print(bytes.decode(encoding="UTF-8"))  #报错，只能解码对应格式

bytes = s.encode(encoding="UTF-8")
print(bytes.decode(encoding="UTF-8"))