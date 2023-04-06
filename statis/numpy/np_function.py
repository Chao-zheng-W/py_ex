import numpy as np
#通用函数
arr1 = np.array([1,2,3])
arr2 = np.array([-1,0,5])
lis1 =list([1,2,3])

print(arr1 + 1)
#print(lis1 + 1) #非法操作

print(arr1 * 2)
print(lis1 * 2)  #结果是复制一遍

print(arr1 * arr2)  #对应元素相乘
print(arr1 + arr2)  #对应元素相加

print(arr1 > arr2) #返回布尔值

#逻辑运算
print('----------------')
print(arr1 > 2)
print(np.any(arr1 > 2))  #相当于or，只要有True,返回True
print(np.all(arr1 > 2))  #相当于and，全部都是True,返回True