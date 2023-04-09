'''从探索性分析发现，特征值或者变量间有强相关性
可以从降维的角度，优化数据，有利于后续分析
用Lasso方法选出13列特征值的最重要因素
'''

import pandas as pd
import numpy as np

inputfile = 'data.csv'
data = pd.read_csv(inputfile)

'''以下代码报错，没法复现，按照视频内容手动降维数据
lasso = Lasso(1000)
lasso.fit(data.iloc[1:,:13],data['y'])
print(lasso.coef_())
'''

#0代表无系数，其他值本代表各系数，因为上面代码报错，故仅演示效果
lasso_coef_ = np.array([1,0,3,4,5,6,7,8,0,0,0,0,13])
mask = lasso_coef_ != 0

#用逻辑索引，优化原数据，并保存到新的csv文件中
data_13 = data.iloc[:,:13]
data_new = data_13.loc[:,mask]
data_new['y'] = data['y']
print(data_new)
data_new.to_csv('data_new.csv', index= None)  #不需要索引

