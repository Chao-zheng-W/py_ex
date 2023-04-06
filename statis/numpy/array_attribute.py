import numpy as np
arr1 = np.array([0.3,4.5,2.5]) #用列表形式，创建一个数组
arr2 = np.array([[3,4,2],[5,2,3]]) #创建了一个2行3列的数组

print(arr1,type(arr1))
print(arr2,type(arr2)) #是一个新类：numpy.ndarray

#具有一些属性
print(arr1.shape)
print(arr1.ndim)  #返回数组的维数，int型，这里是1维
print(arr1.dtype)
print(arr2.shape) #tuple型，返回数组的尺寸，2行3列
print(arr2.ndim) #这里是2维
print(arr2.dtype) #描述数组中元素的类型

arr3 = np.array([[[3,4,2],[5,2,3]],[[3,4,2],[5,2,3]]],)
print(arr3.shape) #(2, 2, 3)

arr4 = np.array([3,4.5,2])
print(arr4.dtype) #float64