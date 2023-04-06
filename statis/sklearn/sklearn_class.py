#创建和评价分类模型，以决策树为例
from sklearn.datasets import load_iris
iris = load_iris(return_X_y=True)  #用元组取出了data 和target，参数用法可以ctrl+左键函数查询到
print(iris)

#数据拆分训练集和测试集,这里有一定随机性，所以每次运行结果可能不一样
from sklearn.model_selection import train_test_split
data_train, data_test, target_train, target_test = train_test_split(iris[0],iris[1],test_size=0.2,stratify=iris[1])
print(data_train.shape,data_test.shape)
print(target_train.shape,target_test.shape)

#导入决策树,使用data_train和target_train训练模型
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier().fit(data_train,target_train)
print(clf.classes_)  #有3个class，是已知信息
print(clf.feature_importances_)  #iris['data']中四列feature_importances_的权重，影响大小；最后一个有约90%

#把测试集给模型，验证模型效果
preticted = clf.predict(data_test)
print(preticted)
print(target_test)    #效果非常好

#量化模型效果
from sklearn.metrics import classification_report
print(classification_report(target_test,preticted))
