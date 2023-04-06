#创建和评价聚类模型
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

iris= load_iris()
kmeans = KMeans(n_clusters=3).fit(iris['data']) #对鸢尾花数据分成3类
print(kmeans.labels_)
print(iris['target'])  #与原始数据比较会发现后100个分类效果不太好

#当已知target时对聚类模型进行评价
from sklearn.metrics import adjusted_rand_score
score1 = adjusted_rand_score(iris['target'],kmeans.labels_)
print(score1)  #这个值越接近1越好

#实际业务场景中更多是未知target，如何评价聚类的好坏
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

score= []
for i in range(2,7):
    iris = load_iris()
    kmeans = KMeans(n_clusters=i).fit(iris['data'])
    sil_score= silhouette_score(iris['data'],kmeans.labels_)
    score.append(sil_score)

plt.plot(range(2,7), score,marker='o')  #n_clusters=5时两边畸变程度大，比较好
plt.show()