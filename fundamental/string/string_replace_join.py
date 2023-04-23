s = 'hello Python Java'
print(s.replace("Java",'Python'))

s2 = 'hello Java Java Java'
print(s2.replace("Java",'Python',2))

lst = ['hello','Python','Java']
print('|'.join(lst)) #列表可以合并，用指定的符号
print(''.join(lst))

t = ('hello','Python','Java')
print('|'.join(lst)) #元组可以合并，用指定的符号
