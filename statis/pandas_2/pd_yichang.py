#处理异常值outlier
import pandas as pd
import matplotlib.pyplot as  plt
import numpy as np

outlier_test = pd.read_excel('data\\outlier_test.xlsx')
print(outlier_test)

#用箱线图检测异常值
plt.boxplot(outlier_test['amounts'])
plt.show()  #有一个outlier

#定义函数，找出异常值，并转换为空值
def replace(x):
    QU = x.quantile(0.75)  #上四分位值
    QL = x.quantile(0.25)  #上四分位值
    IQR = QU - QL          #间距
    x[x < (QL-1.5*IQR)]= np.nan  #用了逻辑索引，把偏小的离群值改为空
    x[x > (QU + 1.5 * IQR)] = np.nan  # 用了逻辑索引，把偏大的离群值改为空
    print(x)
    return x

replace(outlier_test['amounts'])
