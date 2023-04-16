#使用post方法提交表单，模拟登录
import requests

'''
获取验证码比较麻烦，用开发者工具找到验证码的url
然后根据url保存下来图片，再人工目读，速度稍微快点，验证码可能会更新
'''

verifyCode_url = 'https://www.ptpress.com.cn//kaptcha.jpg?v=0.3572469384343393'  #可以发现每次刷新都会换照片
s = requests.session()  #为保证请求的连贯性都放在一个session下面，从而验证码不改变
rq = s.get(verifyCode_url)

with open('D:\py_ex\internet_spider\simulate_login\\verifycode.png','wb') as f:
    f.write(rq.content)  #在内存中运行，而不会写到硬盘中

'''
进入登录页面，打开开发者工具，选择network，找到和登录相关的包
这里是login，通用头中有要提交给的url
在login包下payload模块form data是要提交的数据，按照相应名称构造表单'''

url = 'https://www.ptpress.com.cn/login'
username = '##'
password = '##'
verifyCode = '##'

data = {
    'username':username,
    'password':password,
    'verifyCode':verifyCode
}

rq = s.post(url,data)
print(rq.status_code)
