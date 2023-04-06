#矩阵的相关操作
import numpy as np
matr1 = np.mat('1,2,3;4,5,6;7,8,9') #用分号；表示不同行
matr2 = np.matrix('1,2,3;4,5,6;7,8,9')
print(matr1,type(matr1))
print(matr2,type(matr1))

#矩阵可以拼接
print('--------------------')
print(np.bmat('matr1,matr2'))
print('--------------------')
print(np.bmat('matr1;matr2'))
print('--------------------')
print(np.bmat('matr1,matr2;matr1,matr2'))

matr3 = np.matrix('1,2,3;4,5,6')
#矩阵的属性
print(matr1.T) #转置
print(matr2.I) #求逆