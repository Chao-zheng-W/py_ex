#集合的数学操作
s1 = {15,16,17,18}
s2 = {13,14,15,16}

#交集
print(s1.intersection(s2))
print(s1 & s2)
#并集
print(s1.union(s2))
print(s1 | s2)
#差集
print(s1.difference(s2))  #用s1集合减去s2
print(s1 - s2)
#对称集
print(s1.symmetric_difference(s2))  #两元素并集减去交集
print(s1 ^ s2)