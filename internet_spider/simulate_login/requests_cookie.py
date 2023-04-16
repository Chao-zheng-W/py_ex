#使用cookie登录
import requests

#完成登录后刷新网页，可以再network里找到,复制下来.做了脱敏
cookies ='gr_user_id=###; acw_tc=2760778c16816261833777570e7468ed6e55c46d7a5d3c06fc59614852ccc8; JSESSIONID=5D638DFE7AB233603130C0A5B34B0768'

#直接和get方法发送时，要用字典。
Cookie = {}
for i in cookies.split('; '): #用;切割，得到列表
    key, value = i.split('=')  #再用=切割，得到键值对
    Cookie[key] = value


url = 'https://www.ptpress.com.cn/'
rq = requests.get(url,cookies=Cookie)

