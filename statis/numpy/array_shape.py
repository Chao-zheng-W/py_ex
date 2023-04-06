import numpy as np
#修改数组的形态，但是要保证元素能够满足，否则报错
arr1= np.arange(12).reshape(3,4)
print(arr1)
arr2 =arr1.reshape(2,6)
print(arr2)

#数组展平的两个操作
print(arr1.flatten())
print(arr2.ravel())

#将两个数组拼接，要保证行或列某一个长度相等
print(np.vstack([arr1,arr1]))  #按列拼接，拼接的数组要放在一个列表或元组里
print(np.vstack((arr1,arr1)))  #按行拼接，
