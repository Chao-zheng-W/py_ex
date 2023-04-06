#划分训练集和测试集
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import pandas as pd

iris = load_iris()
print(pd.Series(iris['target']).value_counts())  #计算每个值的数量

#训练集占0.8，测试集占0.2
#为了不偏离，一般会保证target中类别数量一致，用stratify参数限定
data_train, data_test, target_train, target_test = train_test_split(iris['data'],iris['target'],test_size=0.2,stratify=iris['target'])

print(data_train.shape, data_train)
print(target_train.shape, target_train)
print(pd.Series(target_train).value_counts())
