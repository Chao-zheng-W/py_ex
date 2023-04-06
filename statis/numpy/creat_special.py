#创建特殊数组

import numpy as np


arr1 = np.arange(2,10) #创建一维数组，左闭又开区间
arr2 = np.arange(2,10,2)  #规定步长为2
arr3 = np.arange(10)  #默认从0开始
print(arr1)
print(arr2)
print(arr3)

arr4 = np.linspace(2,10,9) #与np.arange的区别是，最后一个参数代表要产生的元素数量
print(arr4)

arr0 = np.zeros([2,3]) #生成一个2行3列的全零数组
print(arr0)
