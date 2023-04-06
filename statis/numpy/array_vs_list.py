import numpy as np
list1 = [2,3,4]
arr1 = np.array([2,3,4])

#对每一个元素进行平方
#list1 **2 #报错，列表不支持这种运算
print([i**2 for i in list1])  #需要经历循环，消耗资源
print(arr1 **2) #可以直接操作