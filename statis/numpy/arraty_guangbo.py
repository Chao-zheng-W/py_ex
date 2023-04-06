#数组的广播操作
import numpy as np
arr1 = np.arange(1,13).reshape(4,3)
print(arr1)
arr2 = np.array([1,2,3])
print(arr2)
print(arr1+arr2)  #自动扩展arr2，1列的数组同理

print('------------------')
arr3 = np.array([[1],[2],[3],[4]])
print(arr1)
print(arr3)
print(arr1+arr3)