class Cpu():
    pass
class Disk():
    pass
class Computer():
    def __init__(self,cpu,disk):
        self.cpu = cpu
        self.disk = disk

#(1)实例对象的赋值
cpu1 = Cpu()
cpu2 = cpu1
print(id(cpu1))
print(id(cpu2))  #内存地址一致

#（2）浅拷贝，创建新的主对象，子对象不变
disk1 =Disk()
computer1 = Computer(cpu1,disk1)
import copy
computer2 = copy.copy(computer1)
print(computer1,computer1.cpu,computer1.disk)
print(computer2,computer2.cpu,computer2.disk)  #与上面对比，主对象有了新的，子对象不变

#（3）深拷贝，新的主对象，新的子对象
computer3 = copy.deepcopy(computer1)
print(computer1,computer1.cpu,computer1.disk)
print(computer3,computer3.cpu,computer3.disk)  #与上面对比，主对象有了新的，子对象也是新的