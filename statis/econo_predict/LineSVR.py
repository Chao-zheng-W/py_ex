'''
1、本来要有个灰色模型GM11预测后两年的特征值，
    但是视频中要自己定义函数，有点麻烦
    所以跳过，直接拿后两年的值预测
2、直接用支持向量机下的线性回归方法
'''

import pandas as pd
from sklearn.svm import LinearSVR
import matplotlib.pyplot as plt

data_new = pd.read_csv('data_new.csv')

data_tr_mean = data_new.mean()
data_tr_std = data_new.std()

#数据标准化
data_tr = (data_new - data_tr_mean) / data_tr_std

#模型训练
svr = LinearSVR()
svr.fit(data_tr.iloc[:,:8],data_new['y'])  #没有对标签进行归一化,用归一化数据没法收敛
y_pre = svr.predict(data_tr.iloc[:,:8])    #有很大问题，但是不知道问题在哪。
data_new['y_pre'] = y_pre

#结果可视化
fig,a = plt.subplots(2,1)
a[0].plot(range(1993,2013),data_new['y_pre'])
a[1].plot(range(1993,2013),data_new['y'])
plt.show()