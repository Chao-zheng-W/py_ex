from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.ptpress.com.cn/')


with open('page_source.txt','w',encoding='utf-8') as f:
    f.write(driver.page_source)  #获取网页源码，可以发现和requests的结果不一样，这里所见即所得。
