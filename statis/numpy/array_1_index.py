import numpy as np

arr1 = np.array([2.3,2.5,4,4.5,6])
#一维数组的单个元素索引,与列表类似
print(arr1[3])  #正序从0开始
print(arr1[-2]) #逆序从-1开始

#一维数组的多个元素索引（切片）
print(arr1[2:3])  #是一个左闭右开区间
print(arr1[2:4])
print(arr1[-3:-1])

#比较返回值的属性
print(arr1[2:3].shape)  #切片保留原来的结构，1维的向量
print(arr1[2].shape)  #直接索引得到独立的值

print('------------逻辑型索引------------')
#要取出arr1中的最后一位，用一个都是bool值的索引
print(arr1[[False,False,False,False,True]])

index = arr1 > 4  #直接进行比较就会得到bool值的索引，于是可以直接使用
print(index)
print(arr1[index])  #实际数据分析中用得更多