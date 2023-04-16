#使用cookie登录
import requests

#完成登录后刷新网页，可以再network里找到,复制下来.做了脱敏
cookies ='gr_user_id=###; acw_tc=##; JSESSIONID=5##8'

#直接和get方法发送时，要用字典。
Cookie = {}
for i in cookies.split('; '): #用;切割，得到列表
    key, value = i.split('=')  #再用=切割，得到键值对
    Cookie[key] = value


url = 'https://www.ptpress.com.cn/'
rq = requests.get(url,cookies=Cookie)

