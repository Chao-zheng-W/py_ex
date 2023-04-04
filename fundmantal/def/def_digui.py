'''计算6的阶乘'''

def fun(n):
    if n==1:
        return 1
    else:
        res = n*fun(n-1)
        print(res)
        print(n)
        return res

print(fun(6))