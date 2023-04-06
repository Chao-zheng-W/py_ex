#二维数组的索引
import numpy as np
arr1 = np.arange(1,13).reshape(3,4)  #本来是一维的数组，通过reshape改写成3行4列
print(arr1)

#索引0代表第一行，列相同;对多维数组，用逗号再加一个参数即可
print(arr1[2,3])  #取出12,
print(arr1[1:3, 0:3])  #同样是左闭右开，切片某一块

print(arr1[:, 2:4]) #取出整列或整行，用:代替
print(arr1[2:, :],arr1[2:, :].ndim)  #取出的仍然保留二维数组的形式
print(arr1[2, :],arr1[2, :].ndim)  #取出是一维形式


#也可以使用逻辑索引
print(arr1[[True,True,False],2] ) #取出第三列的第一个值
print(arr1[[True,True,False],2:] ) #取出第三列之后（含）的第一个值
print(arr1[:,[True,True,False,True]] )
#print(arr1[[True,True,False],[True,True,False,True]] )  报错

print('-------------------')
#取出大于4的行
arr2 = np.array([[5,6,7,8],[1,2,3,4],[9,10,11,12]])
print(arr2)
'''以下不是理想结果
print(arr2>4)  #原因是bool索引只能是一维数组
print(arr2[arr2>4])'''
print(arr2[:,0]>4)
print(arr2[arr2[:,0]>4,2:])

print('-------------------')
#取出大于4的行，即5，7，9，11；无法做到
arr3 = np.array([[5,1,7,1],[1,1,1,1],[9,1,11,1]])
print(arr3)
print(arr3[:,0]>4)
print(arr3[arr3[:,0]>4,:])