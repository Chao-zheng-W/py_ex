#元组的遍历

t = ("hello",'world',98)

#使用索引
print(t[0])
print(t[1])
print(t[2])
#print(t[3])  # 报错tuple index out of range

#使用for循环遍历
for item in t:
    print(item)