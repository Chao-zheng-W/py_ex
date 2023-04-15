'''
selenium调用谷歌浏览器
使用shift+alt+E调试
不要直接run，会闪退浏览器，无法操作
'''

##1、用代码发送点击命令
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.ptpress.com.cn/')   #到此打开网页

from selenium.webdriver.support.ui import WebDriverWait   #导入
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver,10)  #设置等待时常，考虑到网速
confirm_btn = wait.until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR,'#master > div.list > div:nth-child(1) > div > a > div > img')   #定位按钮位置，在可点击位置右键两次检查，相应代码位置右键copy selector。
    )                          #比如这里选择“精品力作”的第一本书
)
confirm_btn.click()  #点击操作


##2、用代码给搜索框发送输入命令
search_btn = driver.find_element(
    By.CSS_SELECTOR,
    '#header > div.container > div > div.col-md-8.tools > div.search > input[type=text]'  #定位按钮，方法同上
)
search_btn.send_keys('Python网络爬虫')   #点击搜索操作同上


##3、当打开多个页面时，检测和跳转。先手动打开好主页，精品力作1，精品力作2
windows_gui = driver.window_handles
print(windows_gui)  #有三个
driver.switch_to.window(windows_gui[1])  #转到索引第一个









