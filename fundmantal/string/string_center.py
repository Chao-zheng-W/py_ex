a = 'hello,python'
print(a.center(20,"$")) #居中对齐，后一个参数为填充符号
print(a.ljust(20,"$")) #左对齐，后一个参数为填充符号
print(a.rjust(20,"$")) #左对齐，后一个参数为填充符号

print(a.zfill(20)) #右对齐，用0填充
print('-1024'.zfill(20)) #右对齐。特例，用0填充，在负号里