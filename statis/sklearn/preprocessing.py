#sklearn集成了对数据的预处理，比如标准化
from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler  #标准化包
from sklearn.model_selection import train_test_split

iris = load_iris()
data_train, data_test, target_train, target_test = train_test_split(iris['data'],iris['target'],test_size=0.2,stratify=iris['target'])

min_max_scaler = MinMaxScaler().fit(data_train)  #生成转换器，在这个例子中就是用data_train的最大值和最小值。
print(min_max_scaler.transform(data_train))
#用同样的转化器也可以处理其他数据，但是可能会有异常值，因为最小值比data_train的最小值要小，或者最大值比data_train的最大值要大
print(min_max_scaler.transform(data_test))

#或者一步到位，不要转换器
print(MinMaxScaler().fit_transform(data_train))


