import time
print(time.localtime(time.time()))  #输出现在时间

import sys
print(sys.getsizeof(35))
print(sys.getsizeof(8.0))
print(sys.getsizeof("8.0"))
print(sys.getsizeof(True))  #获取使用内存的大小

#演示系统自带模块，还有其他的