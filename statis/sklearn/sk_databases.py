#导入数据集
from sklearn.datasets import load_breast_cancer  #癌症数据集

cancer = load_breast_cancer()
#print(cancer)
#print(cancer.keys())
#print(cancer['DESCR'])
#print(cancer['filename'])
#print(cancer['data'].shape,cancer['data'])  #569行，30列

from sklearn.datasets import load_iris  #鸢尾花数据集
iris = load_iris()
print(iris.keys())
print(iris['DESCR'])