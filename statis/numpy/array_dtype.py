import numpy as np
arr1=np.array([3,4,5])
print(arr1.dtype)
print('----------')

#修改第一个元素为浮点型
arr1[0] = 1.2
print(arr1)  #无法修改，程序自动四舍五入
print('----------')

#1、要么事先声明
arr1=np.array([3,4,5],dtype=np.float32)
print(arr1)
print(arr1.dtype)
arr1[0] = 1.2
print(arr1)  #可以改了
print('----------')

#2、要么转换数组类型
arr1 = np.array([3,4,5])
arr2 = np.float64(arr1)
print(arr2)