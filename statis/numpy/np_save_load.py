#保存和读取数据,相比.txt文件更小，实际用得更多
import numpy as np
arr1 = np.arange(1,13).reshape(3,4)
print(arr1)

np.save('arr1.npy',arr1) #按照二进制保存文件
arr1_1 = np.load('arr1.npy') #读取文件
print(arr1_1)

print('----------------------')
arr2 = np.arange(1,13).reshape(4,3)
np.savez('tmp/arr1&2.npz',arr1,arr2)  #保存多个变量时，方法不同,文件后缀不同。可以保存在文件夹下，写出路径即可。
arr1_2_load = np.load('tmp/arr1&2.npz') #读取文件
print(arr1_2_load)  #多变量存储在一个变量中
print(arr1_2_load.files) #通过.files方法查看有哪些变量

print(arr1_2_load['arr_0'])  #输入具体的变量名查看

for i in arr1_2_load:  #遍历也没办法看到
    print(i)