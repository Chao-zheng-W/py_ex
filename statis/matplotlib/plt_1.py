import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,1.1,0.1)
print(x)

plt.figure(num=1)  #第一环节：创建画布
plt.plot(x,x**2)   #第二环节：画出线
plt.plot(x,x**4)   #第二环节：依然在上面画布里，画出第二条线
plt.show()         #第三环节：展示图像

plt.figure(num=2)  #第一环节：创建新画布
plt.plot(x,x**6)   #第二环节：画出线
plt.show()         #第三环节：展示图像
