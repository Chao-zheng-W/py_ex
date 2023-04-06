#求解距离矩阵。假设平面有n个点，求任意两点的距离，并放在一个n*n的矩阵里
import numpy as np
n = 5 #
x = np.linspace(1,100,n) #点的横坐标，linspace表示等差数列
y = np.linspace(1,100,n) #点的纵坐标
dict = np.zeros([n,n])  #初始化距离矩阵，全都是0

print(x)
print(y)
print(dict)

for i in range(n):
    for j in range(n):
        dict[i,j] = np.sqrt((x[i]-x[j])**2 + (y[i]-y[j])**2)  #求解欧式距离，并放到矩阵对应位置

print(dict)