#numpy直接和.txt文件交互
import numpy as np
arr1 = np.arange(1,13).reshape(3,4)
np.savetxt('arr1txt.txt',arr1) #元素间默认用空格分割,整形会变成浮点型
arr2 = np.loadtxt('arr1txt.txt')
print(arr2)

arr3 = np.arange(1,13).reshape(3,4)
np.savetxt('arr3txt.txt',arr3,delimiter=',') #元素间改成逗号分割
#arr4 = np.loadtxt('arr3txt.txt')  #报错，逗号分割没办法成数组
with open("arr3txt.txt",'r',encoding='utf-8') as files:
    arr4 = files.readlines()
    print(arr4)