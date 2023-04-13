#获取网页源代码
import requests
import chardet

url = "http://tipdm.com/"
rg = requests.get(url)
print("状态码",rg.status_code)
print('响应头',rg.headers)
print('网页源码',rg.text)   #rg.content是byte型，rg.text是str类型

with open('rg_text.txt','w',encoding='utf-8') as f:
    f.write(rg.text)

url = "http://tipdm.com/"
rg = requests.get(url,timeout=2)  #截止时间2秒，防止意外如断网无法获取到网页源码导致的卡住
print(chardet.detect(rg.content))  #获取字符编码方式