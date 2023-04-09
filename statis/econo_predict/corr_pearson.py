#探索性分析，看特征值间的相关系数
import pandas as pd

inputfile = 'data.csv'

data= pd.read_csv(inputfile)
print(data.corr(method='pearson'))  #得到相关系数矩阵

'''
除了x11，其他都对y有比较大的影响
各特征间，除了x11都有比较大的相关性
'''
