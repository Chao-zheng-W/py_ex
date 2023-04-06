##构建和评价线性回归模型

#用到的包、库
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

#导入数据集
housing = fetch_california_housing()
#print(housing.keys())
#print(housing['DESCR'])
#print(housing['target'])

#分割数据集
data_train, data_test,target_train, target_test=train_test_split(housing['data'],housing['target'],test_size=0.2)
print(data_train.shape,data_test.shape)
print(target_train.shape,target_test.shape)

#创建和训练模型
model = LinearRegression().fit(data_train,target_train)

#模型属性
print(model.coef_)       #线性模型各变量系数
print(model.intercept_)  #线性模型的截距

#可视化定性评估
predicted = model.predict(data_test)  #拿测试集给模型预测
plt.figure()
plt.plot(range(len(target_test)),predicted)
plt.plot(range(len(target_test)),target_test,'r-.')
plt.show()

#定量评估
print(mean_squared_error(target_test,predicted)) #这个值越接近0越好，说明预测误差越小，根据实际业务需要判定