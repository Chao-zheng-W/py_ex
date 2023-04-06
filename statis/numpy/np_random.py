import numpy as np

#生成随机数
print(np.random.random(10))
print(np.random.random([2,3])) #生成0-1之间的随机数组，可以规定尺寸

print(np.random.rand(10)) #生成符合均匀分布的随机数组，可以规定尺寸
print(np.random.rand(2,3))  #注意和random区别，用元组规定尺寸

print(np.random.randn(10)) #生成符合正态分布的随机数组，用元组规定尺寸
print(np.random.randn(2,3))