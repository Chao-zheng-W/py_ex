s1 = {12,13,14,15,17}
s2 = {12,14,15,13,17}
s3 = {12,13}
s4 = {15,18}

#判断集合是否不相等
print(s1 != s2)  # False
print(s3 != s4)  # True

#判断集合是否相等
print(s1 == s2)  # True
print(s3 == s4)  # False

#判断两个集合是否没有交集
print(s1.isdisjoint(s2)) # False

#判断集合是否是另一个的子集
print(s3.issubset(s1))  # True

#判断集合是否是另一个的超集
print(s1.issuperset(s2))  # True
print(s1.issuperset(s3))  # True