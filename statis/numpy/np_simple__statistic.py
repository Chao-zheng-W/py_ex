import numpy as np
arr1 = np.random.randint(1,10,(3,4))  #random随机数，randint随机1-10的整形，构成3行4列的数组
print(arr1)

arr2=arr1.argsort(axis=0)  #axis代表在列方向排序
print(arr2) #会返回数组大小的下标，或者索引，

arr1.sort(axis=0)
print(arr1)  #直接作用在原数组，axis代表在列方向排序
arr1.sort(axis=1)
print(arr1)

arr3=np.tile(arr1,2)
print(arr3)  #对整个数组复制两次
arr4=np.repeat(arr1,2,axis=1)
print(arr4)  #对元素复制两次

print(arr1.mean()) #返回整个数组平均值
print(arr1.mean(axis=0))  #按列返回数组平均值

print(arr1.max(axis=1))  #按行返回最大值
print(arr1.argmax(axis=1)) #返回最大值的索引