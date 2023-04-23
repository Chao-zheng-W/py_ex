s='hello world python'
print(s.split())  #分割，生成列表

s2='hello|world|python'
print(s2.split('|'))  #读取分隔符，生成列表
print(s2.split('|',maxsplit=1)) #添加分隔次数参数

print(s2.rsplit('|',maxsplit=1)) #从右分隔